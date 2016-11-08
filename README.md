Nedry-Pass Password Protection
===============================

![logo](./nedry_pass/Newman_01.gif)

version number: 0.0.1
author: Scott Doucet

Overview
--------

A security package for those tough jobs. Protect your data like a boss with Nedry-Pass.
Developed by a top Computer Scientist at a World Renown Mega-Resort; this sort of protection
should come with a Warning label!

Installation / Usage
--------------------

To install use pip:

    $ pip install nedry_pass


Or clone the repo:

    $ git clone https://github.com/Duroktar/nedry_pass.git
    $ python setup.py install

Example
-------

Either raise the custom exception yourself

    from nedry_pass import YouDidntSayTheMagicWord

    raise YouDidntSayTheMagicWord

or use the built in getpass override

    from nedry_pass import getpass

    secret = 'fini.obj'
    getpass(secret)

OR live out the original scene (slightly modified) from the comfort of your own home

    from nedry_pass import access_main_program

    access_main_program()

Disclaimer
----------
This package is merely a form of fan art and in no way intends to infringe on any copyrights held by their respective
owners.

Credits
-------
Scott Doucet, 2016
