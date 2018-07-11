"""Evaluator engine."""
import csv
from bsornot.explanationscore import Explanation
from bsornot.lengthscore import Length


class Evaluator:
    """
    Evaluator class for calculating scores.

    Initialises dictionaries and evaluates scores of BS.
    """

    def __init__(self, name):
        """Initialize the dictionary of weights."""
        w = {}
        with open('data/weights.csv', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            w = {rows[0]: rows[1] for rows in reader}
        self.explanation = Explanation(w['explanation'])
        self.explanation = Length(w['length'])

    def isBS(self, text):
        """Return a score for BS."""
        total = 0
        scores = []
        scores.append(self.explanation.score(text))
        for score in scores:
            total += score
        """Threshold for BS is 80%"""
        if total >= 0.8:
            return True
        else:
            return False

    def parse_evaluation(self, text, username):
        """Respond to query for a BS evaluation."""
        response = '@{0} '.format(username)
        if self.isBS(text):
            return response + "Explanation is usually BS"
        else:
            return response + "I don't know yet if this is BS or not."
