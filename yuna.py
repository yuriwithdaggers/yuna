import requests
from base64 import b64encode
import urllib3

import time

#Se não desativar isso, fica dando warning de requisição insegura.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sessao = requests.session()

#clean code friendly
class Auth:
    def __init__(self, nomeProcesso, idProcesso, porta, senha, protocolo):
        self.nomeProcesso = nomeProcesso
        self.idProcesso = idProcesso
        self.porta = porta
        self.senha = senha
        self.protocolo = protocolo

#Procura o arquivo necessário pra autentificar as requisições
def lockfile():
    #Arquivo de autentificação do LoL para requests
    lock_file = ""
    #O LoL precisa estar aberto para gerar o lockfile.
    caminhoLockfile = r"C:\Riot Games\League of Legends\lockfile"
    lock_file = open(caminhoLockfile)
    lock_file_data = lock_file.read()
    #Terminou de ler o lockfile

    lock_file_data = lock_file_data.split(':')

    autorization = Auth(lock_file_data[0], lock_file_data[1], lock_file_data[2], lock_file_data[3], lock_file_data[4])
    return autorization

#A requisição precisa ser encriptada, nome auto-explicativo
def encriptaHeaders(senha):
    base64 = b64encode(bytes(f'riot:{senha}', 'utf-8')).decode('ascii')
    headers = { 'Authorization': f'Basic {base64}'}
    return headers

lockInfo = lockfile()
headers = encriptaHeaders(lockInfo.senha)

#Aqui é onde a mágica acontece
def requisicao(metodo, endpoint, acao=''):
    url = f'{lockInfo.protocolo}://127.0.0.1:{lockInfo.porta}{endpoint}'

    find = getattr(sessao, metodo)

    if acao:
        request = find(url, verify=False, headers=headers, json=acao)
    else:
        request = find(url, verify=False, headers=headers)

    return request
