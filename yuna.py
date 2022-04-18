import requests
from base64 import b64encode
import urllib3

#We need to disable these notifications for the code to work.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.session()

#clean code friendly
class Auth:
    def __init__(self, nameProcess, idProcess, port, passwd, method):
        self.nameProcess = nameProcess
        self.idProcess = idProcess
        self.port = port
        self.passwd = passwd
        self.method = method

#Search for the file needed to authenticate the requests
def lockfile():
    #LoL authentication file for requests
    lock_file = ""
    #LoL needs to be on local disk C to find the file, but you can change this in code.
    pathFile = r"C:\Riot Games\League of Legends\lockfile"
    lock_file = open(pathFile)
    lock_file_data = lock_file.read()
    #Finished reading the lockfile

    lock_file_data = lock_file_data.split(':')

    autorization = Auth(lock_file_data[0], lock_file_data[1], lock_file_data[2], lock_file_data[3], lock_file_data[4])
    return autorization

#The request needs to be encrypted
def encryptHeaders(passwd):
    base64 = b64encode(bytes(f'riot:{passwd}', 'utf-8')).decode('ascii')
    headers = { 'Authorization': f'Basic {base64}'}
    return headers

lockInfo = lockfile()
headers = encryptHeaders(lockInfo.passwd)

#Here is where the magic happens
def yuna(method, endpoint, action=''):
    url = f'{lockInfo.method}://127.0.0.1:{lockInfo.port}{endpoint}'

    #At this point, you are identified and the client recognizes your request as legitimate.

    find = getattr(session, method)

    if action:
        request = find(url, verify=False, headers=headers, json=action)
    else:
        request = find(url, verify=False, headers=headers)

    return request
