import os
import sys
import jetpack.parsers

def test_io_keqv_txt(get_file):
    fname = get_file('parsers_parameters.txt')
    data = jetpack.parsers.parse_keqv_txt(fname)
    print(data)
    assert set(['t_degree', 'p_pascal', 'rh_percent']) == set(data.keys())
