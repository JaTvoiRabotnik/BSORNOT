"""Test class for Evaluators."""
import unittest
import bsornot.evaluator as evaluator
import csv


class TestMetrics(unittest.TestCase):
    """
    Testing the metrics.

    There are 4 initial metrics:
    - Explanations
    - Ambiguity
    - Plural use
    - Bad grammar
    """

    def test_BS_explanation(self):
        """Testing explanations - definitely BS."""
        with open('data/test_cases_positive.csv', newline='') as csvfile:
            excusesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in excusesreader:
                label = float(row[1])
                result = evaluator.evaluate(row[0])
                # a result greater than 0.8 indicates BS.
                errorMessage = '{0} is less than {1} - {2}'.format(result, label, row[0])
                self.assertTrue(result >= label, errorMessage)

    def test_Non_BS_explanation(self):
        """Testing explanations - not sure whether BS or Not."""
        with open('data/test_cases_negative.csv', newline='') as csvfile:
            excusesreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in excusesreader:
                label = float(row[1])
                result = evaluator.evaluate(row[0])
                # a result smaller than 0.8 indicates uncertainty.
                errorMessage = '{0} is greater than {1} - {2}'.format(result, label, row[0])
                self.assertTrue(result <= label, errorMessage)

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


if __name__ == '__main__':
    unittest.main()
