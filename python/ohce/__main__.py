from ohce.greeter import Greeter, SystemClock
from ohce.ui import UI, ConsoleInteractor


def main():
    system_clock = SystemClock()
    greeter = Greeter(system_clock)
    greetings = greeter.greet()
    print(greetings)
    
    console_interactor = ConsoleInteractor()
    ui = UI(console_interactor)
    ui.main_loop()


main()
