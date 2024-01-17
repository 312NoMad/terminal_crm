import sys
import tty
import termios

def get_char():
    # Save the terminal settings
    old_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setraw(sys.stdin.fileno())  # Set the terminal to raw mode
        char = sys.stdin.read(1)  # Read a single character
        return char
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)