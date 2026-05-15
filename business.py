from data import GreetingRepository

class GreetingService:
    def __init__(self):
        self.repository = GreetingRepository()

    def get_greeting(self, name: str | None) -> str:
        if not name or name.strip() == "":
            name = "Guest"
        
        return self.repository.get_greeting_from_db(name)