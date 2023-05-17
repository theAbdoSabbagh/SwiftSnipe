from discord_webhook import DiscordWebhook, DiscordEmbed
from json import dumps

class WebhookSniper:
    def __init__(self, url: str, username: str = None, avatarUrl: str = None):
        self.webhookClient = DiscordWebhook(
            url = url,
            username = username,
            avatar_url = avatarUrl
        )
        self.avatarUrl = avatarUrl
        self.username = username

    def sendSuccessfulSnipe(self, id_: int, name: str, responseBody, statusCode: int, pingRoleId: int = None):
        embed = DiscordEmbed()
        embed.set_title('Success')
        embed.set_description(f"Successfully sniped username `{name}` for <@{id_}>")
        embed.add_embed_field(name='Response Body', value='```' + dumps(responseBody, indent=2)[:900] + '```')
        embed.add_embed_field(name='Status Code', value=str(statusCode))
        embed.set_timestamp()

        webhook = self.webhookClient
        webhook.remove_embeds()
        webhook.add_embed(embed)
        if pingRoleId:
            webhook.set_content(f'<@&{pingRoleId}>')

        webhook.execute()

    def sendFailureSnipe(self, id_: int, name: str, responseBody, statusCode: int):
        embed = DiscordEmbed()
        embed.set_title('Failure')
        embed.set_description(f"Failed to snipe username `{name}` for <@{id_}>")
        embed.add_embed_field(name='Response Body', value='```' + dumps(responseBody, indent=2)[:900] + '```')
        embed.add_embed_field(name='Status Code', value=str(statusCode))
        embed.set_timestamp()

        webhook = self.webhookClient
        webhook.remove_embeds()
        webhook.add_embed(embed)
        webhook.execute()

if __name__ == '__main__':
    options = {
        'url': 'your_webhook_url',
        'username': 'YourUsername',
        # 'avatarUrl': 'YourAvatarUrl'
    }

    sniper = WebhookSniper(**options)
    sniper.sendSuccessfulSnipe(id_='your_id', name='ExampleUser', responseBody={}, statusCode=200, pingRoleId='your_role_id')
    sniper.sendFailureSnipe(id_='your_id', name='ExampleUser', responseBody={}, statusCode=404)
