from blip.client import BlipTestClient
import time


class BlipFlow:
    def __init__(self, name, client, actions, expected_message):
        self.name = name
        self.__client = client
        self.actions = actions
        self.expected_message = expected_message

    def __start_client(self):
        time.sleep(5)
        self.__client.start_chat()

    def __close_client(self):
        time.sleep(5)
        self.__client.close_chat()

    def run(self):
        self.__start_client()

        for action in self.actions:
            self.__client.send_message(action)
            time.sleep(5)

        last_message = self.__client.last_message

        self.__close_client()

        return last_message

    def test(self):
        last_message = self.run()

        if last_message is None:
            return False

        return last_message['text'] == self.expected_message
