"""Explanation scorer."""
import re


class Explanation:
    """
    Scorer for explanations.

    Decides whether a statement is an explanation or not.
    """

    def __init__(self, name):
        """Initialise the class."""
        self.weight = name

    def score(self, text):
        """
        Catch explanations.

        This is the actual engine, the scorer.
        """
        explanation = re.compile('.+but.+', re.IGNORECASE)
        if explanation.match(text):
            return 1 * self.weight
        else:
            return 0 * self.weight
