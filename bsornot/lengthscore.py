"""Sentence length scorer."""
import math


class Length:
    """
    Scorer for sentence length.

    The longer the sentence, the higher the score.
    """

    def __init__(self, weight):
        """Initialise the class."""
        self.weight = weight

    def score(self, text):
        """Count the length of a sentence. Return value between 0 and 1."""
        length = len(text)
        # scaled logistic function
        normalised = (2 / (1 + math.exp(-(1/75)*length))) - 1
        return normalised * float(self.weight)
