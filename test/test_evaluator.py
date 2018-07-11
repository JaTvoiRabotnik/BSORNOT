"""Test class for Evaluators."""
import unittest
from bsornot.explanationscore import Explanation
from bsornot.lengthscore import Length
import csv


class TestMetrics(unittest.TestCase):
    """
    Testing the metrics.

    There are 4 initial metrics:
    - Explanations
    - Information value
    - Ambiguity
    - Plural use
    - Bad grammar
    """

    def setup(self):
        """Setting up for all tests in this class."""


class TestExplanationsPositive(TestMetrics):
    """Testing explanations that ARE bullshit."""

    def runTest(self):
        """Testing explanations - definitely BS."""
        explanation = Explanation(1)  # set weight to 1
        with open('data/explanations_positive.csv', newline='') as csvfile:
            excusesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in excusesreader:
                label = float(row[1])
                result = explanation.score(row[0])
                # a result greater than 0.8 indicates BS.
                message = '{0} < {1} - {2}'.format(result, label, row[0])
                self.assertTrue(result >= label, message)


class TestExplanationsNegative(TestMetrics):
    """Testing explanations that ARE NOT bullshit."""

    def runTest(self):
        """Testing explanations - not sure whether BS or Not."""
        explanation = Explanation(1)  # set weight to 1
        with open('data/explanations_negative.csv', newline='') as csvfile:
            excusesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in excusesreader:
                label = float(row[1])
                result = explanation.score(row[0])
                # a result smaller than 0.8 indicates uncertainty.
                message = '{0} > {1} - {2}'.format(result, label, row[0])
                self.assertTrue(result <= label, message)


class TestLengthPositive(TestMetrics):
    """Testing long sentences."""

    def runTest(self):
        """Testing long sentences."""
        length = Length(1)  # set weight to 1
        with open('data/length_positive.csv', newline='') as csvfile:
            lengthreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in lengthreader:
                label = float(row[1])
                result = length.score(row[0])
                # a result greater than 0.8 indicates BS.
                message = '{0} < {1} - {2}'.format(result, label, row[0])
                self.assertTrue(result >= label, message)


class TestLengthNegative(TestMetrics):
    """Testing short sentences."""

    def runTest(self):
        """Testing short sentences."""
        length = Length(1)  # set weight to 1
        with open('data/length_negative.csv', newline='') as csvfile:
            lengthreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in lengthreader:
                label = float(row[1])
                result = length.score(row[0])
                # a result smaller than 0.8 indicates uncertainty.
                message = '{0} > {1} - {2}'.format(result, label, row[0])
                self.assertTrue(result <= label, message)

    '''
    def test_2(self):
        self.assertTrue(True)

    def test_3(self):
        self.assertEqual(self.func.state, 0)

    def test_4(self):
        self.func.increment_state()
        self.assertEqual(self.func.state, 1)

    def test_5(self):
        self.func.increment_state()
        self.func.increment_state()
        self.func.clear_state()
        self.assertEqual(self.func.state, 0)
    '''
