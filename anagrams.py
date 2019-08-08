#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
__author__ = "Eileen with instructor help"

import sys
import cProfile
import re
import pstats
import functools
from collections import defaultdict

def profile_decor(func):
    @functools.wraps(func)
    # create object, enable, disable
    def inner(*args, **kwargs):
        profiler = cProfile.Profile() 
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        ps = pstats.Stats(profiler).strip_dirs().sort_stats('cumulative')
        ps.print_stats(10)
        return result 
    return inner

def alphabetize(string):
    """ alphabetize
        Given a string, return a string that includes the same letters in
        alphabetical order.

        Example:

        >>> print alphabetize('cab')
        abc

    """
    return "".join(sorted(string.lower()))

# @profile_decor
def find_anagrams(words):
    """ find_anagrams

        Return a dictionary with keys that are alphabetized words and values
        that are all words that, when alphabetized, match the key.

        Example:

        >>> print find_anagrams(['cat', 'dog', 'act'])
        {'dgo': ['dog'], 'act': ['cat', 'act']}

    """
    anagrams = defaultdict(list)
    
    for w in words:
        anagrams[alphabetize(w)].append(w)
    return anagrams
        
if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read()
            words = words.splitlines()
            d = find_anagrams(words)
            # for k, v in d.items():
            #     print(f'{k} : {v}')
