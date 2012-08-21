"""
parsers.py

File parsing functions for input parameter files
"""
import re
import os
import sys
import json
import yaml


def _transform(s):
    """Convert input to a numerical type if possible.
    
    Parameters
    ----------
    s : str
        Input variable

    Returns
    -------
    A non-string object is returned as it is. A string object is converted to 
    int, float, str in that order
    """
    if not type(s) is str:
        return s
    for converter in int, float, str:   # try them in increasing order of lenience
        try:
            return converter(s)
        except ValueError:
            pass
    raise ValueError("Failed to autoconvert {0!r}".format(s))


def parse_keqv_txt(filename):
    """Parse a parameter file with `key = value` format

    Parameters
    ----------
    filename : str
        File name including the path
    
    Returns
    -------
    data : dict
        Parameters returned as a dictionary
    """
    COMMENT = re.compile(r"""\s*\#\s*(?P<value>.*)""")  
    PARAMETER = re.compile(r"""\s*(?P<parameter>[^=]+?)\s*=\s*(?P<value>[^\#]*)(?P<comment>\s*\#.*)?""", re.VERBOSE)
           
    data = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            m = COMMENT.match(line)
            if m:
                continue
            # parameter
            m = PARAMETER.match(line)
            if m:
                # check for comments after parameter?? -- currently discarded
                parameter = m.group('parameter')
                value = _transform(m.group('value'))
                data[parameter] = value
            else:
                errmsg = '{filename!r}: unknown line in parameter file, {line:r}'.format(vars())
                raise IOError(errmsg)
        return data


def parse_json(filename):
    """Parse a parameter file in JSON format

    Parameters
    ----------
    filename : str
        File name including the path for json file
    
    Returns
    -------
    data : dict
        Parameters returned as a dictionary
    """
    with open(filename) as f:
        try:
            data = json.load(f, )
        except Exception:
            raise

    return data


def parse_yaml(filename):
    """Parse a parameter file in YAML format

    Parameters
    ----------
    filename : str
        File name including the path for json file
    
    Returns
    -------
    data : dict
        Parameters returned as a dictionary
    """
    with open(filename) as f:
        try:
            data = yaml.load(f, Loader=yaml.FullLoader)
        except Exception:
            raise
        
    return data

        