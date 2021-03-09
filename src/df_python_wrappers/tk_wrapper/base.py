"""
basic base class
contains the core wrappers around tkinter with real
functionality
"""

import tkinter as tk

from tkinter import font
from tkinter.scrolledtext import ScrolledText
from df_python_wrappers.tk_wrapper.wrappers import image_from_url, stringvar
from df_python_wrappers.tk_wrapper.simple import SimpleTKWrapper
from df_python_wrappers.common.DictTools import subdict

# the base tkinter wrapper class
class HasMasterBase(SimpleTKWrapper):
    def __init__(self, master_in, **kwargs):
        super().__init__(master_in, **kwargs)

    def button(self, **kwargs):
        button_args_to_pass = ["background", "textvariable", "text",
                               "image", "width", "command"]
        button_kwargs_sub = subdict(kwargs, button_args_to_pass)
        b = tk.Button(self.master(), **button_kwargs_sub)
        if self.color:
            b.configure(highlightbackground=self.color)
        return b

    def checkbutton(self, **kwargs):
        v = tk.BooleanVar()
        b = tk.Checkbutton(self.master(), variable=v, **kwargs)
        if self.color:
            b.configure(bg=self.color)
        return b, v

    def label(self, **kwargs):
        label_args_to_pass = ["background", "textvariable", "text", "image", "width"]
        label_kwargs_sub = subdict(kwargs, label_args_to_pass)
        if self.color:
            label_kwargs_sub["background"] = self.color
        lbl = tk.Label(self.master(), **label_kwargs_sub)

        if "underline" in kwargs and kwargs["underline"]:
            f = font.Font(lbl, lbl.cget("font"))
            f.configure(underline=True)
            lbl.configure(font=f)

        return lbl

    def image_from_url(self, url, **kwargs):
        pim = image_from_url(url, **kwargs)
        l = self.label(image=pim)
        return l

    def entry(self, **kwargs):
        e = tk.Entry(self.master(), **kwargs)
        return e

    def scrolled_text(self, **kwargs):
        if 'wrap' not in kwargs:
            kwargs['wrap'] = tk.WORD
        st = ScrolledText(self.master(), **kwargs)
        return st

    def popup_menu(self, choices, **kwargs):
        sv = stringvar()
        if 'default' in kwargs:
            sv.set(kwargs['default'])
        menu = tk.OptionMenu(self.master(), sv, *choices)
        max_len = max([len(x) for x in choices])
        # FIXME - seems arbitrary but it is working
        menu.configure(width=int(3 + max_len * 1.0))
        if self.color:
            menu.configure(bg=self.color)
        return menu, sv

# eof
