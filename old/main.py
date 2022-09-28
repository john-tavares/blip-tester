from blip.client import BlipClient
from blip.receiver import BlipReceiver

client = BlipClient(cellphone='', api_key='', contract='lanum')
receiver = BlipReceiver(cellphone='', api_key='', contract='lanum')

receiver_identity = client.request_identity(receiver.cellphone)
client_identity = receiver.request_identity(client.cellphone)

print(receiver_identity, client_identity)

client.start_conversation(receiver_identity)
#client.send_message(receiver_identity, 'Teste')
#receiver.send_message(client_identity, 'Teste')

messages = receiver.get_last_message(client_identity)
for message in messages:
    print(message['direction'], message['content'])