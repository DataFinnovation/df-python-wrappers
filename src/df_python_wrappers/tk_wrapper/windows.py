"""
various types of useful utility windows
"""

from df_python_wrappers.tk_wrapper.utils import HasMaster, Root
from df_python_wrappers.tk_wrapper.config import DEFAULT_TEXT_ROW_HEIGHT,\
    DEFAULT_TEXT_CHAR_WIDTH

# built with a callback
# the go method runs the callback and then closes the window
class InitializationWindow(HasMaster):
    def __init__(self, cb, master, **kwargs):
        super().__init__(master, **kwargs)
        self.callback = cb

    def go(self, **kwargs):
        self.callback(**kwargs)
        self.close()

# a basic error popup
# displays a text message
# has a close button
# pops up on top and centered
class ErrorWindow(Root):
    def __init__(self, message):
        h = 2 * DEFAULT_TEXT_ROW_HEIGHT
        w = len(message) * DEFAULT_TEXT_CHAR_WIDTH
        super().__init__(title="ERROR", width=w, height=h)
        self.label_on_grid("ERROR: ", 0, 0)
        self.label_on_grid(message, 0, 1)
        self.button_on_grid(1, 1, text="Close", command=self.quit)
        self.put_in_center()
        self.bring_to_front()

    def quit(self):
        self.master().destroy()

# an error window for fatal errors
# the close button here closes the entire application
# immediately
class FatalErrorWindow(ErrorWindow):
    def __init__(self, message):
        super().__init__(message)
        self.set_title("Fatal Error")

    def quit(self):
        self.toplevel().quit()

# eof
