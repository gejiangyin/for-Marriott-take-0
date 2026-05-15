class GreetingRepository:
    def get_greeting_from_db(self, name: str) -> str:
        # Simulate fetching greeting from database
        return f"Hello, {name}!"