# [Python] Yuna Connector 🔌
**League Client Update connector for you!**

This script returns the credentials needed to interact with the LCU. Allowing to make requests of all methods to League of Legends.
## Download 💻 




- Github `git clone https://github.com/yuriwithdaggers/yuna.git`

## Usage:
```python
yuna("request method", "lcu endpoint", "action to do")
```
## Usage example
- Get user nickname:

```python
import yuna
import json

def getName():
    request = yuna.yuna('get', '/lol-summoner/v1/current-summoner')
    response = json.loads(request.content)
    print(response["displayName"])

getName()
👉 // output: your nickname
```
## Usage example
- Change profile background:

```python
import yuna

def changeBackground(backgroundId):
    request = yuna.yuna("post", "/lol-summoner/v1/current-summoner/summoner-profile", {'key': 'backgroundSkinId', 'value': backgroundId})
    print(request)


changeBackground(~desired background id~)
 👉 // output: <Response [200]>
```
## ⛔️ 🛑 Disclaimer 🛑 ⛔️


**Yuna Connector is not sponsored or endorsed by Riot Games.**