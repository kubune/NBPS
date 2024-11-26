from threading import Thread
import sys
import platform
import tkinter as tk
from tkinter import simpledialog
from NBPS.Server.Extra.Command.Handler import handle_command


if platform.system() == "Windows":
    import msvcrt
elif platform.system() in ["Linux", "Darwin"]:
    import termios
    import tty
else:
    pass

class CommandsHandler(Thread):
    def __init__(self, key="/"):
        super().__init__()
        self.key = key
        self.system = platform.system()

    def get_key(self):
        if self.system == "Windows":
            key = msvcrt.getch()
            try:
                key = key.decode('utf-8')
                return key
            except UnicodeDecodeError:
                return None

        elif self.system in ["Linux", "Darwin"]:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = sys.stdin.read(1)
                return key
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def show_input_box(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        user_input = simpledialog.askstring("Command", "Enter your command:")
        if user_input:
            handle_command(user_input)

    def run(self):
        while True:
            key = self.get_key()
            if key == self.key:
                self.show_input_box()
