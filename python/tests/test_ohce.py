import pytest
from unittest.mock import MagicMock

from ohce.greeter import Greeter
from ohce.ui import UI


def test_nightly_greeting():
    system_clock = MagicMock("SystemClock")
    system_clock.current_hour = MagicMock(return_value=0)
    assert Greeter(system_clock).greet() == "Good night"


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    pytest.fail("TODO")


def test_ohce_main_loop():
    console_interactor = MagicMock()
    console_interactor.read_input.side_effect = ["hello","oto","quit"]
    console_interactor.print_message = MagicMock()

    UI(console_interactor).main_loop()
    assert  console_interactor.print_message.call_args_list[0].args[0] == "olleh"
    assert console_interactor.print_message.call_args_list[1].args[0] == "That was a palindrome!"
    # assert console_interactor.print_message.call_args_list[2].args[0] == "olleh"
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
