#-*- coding: utf-8 -*-

from codebuildpy import culc


def test_codebuildpy_culc_add():
    """
    """
    assert culc.add(5, 5) == 10

def test_codebuildpy_culc_false():
    """
    """
    assert culc.add(5, 5) == 11
