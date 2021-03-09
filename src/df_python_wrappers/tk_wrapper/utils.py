"""
core utils
"""

import tkinter as tk

from df_python_wrappers.tk_wrapper.base import HasMasterBase
from df_python_wrappers.tk_wrapper.wrappers import stringvar

# grid layout helper version
class HasMaster(HasMasterBase):
    # no __init__ needed because super does all setup work
    # with the same arguments

    def _get_grid_args(self, **kwargs):
        args_to_pass = ["sticky"]
        kwargs_sub = {}
        for k in kwargs:
            if k in args_to_pass:
                kwargs_sub[k] = kwargs[k]
        return kwargs_sub

    def button_on_grid(self, row, column, **kwargs):
        kwargs_sub = self._get_grid_args(**kwargs)
        b = self.button(**kwargs)
        b.grid(row=row, column=column, **kwargs_sub)

    def checkbutton_on_grid(self, row, col, **kwargs):
        b, v = self.checkbutton(**kwargs)
        b.grid(row=row, column=col)
        return b, v

    def label_on_grid(self, label_text, row, col, **kwargs):
        kwargs_sub = self._get_grid_args(**kwargs)
        kwargs["text"] = label_text
        lbl = self.label(**kwargs)
        lbl.grid(row=row, column=col, **kwargs_sub)
        return lbl

    def empty_on_grid(self, row, col, **kwargs):
        return self.label_on_grid("", row, col, **kwargs)

    def entry_on_grid(self, row, col, **kwargs):
        e = self.entry(**kwargs)
        e.grid(row=row, column=col)
        return e

    def stringvar_entry_on_grid(self, row, col, **kwargs):
        v = stringvar(**kwargs)
        reduced_kwargs = {k: kwargs[k] for k in kwargs.keys() & ["width", "bg"]}
        reduced_kwargs["textvariable"] = v
        e = self.entry_on_grid(row, col, **reduced_kwargs)
        return e, v

    def var_label_on_grid(self, var, row, col):
        lbl = self.label(textvariable=var)
        lbl.grid(row=row, column=col)
        return lbl

    def stringvar_label_on_grid(self, row, col, **kwargs):
        v = stringvar(**kwargs)
        lbl = self.var_label_on_grid(v, row, col)
        return lbl, v

    def scrolled_text_on_grid(self, row, col, **kwargs):
        st = self.scrolled_text(**kwargs)
        st.grid(row=row, column=col)
        return st

    def image_from_url_on_grid(self, url, row, col, **kwargs):
        l = self.image_from_url(url, **kwargs)
        l.grid(row=row, column=col)
        return l

    def popup_menu_on_grid(self, choices, row, col, **kwargs):
        menu, sv = self.popup_menu(choices, **kwargs)
        menu.grid(row=row, column=col)
        return menu, sv

class Root(HasMaster):
    def __init__(self, **kwargs):
        self.the_tk = tk.Tk()
        super().__init__(self.the_tk, **kwargs)

    def mainloop(self):
        self.master().mainloop()

    def get_root(self):
        return self.the_tk

# eof
