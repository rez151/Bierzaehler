#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.23a
#  in conjunction with Tcl version 8.6
#    Jun 11, 2019 05:12:44 PM CEST  platform: Linux

import sys

import bierprototype
from sensormanager.sensormanager import Sensormanager

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def set_Tk_var():
    global sensormanager
    sensormanager = Sensormanager()
    global txt_inhalt
    txt_inhalt = tk.StringVar()
    txt_inhalt.set('{:03.3f}'.format(sensormanager.current_state["inhalt"]) + " l")
    global txt_gesamtverbrauch
    txt_gesamtverbrauch = tk.StringVar()
    txt_gesamtverbrauch.set('{:07.1f}'.format(sensormanager.current_state["gesamtverbrauch"]) + " l")


def refresh():
    txt_inhalt.set('{:03.3f}'.format(sensormanager.current_state["inhalt"]) + " l")
    txt_gesamtverbrauch.set('{:07.1f}'.format(sensormanager.current_state["gesamtverbrauch"]) + " l")


def manual():
    print('bierprototype_support.manual')
    sys.stdout.flush()


def ok():
    print('bierprototype_support.ok')

    for x in range(1000):
        sensormanager.count_pulse()

    sys.stdout.flush()


def p():
    print('bierprototype_support.p')
    sys.stdout.flush()


def reset():
    print('bierprototype_support.reset')
    sensormanager.reset()
    sys.stdout.flush()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    bierprototype.vp_start_gui()
