"""Test class for Evaluators."""
import unittest
import bsornot.evaluator as evaluator


class TestMetrics(unittest.TestCase):
    """
    Testing the metrics.

    There are 4 initial metrics:
    - Explanations
    - Ambiguity
    - Plural use
    - Bad grammar
    """

    def test_explanation(self):
        """Testing explanations."""
        # positive cases
        excuses = []
        excuses.add("I like you, but I am just not ready for a relationship")
        excuses.add("I'm not a racist, but I think black people get too many \
                   advantages")
        excuses.add("I'm sorry, but I am very busy with my career.")
        for excuse in excuses:
            result = evaluator.evaluate(excuse, "user")
            # a result greater than 0.8 indicates BS.
            self.assertTrue(result >= 0.8)

        # negative cases
        valids = []
        valids.add("I am kind, but also very demanding.")
        for valid in valids:
            result = evaluator.evaluate(valid, "user")
            # a result less than 0.8 indicates uncertainty.
            self.assertTrue(result < 0.8)

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
