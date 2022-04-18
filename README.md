# [Python] Yuna Connector 🔌
**League Client Update connector for you!**

This script returns the credentials needed to interact with the LCU. Allowing to make requests of all methods to League of Legends.
## Download 💻 




- Github `git clone https://github.com/yuriwithdaggers/yuna.git`

## Usage:
```python
requisicao("request method", "lcu endpoint", "action to do")
```
## Usage example
- Get user nickname:

```python
import yuna
import json

def getName():
    request = yuna.requisicao('get', '/lol-summoner/v1/current-summoner')
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
    request = yuna.requisicao("post", "/lol-summoner/v1/current-summoner/summoner-profile", {'key': 'backgroundSkinId', 'value': backgroundId})
    print(request)


changeBackground(~desired background id~)
 👉 // output: <Response [200]>
```
## Code Language 
- The code and environment variables are written in Portuguese, because content on this subject in Portuguese is very rare, so the code aims to be friendly with our friends who don't understand English perfectly.


## ⛔️ 🛑 Disclaimer 🛑 ⛔️


**Yuna Connector is not sponsored or endorsed by Riot Games.**