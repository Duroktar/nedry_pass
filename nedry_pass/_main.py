#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nedry-Pass


Copyright (c) 2016, Scott Doucet
All rights reserved.
"""
import os as _os
import sys as _sys
import itertools as _it
import platform as _platform
import threading as _threading
import contextlib as _contextlib
from glob import glob1 as _glob
from time import sleep as _sleep
from getpass import getpass as _gp
from os.path import abspath as _abspath
from os.path import dirname as _dirname
from os.path import join as _join

try:
    import winsound as _winsound
except ImportError:
    _winsound = None
try:
    # Python2
    import Tkinter as _tk
except ImportError:
    # Python3
    import tkinter as _tk

__all__ = ['YouDidntSayTheMagicWord', 'getpass', 'access_main_program']

_PATH = _dirname(_abspath(__file__))


class YouDidntSayTheMagicWord(Exception):
    """
        Custom YouDidntSayTheMagicWord exception that spams the console with
        "YOU DIDN'T SAY THE MAGIC WORD!" while displaying an animated gif of
        Dennis Nedry wagging his finger with "Uh uh uh, you didn't say the
        magic word." repeating in the background. Why? Because.

    """
    def __init__(self):
        self._console_spam()
        _sleep(0.8)
        self._audio_spam()
        self._gif_spam()
        _sys.exit()

    @staticmethod
    def _console_spam(string=None):
        """
            Spawns a daemon thread that spams "YOU DIDN'T SAY THE MAGIC WORD!"
            to the console.

        :param string:
        :return:
        """
        _string = "YOU DIDN'T SAY THE MAGIC WORD!" if string is None else string

        def run():
            while 1:
                print _string
                _sleep(0.05)

        t1 = _threading.Thread(target=run)
        t1.daemon = True
        t1.start()

    @staticmethod
    def _audio_spam():
        """
            Spawns a daemon thread that spams "Uh uh uh, you didn't say the
            magic word." to the speakers the easiest way possible for "most"
            systems.

        """
        this_sys = _platform.system()
        audiofile = _join(_PATH, 'magic_word.wav')

        def run():
            if this_sys == "Windows":
                flags = _winsound.SND_FILENAME | _winsound.SND_ASYNC | _winsound.SND_LOOP
                _winsound.PlaySound(audiofile, flags)
                while True:
                    _sleep(0.1)
            elif this_sys == "Linux":
                with ignore_stderr():
                    while True:
                        _os.system("play -q " + audiofile)
                        _sleep(0.1)
            else:
                try:
                    with ignore_stderr():
                        while True:
                            _os.system("afplay " + audiofile)
                            _sleep(0.1)
                except OSError:
                    pass

        t1 = _threading.Thread(target=run)
        t1.daemon = True
        t1.start()

    @staticmethod
    def _gif_spam():
        """
            Opens a tkLabel frame that animates the Nedry_0*.gif files onto
            the screen, simulating an animated gif.

        :return: returns on window close
        """
        pics = [_join(_PATH, i) for i in _glob(_PATH, '*.gif')]
        root = _tk.Tk()
        label = _tk.Label(root)
        label.pack(padx=10, pady=10)
        # store as tk img_objects
        pictures = _it.cycle(_tk.PhotoImage(file=img_name) for img_name in pics)
        # milliseconds
        delay = 150

        def animate():
            """ cycle through """
            img = next(pictures)
            label["image"] = img
            root.after(delay, animate)

        animate()
        root.mainloop()


def getpass(to_match, prompt=None, tries=3):
    """
        Function `getpass` that presents defined `prompt` to the user and
        gives 3 default `tries` to input the correct `to_match` password before
        throwing the YouDidntSayTheMagicWord exception.

    :param to_match: password string that user must match to proceed
    :param prompt: console prompt presented to user, defaults to '> '
    :param tries: how many tries the user has to input the correct password
    :return: returns True on correct password guess
    """
    p = '> ' if prompt is None else prompt
    if tries < 0:
        tries = 0
    count = 0
    while count < tries:
        try_pass = _gp(prompt=p) or ""
        if not try_pass == to_match:
            count += 1
            if count != tries:
                print "PERMISSION DENIED."
        else:
            return True
    else:
        print "PERMISSION DENIED....AND....."
        _sleep(0.8)
        raise YouDidntSayTheMagicWord


def access_main_program():
    """
        A function to simulate the scene from the movie. Raises the
        YouDidntSayTheMagicWord exception if "please" not found in user
        input.

    """
    tries = 3
    count = 0
    __pass = "please"
    print "Jurassic Park, System Security Interface\n" \
          "Version 4.0.5, Alpha E \n" \
          "Ready..."
    while count < tries:
        echo = raw_input('> ').split() or ""
        if echo is None:
            echo = ""
        if __pass == echo:
            break
        count += 1
        if count != tries:
            print "ACCESS: PERMISSION DENIED."
        else:
            print "ACCESS: PERMISSION DENIED....AND....."
            _sleep(0.8)
            raise YouDidntSayTheMagicWord


@_contextlib.contextmanager
def ignore_stderr():
    """
        Shuts up some console messages present on linux that were ruining the fun.

    """
    devnull = _os.open(_os.devnull, _os.O_WRONLY)
    old_stderr = _os.dup(2)
    _sys.stderr.flush()
    _os.dup2(devnull, 2)
    _os.close(devnull)
    try:
        yield
    finally:
        _os.dup2(old_stderr, 2)
        _os.close(old_stderr)


if __name__ == '__main__':
    access_main_program()
