"""
function wrappers needed to use this package
"""

import io
import urllib

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from df_python_wrappers.tk_wrapper.config import WINDOW_BAR_HEIGHT


def compute_corner_position(side, master):
    topx = master.winfo_x()
    topy = master.winfo_y()
    height = master.winfo_height()
    width = master.winfo_width()
    if side == "w":
        x = topx - width
        y = topy + height
    elif side == "n":
        x = topx - width
        y = topy - height - WINDOW_BAR_HEIGHT
    elif side == "s":
        x = topx
        y = topy + height + WINDOW_BAR_HEIGHT
    elif side == "e":
        x = topx + width
        y = topy
    else:
        raise ValueError("Unknown Side: " + str(side))
    return x, y


def new_wrapper(p, master, the_type, **kwargs):
    def new_wrapper_int():
        master.update()
        new_window = tk.Toplevel(master)
        res = the_type(p, new_window)
        res.update()

        if "side" not in kwargs:
            kwargs["side"] = "s"

        side = kwargs["side"]
        x, y = compute_corner_position(side, master)

        res.set_position_top_left(x, y)
        return res

    return new_wrapper_int


def new_wrapper_exec(p, master, the_type, **kwargs):
    f = new_wrapper(p, master, the_type, **kwargs)
    r = f()
    return r


def file_select_wrapper(the_v):
    def file_select_wrapper_int():
        the_v.set(filedialog.askopenfilename())

    return file_select_wrapper_int


def stringvar(**kwargs):
    v = tk.StringVar()
    if "default" in kwargs:
        v.set(kwargs["default"])
    return v


# list needed because tk doesn't keep a proper reference
# http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
images_list = []


def image_from_url(url, **kwargs):
    raw_data = urllib.request.urlopen(url).read()
    im_raw = Image.open(io.BytesIO(raw_data))
    # FIXME - trouble displaying PNG images otherwise
    im = im_raw.convert('RGB')

    if 'scale' in kwargs:
        x = kwargs['scale']
        s = im.size
        size_new = (int(s[0] * x), int(s[1] * x))
        im.thumbnail(size_new)

    pim = ImageTk.PhotoImage(im)
    images_list.append(pim)
    return pim


def callback_wrapper(callback_function):
    # these are the args on raw tk callbacks
    # we don't care here
    def callback_wrapper_int(_name, _index, _mode):
        callback_function()

    return callback_wrapper_int


def register_callback_on_write(var, callback):
    cb_func = callback_wrapper(callback)
    var.trace_add("write", cb_func)


def clear_scrolled_text(widget):
    widget.delete(1.0, tk.END)

# eof
