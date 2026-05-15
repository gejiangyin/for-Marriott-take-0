from business import GreetingService

class GreetingController:
    def __init__(self):
        self.service = GreetingService()

    def handle_request(self, user_name: str | None):
        result = self.service.get_greeting(user_name)
        print(f"Response: {result} ")