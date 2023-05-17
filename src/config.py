import json

def write_config_template():
    default_config = {
        "namelists": {},
        "accounts": [],
        "delays": {
        "nameRetry": 300,
        "retry": 3600
        },
        "webhook": {
        "enabled": False,
        "sendFailures": False,
        "pingRoleId": '',
        "url": ''
        }
    }
    with open('config.json', 'w') as file:
        json.dump(default_config, file, indent=2)

def read_parse_config():
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
