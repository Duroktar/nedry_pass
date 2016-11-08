#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Copyright 2016 Scott Doucet

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import os as _os
import sys as _sys
from glob import glob1 as _glob
from os.path import dirname as _dirname
from os.path import abspath as _abspath
from os.path import join as _join
from time import sleep as _sleep
from getpass import getpass as _gp
import threading as _threading
import platform as _platform
import contextlib as _contextlib
import itertools as _it
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
    def __init__(self):
        self._console_spam()
        _sleep(0.8)
        self._audio_spam()
        self._gif_spam()
        _sys.exit()

    @staticmethod
    def _console_spam(string=None):
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
        pics = [_join(_PATH, i) for i in _glob(_PATH, '*.gif')]
        _giffer(pics)


def getpass(to_match, prompt=None, tries=3):
    p = '> ' if prompt is None else prompt
    if tries < 0:
        tries = 0
    count = 0
    while count < tries:
        try_pass = _gp(prompt=p)
        if not try_pass == to_match:
            count += 1
            if count != tries:
                print "PERMISSION DENIED."
        else:
            return
    else:
        print "PERMISSION DENIED....AND....."
        _sleep(0.8)
        raise YouDidntSayTheMagicWord


def access_main_program():
    tries = 3
    count = 0
    __pass = "please"
    print "Jurassic Park, System Security Interface\n" \
          "Version 4.0.5, Alpha E \n" \
          "Ready..."
    while count < tries:
        echo = raw_input('> ').split()
        if __pass in echo:
            break
        count += 1
        if count != tries:
            print "{}: PERMISSION DENIED.".format(echo[0])
        else:
            print "{}: PERMISSION DENIED....AND.....".format(echo[0])
            _sleep(0.8)
            raise YouDidntSayTheMagicWord


def _giffer(files):
    root = _tk.Tk()
    label = _tk.Label(root)
    label.pack(padx=10, pady=10)
    # store as tk img_objects
    pictures = _it.cycle(_tk.PhotoImage(file=img_name) for img_name in files)
    # milliseconds
    delay = 150

    def animate():
        """ cycle through """
        img = next(pictures)
        label["image"] = img
        root.after(delay, animate)
    animate()
    root.mainloop()


@_contextlib.contextmanager
def ignore_stderr():
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
    raise YouDidntSayTheMagicWord
