import requests
from uuid import uuid4

class BlipReceiver:
    def __init__(self, cellphone, api_key:str, contract:str):
        contract = contract+".http." if contract != '' else ''
        
        self.identity = f'{cellphone}@wa.gw.msging.net'
        self.cellphone = cellphone
        self.headers = {'Content-Type': 'application/json', 'Authorization': api_key}
        self.command_url = f'https://{contract}msging.net/commands'
        self.message_url = f'https://{contract}msging.net/messages'
    
    def get_last_message(self, client_identity):
        payload = {  
            "id": uuid4().hex,
            "method": "get",
            "uri": f"/threads/{client_identity}?refreshExpiredMedia=true"
        }
        response = requests.post(self.command_url, headers=self.headers, json=payload).json()
        if 'resource' not in response:
            return []
        
        return response['resource']['items']
    
    def request_identity(self, client_identity:str):
        payload = {
            "id": uuid4().hex,
            "to": "postmaster@wa.gw.msging.net",
            "method": "get",
            "uri": f"lime://wa.gw.msging.net/accounts/{client_identity}"
        }
        response = requests.post(self.command_url, headers=self.headers, json=payload).json()
        
        return response['resource']['alternativeAccount']
    
    def send_message(self, client_identity, message):
        payload = {
            "id": uuid4().hex,
            "to": client_identity,
            "type": "text/plain",
            "content": message
        }
        response = requests.post(self.message_url, headers=self.headers, json=payload)
        return response