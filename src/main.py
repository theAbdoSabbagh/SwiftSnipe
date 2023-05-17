from asyncio import run, sleep
from api import postPomelo
from utils import tokenToId
from config import read_parse_config, write_config_template
from webhook import WebhookSniper
from logger import logger

if not read_parse_config():
    write_config_template()
    logger.info('Successfully created config.json file.')

config = read_parse_config()

if not config['accounts']:
    logger.warning("You have not added any accounts to your config. Was that a mistake?")

accounts = config['accounts']
delays = config['delays']
namelists = config['namelists']
webhookConfig = config['webhook']
enabled = webhookConfig.get('enabled', False)
url = webhookConfig.get('url', '')
pingRoleId = webhookConfig.get('pingRoleId', '')
sendFailures = webhookConfig.get('sendFailures', False)

parsedAccounts = [
    {
        'names': sum([namelists[name] for name in account['namelists'] if name in namelists], []),
        'token': account['token']
    }
    for account in accounts
]

webhook = WebhookSniper(url) if enabled and url else None

async def attemptAccount(account):
    names = account['names']
    token = account['token']
    for name in names:
        status, data = await postPomelo(token, name)
        if status == 200:
            logger.info(f"Successfully sniped username '{name}' for '{token}' {data} {status}")
        else:
            logger.info(f"Failed to snipe username '{name}' for '{token}' {data} {status}")

        if webhook:
            if status == 200:
                webhook.sendSuccessfulSnipe(**{
                    'id_': tokenToId(token),
                    'name': name,
                    'responseBody': data,
                    'statusCode': status,
                    'pingRoleId': pingRoleId
                })
            elif sendFailures:
                webhook.sendFailureSnipe(**{
                    'id_': tokenToId(token),
                    'name': name,
                    'responseBody': data,
                    'statusCode': status
                })

        if data.get('message') == 'Unauthorized':
            return False
        if status == 200:
            return True

        logger.info(f"Sleeping for {delays['nameRetry']} seconds")
        await sleep(delays['nameRetry'])
    
    return False

async def main():
    for account in parsedAccounts:
        while True:
            if await attemptAccount(account):
                return
            logger.info(f"Sleeping for {delays['retry']} seconds")
            await sleep(delays['retry'])

run(main())
