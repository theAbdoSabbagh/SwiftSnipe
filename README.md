
# Discord Name Sniper

[](https://github.com/your-username/discord-name-sniper/stargazers)

> Please consider leaving a ⭐ on the repository to support me.

### IMPORTANT NOTICE!
> Make sure to set a high delay just to be safe and avoid your account getting deactivated for suspecious usage.
### Why Use Discord Name Sniper?
> Discord has introduced a new naming system that eliminates discriminators, allowing only unique names. All Discord users are required to change their names accordingly. The article linked [here](https://support.discord.com/hc/en-us/articles/12620128861463-New-Usernames-Display-Names)  provides a comprehensive understanding of the changes. It is crucial to note that the older the account, the sooner you will be able to change your name, as explained in the article.
### Key Features
- Multiple tokens
- Individual lists of names to be sniped for each token
- Customizable delays to enhance sniping efficiency and maximize security
- Webhook support for real-time notifications
### Response Codes
> Important! These responses are just assumptions because there weren't any other than 401 since nobody could rename themselves yet.

| Status | Description                                      |
| ------ | ------------------------------------------------ |
| 200    | Successfully sniped a name                       |
| 400    | The name is already taken                        |
| 401    | You are not yet authorized to change your name   |
| 429    | You make too many requests. Increase your delays |

### Configuration 
- `namelists`: An object containing lists of names. The order of the lists determines their priority. 
- `accounts`: An array of objects, each containing a token and a list of name list names. The order of the name lists determines their priority. 
- `delays` 
  - `retry`: Number of seconds to wait before attempting again if you are still ineligible to change your name. 
  - `nameRetry`: Number of seconds to wait before trying the next name in the list if you are eligible to change your name. 
- `webhook` 
  - `enabled`: Boolean value to enable or disable webhook functionality. 
  - `url`: URL of the webhook. 
  - `sendFailures`: Boolean value to enable or disable sending failure notifications to the webhook. 
  - `pingRoleId` (optional): ID of the role to mention on successful snipes.
##### Example Configuration

```json

{
    "namelists": {
       "mynames": ["iwannasnipethisname", "andthisonetoo"],
       "mynamestwo": ["phil", "notphil"]
    },
    "accounts": [
        {
            "token": "********.***.**************",
            "namelists": ["mynames", "mynamestwo"]
        },
        {
            "token": "********.***.**************",
            "namelists": ["mynamestwo"]
        }
    ],
    "delays": {
        "retry": 300,
        "nameRetry": 10
    },
    "webhook": {
        "enabled": false,
        "url": "",
        "pingRoleId": "",
        "sendFailures": false
    }
}
```


### Usage Instructions 
`- Coming soon!`

### Build Instructions 
`- Coming soon!`


### Disclaimer
> Please be aware that self-botting is strictly forbidden by Discord's terms of service. By using this program, you assume all risks and consequences. I cannot be held responsible for any account suspensions or penalties that may occur.
