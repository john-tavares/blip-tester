import requests
from uuid import uuid4

class BlipClient:
    def __init__(self, cellphone, api_key:str, contract:str, start_message='bliptester'):
        contract = contract+".http." if contract != '' else ''
        self.namespace = 'aa3ec985_9c33_4b56_8c1a_0449dc92104a'
        self.start_message = start_message
        self.identity = f'{cellphone}@wa.gw.msging.net'
        self.cellphone = cellphone
        self.headers = {'Content-Type': 'application/json', 'Authorization': api_key}
        self.command_url = f'https://{contract}msging.net/commands'
        self.message_url = f'https://{contract}msging.net/messages'
    
    def request_identity(self, server_identity:str):
        payload = {
            "id": uuid4().hex,
            "to": "postmaster@wa.gw.msging.net",
            "method": "get",
            "uri": f"lime://wa.gw.msging.net/accounts/{server_identity}"
        }
        response = requests.post(self.command_url, headers=self.headers, json=payload).json()
        
        return response['resource']['alternativeAccount']
    
    def start_conversation(self, server_identity):
        payload = {
            "id": uuid4().hex,
            "to": server_identity,
            "type": "application/json",
            "content": {
                "type": "template",
                "template": {
                    "namespace": self.namespace,
                    "name": self.start_message,
                    "language": {
                        "code": "pt_BR",
                        "policy": "deterministic"
                    },
                    "components": []
                }
            }
        }
        response = requests.post(self.message_url, headers=self.headers, json=payload)
        return response
    
    def send_message(self, server_identity, message):
        payload = {
            "id": uuid4().hex,
            "to": server_identity,
            "type": "text/plain",
            "content": message
        }
        response = requests.post(self.message_url, headers=self.headers, json=payload)
        return response