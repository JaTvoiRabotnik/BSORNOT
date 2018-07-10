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
        excuse1 = "I like you, but I am just not ready for a relationship"
        excuse2 = "I'm not a racist, but I think black people get too many \
                   advantages"
        excuse3 = "I'm sorry, but I am very busy with my career."
        expected_OK = "@user Explanation is usually BS"
        result1 = evaluator.evaluate(excuse1, "user")
        self.assertEqual(result1, expected_OK)
        result2 = evaluator.evaluate(excuse2, "user")
        self.assertEqual(result2, expected_OK)
        result3 = evaluator.evaluate(excuse3, "user")
        self.assertEqual(result3, expected_OK)

        # negative cases
        valid1 = "I am kind, but also very demanding."
        expected_NOK = "@user I don't know yet if this is BS or not."
        result1 = evaluator.evaluate(valid1, "user")
        self.assertEqual(result1, expected_NOK)

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
