"""Provides some utilities widely used by other modules"""

import random

username = 'demo';

# ______________________________________________________________________________
# Colors available to color the map
class Color(object):
    """docstring for Color"""
    def __init__(self, name, colorCode):
        super(Color, self).__init__()
        self.name = name
        self.colorCode = colorCode

availableColors = {};
availableColors['R'] = Color('Red', '#d50000');
availableColors['G'] = Color('Green', '#1b5e20');
availableColors['Y'] = Color('Yellow', '#ffff00');
availableColors['O'] = Color('Orange', '#e65100');
availableColors['B'] = Color('Brown', '#795548');
availableColors['T'] = Color('Teal', '#009688');
availableColors['P'] = Color('Purple', '#4a148c');

# ______________________________________________________________________________
# Algorithms available to color the map
availableAlgorithms = [];
availableAlgorithms.append('Simple Backtracking');
availableAlgorithms.append('Backtracking with Forward Checking');
availableAlgorithms.append('Backtracking with MAC');
availableAlgorithms.append('Min Conflicts');

# ______________________________________________________________________________
# Functions on Sequences and Iterables


def count(seq):
    """Count the number of items in sequence that are interpreted as true."""
    return sum(bool(x) for x in seq)

def first(iterable, default=None):
    """Return the first element of an iterable or the next element of a generator; or default."""
    try:
        return iterable[0]
    except IndexError:
        return default
    except TypeError:
        return next(iterable, default)

# ______________________________________________________________________________
# argmin and argmax


identity = lambda x: x

argmin = min
argmax = max

def argmin_random_tie(seq, key=identity):
    """Return a minimum element of seq; break ties at random."""
    return argmin(shuffled(seq), key=key)

def shuffled(iterable):
    """Randomly shuffle a copy of iterable."""
    items = list(iterable)
    random.shuffle(items)
    return items
