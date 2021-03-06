#/usr/bin/env python

# Matthieu Brucher
# Last Change : 2007-08-22 18:20

from __future__ import absolute_import

import unittest
import numpy

from PyDSTool.Toolbox.optimizers.criterion import OrComposition, AndComposition


class TrueCriterion(object):
  def __call__(self, state, **kwargs):
    return True

class FalseCriterion(object):
  def __call__(self, state, **kwargs):
    return False

class test_OrCriterion(unittest.TestCase):
  def test_true(self):
    criterion = OrComposition(TrueCriterion(), FalseCriterion())
    state = {}
    assert(criterion(state))

  def test_true2(self):
    criterion = OrComposition(TrueCriterion(), TrueCriterion())
    state = {}
    assert(criterion(state))

  def test_false(self):
    criterion = OrComposition(FalseCriterion(), FalseCriterion())
    state = {}
    assert(not criterion(state))

class test_AndCriterion(unittest.TestCase):
  def test_true(self):
    criterion = AndComposition(TrueCriterion(), TrueCriterion())
    state = {}
    assert(criterion(state))

  def test_false(self):
    criterion = AndComposition(FalseCriterion(), TrueCriterion())
    state = {}
    assert(not criterion(state))

if __name__ == "__main__":
  unittest.main()
