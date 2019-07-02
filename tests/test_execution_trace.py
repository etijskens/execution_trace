#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `execution_trace` package."""

import os
import sys
# import pytest

from click import echo


# Make sure that the current directory is the project directory.
# 'make test" and 'pytest' are generally run from the project directory.
# However, if we run/debug this file in eclipse, we end up in test
if os.getcwd().endswith('tests'):
    echo(f"Changing current working directory"
         f"\n  from '{os.getcwd()}'"
         f"\n  to   '{os.path.abspath(os.path.join(os.getcwd(),'..'))}'\n")
    os.chdir('..')
# Make sure that we can import the module being tested. When running
# 'make test" and 'pytest' in the project directory, the current working
# directory is not automatically added to sys.path.
if not ('.' in sys.path or os.getcwd() in sys.path):
    echo(f"Adding '.' to sys.path.\n")
    sys.path.insert(0, '.')

from execution_trace import trace,print2stderr
from execution_trace import __version__
# ==============================================================================
def test_trace():
    import logging
    log = logging.getLogger('main')
    log.addHandler(logging.StreamHandler(sys.stderr))
    log.setLevel(logging.INFO)
    with trace('executing __main__','finished.',log=log):
        with trace('something',singleline=False):
            # we must print to the same stream, otherwise the printed lines 
            # are not in the right order
            print2stderr('hello')
            print('world')
        with trace('something else'):
            # we must print to the same stream, otherwise the printed lines 
            # are not in the right order
            print2stderr('hello ...',end='')
# ==============================================================================
def test_version():
    assert __version__=="0.0.0"
# ==============================================================================

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_trace
    the_test_you_want_to_debug()
# ==============================================================================
