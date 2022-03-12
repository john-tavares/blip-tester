from blip.client import BlipTestClient
from blip.flow import BlipFlow

blip = BlipTestClient(
    "Tester", "YmxpcHRlc3Rlcjo2NjMyYjdjYi0yOTNhLTRmMzMtYmRlYi1kYzE1ZGFiZDY1NWM=")

hello_world_flow = BlipFlow(
    'Hello World', blip, ['Hello World'], 'Olá! !<br>Seja2 bem-vindo(a)!')

print(hello_world_flow.test())
