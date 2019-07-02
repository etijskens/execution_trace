# -*- coding: utf-8 -*-

"""
Package execution_trace
=======================================

A context manager for generating an start/stop messages around tasks.
"""
#===============================================================================
__version__ = "1.0.0"
#===============================================================================
import sys
from contextlib import contextmanager

#===============================================================================
def print2stderr(*args, **kwargs):
    """
    The standard print, but print to stderr instead of to stdout.
    """
    print(*args, file=sys.stderr, **kwargs)

#===============================================================================
@contextmanager
def trace(begin_msg='doing',end_msg='done.',log=None,singleline=True, combine=True):
    """
    Generate an execution trace by printing a message before and after
    a code fragment executes.
    
    :param str begin_msg: print this before body is executed
    :param str end_msg: print this after body is executed
    :param log: if None, generates the execution trace on stderr, otherwise on
        a logger object (from the logging module)
    :param singleline: generates a single line execution trace as in 
        `<begin_msg> ... <end_msg>`. Calling print2stderr may obfuscate this.
    :param combine: if True the after message recapitulates the begin message.
        This parameter is ignored when singleline is True.
    """
    if log:
        log.info(begin_msg+' ...')
        yield
        log.info(f"{begin_msg} {end_msg}")
    elif singleline:
        print2stderr(begin_msg,'... ', end='')
        yield
        print2stderr(end_msg)
    else:
        print2stderr(begin_msg,'...')
        yield
        if combine:
            print2stderr(begin_msg,end_msg,'\n')
        else:
            print2stderr(end_msg,'\n')
#===============================================================================

#===============================================================================
# use case
#===============================================================================
if __name__=="__main__":
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
        with trace('something',singleline=False,combine=False):
            # we must print to the same stream, otherwise the printed lines 
            # are not in the right order
            print2stderr('hello')
            print('world')
        with trace('something else'):
            # we must print to the same stream, otherwise the printed lines 
            # are not in the right order
            print2stderr('hello ...',end='')
#===============================================================================
