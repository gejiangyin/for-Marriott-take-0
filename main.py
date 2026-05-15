from presentation import GreetingController

if __name__ == "__main__":
    controller = GreetingController()
    controller.handle_request("Alice")
    controller.handle_request(None)
    controller.handle_request("     ")

