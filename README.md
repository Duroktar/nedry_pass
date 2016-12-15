Nedry-Pass Password Protection
===============================
**A security package for those tough jobs!**

![logo](https://github.com/Duroktar/nedry_pass/blob/master/nedry_pass/front.JPG)
Overview
--------

Protect your data like a boss with Nedry-Pass.
Developed by a top Computer Scientist at a World Renown Mega-Resort. This sort of protection
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

```python
from nedry_pass import YouDidntSayTheMagicWord

raise YouDidntSayTheMagicWord
```

or use the built in getpass override

```python
from nedry_pass import getpass

secret = 'fini.obj'
getpass(secret)
```

OR live out the original scene (slightly modified) from the comfort of your own home

    $ wht_rbt.obj

Changes
-------
Version 0.0.6:
 - Fixed IndexError on no input.


Version 0.0.5:
 - Refactored a lot of code and added comments.
 - Added wht_rbt.obj as runnable script like in the book.

Disclaimer
----------
This package is merely a form of fan art and in no way intends to infringe on any copyrights held by their respective
owners.

Credits
-------
Scott Doucet, 2016

version number: ![PyPI](https://img.shields.io/pypi/v/nedry-pass.svg)

[![PyPI downloads](https://img.shields.io/pypi/dm/nedry-pass.svg)](https://pypi.python.org/pypi/nedry-pass)
