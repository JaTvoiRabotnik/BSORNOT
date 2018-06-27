import unittest
import bsornot.evaluator as evaluator


class TestMetrics(unittest.TestCase):
    def test_explanation(self):
        excuse1 = "I like you, but I am just not ready for a relationship"
        expected1 = "@user Explanation is usually BS"
        result1 = evaluator.evaluate(excuse1, "user")
        self.assertEqual(result1, expected1)

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
