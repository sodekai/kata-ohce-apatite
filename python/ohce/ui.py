from ohce import reverse


class ConsoleInteractor:
    def read_input(self):
        return input()

    def print_message(self, message):
        print(message)


class UI:
    def __init__(self, console_interactor):
        self.interactor = console_interactor

    def main_loop(self):
        while True:
            input = self.interactor.read_input()
            if input == "quit":
                break
            reversed = reverse(input)

            if reversed == input:
                self.interactor.print_message("That was a palindrome!")

            else : self.interactor.print_message(reversed)