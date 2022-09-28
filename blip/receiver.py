import requests
from uuid import uuid4

class BlipReceiver:
    def __init__(self, cellphone, api_key:str, contract:str):
        self.identity = f'{cellphone}@wa.gw.msging.net'
        self.cellphone = cellphone
        self.headers = {'Content-Type': 'application/json', 'Authorization': api_key}
        self.command_url = f'https://{contract}.http.msging.net/commands'
        self.message_url = f'https://{contract}.http.msging.net/messages'
    
    def get_last_message(self, client_identity):
        payload = {  
            "id": uuid4().hex,
            "method": "get",
            "uri": f"/threads/{client_identity}?refreshExpiredMedia=true"
        }
        response = requests.post(self.command_url, headers=self.headers, json=payload).json()
        print(response)
        
        if 'resource' not in response:
            return []
        
        return response['resource']['items']