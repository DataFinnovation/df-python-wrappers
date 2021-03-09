"""
simpest basic tk wrapper
these wrappers cover naming and basic 2-line stuff
"""

import tkinter as tk

from df_python_wrappers.tk_wrapper.config import DEFAULT_WIDTH, DEFAULT_TEXT_ROW_HEIGHT
from df_python_wrappers.tk_wrapper.config import DEFAULT_HEIGHT

class SimpleTKWrapper:
    def __init__(self, master_in, **kwargs):
        self.the_master = master_in
        self.set_window_size(kwargs.get("width", DEFAULT_WIDTH),
                             kwargs.get("height", DEFAULT_HEIGHT))
        self.color = None
        if self.get_color():
            self.set_color(self.get_color())
        if "title" in kwargs:
            self.set_title(kwargs["title"])
        if self.get_title():
            self.set_title(self.get_title())

    def set_color(self, the_color):
        self.color = the_color
        self.master().configure(background=self.color)

    def get_color(self):
        return self.color

    def close(self):
        self.master().destroy()

    def destroy_all_children(self):
        for w in self.master().winfo_children():
            w.destroy()

    def close_toplevel(self):
        self.toplevel().destroy()

    def get_title(self):
        return None

    def master(self):
        return self.the_master

    def update(self):
        self.master().update()

    def new_frame(self):
        return tk.Frame(self.master())

    def new_window(self):
        return tk.Toplevel(self.master())

    def set_title(self, new_title):
        self.master().title(new_title)

    def set_window_size(self, width, height):
        x, y = self.position()
        self.set_geometry(width, height, x, y)

    def set_position_top_left(self, x, y):
        w, h = self.dims()
        self.set_geometry(w, h, x, y)

    def set_geometry(self, w, h, x, y):
        self.master().geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.master().update()

    def position(self):
        return self.master().winfo_x(), self.master().winfo_y()

    def dims(self):
        return self.master().winfo_width(), self.master().winfo_height()

    def taller(self, increment):
        w, h = self.dims()
        self.set_window_size(w, h+increment)

    def wider(self, increment):
        w, h = self.dims()
        self.set_window_size(w+increment, h)

    def taller_by_text_row(self):
        self.taller(DEFAULT_TEXT_ROW_HEIGHT)

    def bring_to_front(self):
        self.master().lift()
        self.master().attributes('-topmost',True)

    def toplevel(self):
        return self.master().winfo_toplevel()

    def screen_dims(self):
        tl = self.toplevel()
        w = tl.winfo_screenwidth()
        h = tl.winfo_screenheight()
        return w, h

    def all_dims(self):
        return self.dims() + self.screen_dims()

    def put_top_left(self):
        self.set_position_top_left(0, 0)

    def put_top_right(self):
        w_w, _, s_w, _ = self.all_dims()
        self.set_position_top_left(s_w - w_w, 0)

    def put_bottom_left(self):
        _, w_h, _, s_h = self.all_dims()
        self.set_position_top_left(0, s_h - w_h)

    def put_bottom_right(self):
        w_w, w_h, s_w, s_h = self.all_dims()
        self.set_position_top_left(s_w - w_w, s_h - w_h)

    def put_in_center(self):
        w_w, w_h, s_w, s_h = self.all_dims()
        self.set_position_top_left(s_w/2 - w_w/2, s_h/2 - w_h/2)


# eof
