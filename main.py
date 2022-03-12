from blip.client import BlipTestClient
import time

blip = BlipTestClient(
    "Tester", "YmxpcHRlc3Rlcjo2NjMyYjdjYi0yOTNhLTRmMzMtYmRlYi1kYzE1ZGFiZDY1NWM=")

blip.start_chat()

for i in range(5):
    blip.send_message("Oi!")
    time.sleep(5)

blip.close_chat()
