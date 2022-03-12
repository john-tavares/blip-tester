from client import BlipTestClient


class BlipFlow:
    def __init__(self, name, client, actions, expected_message):
        self.name = name
        self.__client = client
        self.actions = actions
        self.expected_message = expected_message
        self

    def __start_client(self):
        self.client.start_chat()

    def __close_client(self):
        self.client.close_chat()

    def run(self):
        self.start_client()

        for action in self.actions:
            self.client.send_message(action)

        last_message = self.client.last_message

        self.close_client()

        return last_message

    def test(self):
        pass
