"""Evaluator engine."""
import csv
from flask import jsonify
from bsornot.explanationscore import Explanation
from bsornot.lengthscore import Length
from bsornot.saliencescore import Salience


class Evaluator:
    """
    Evaluator class for calculating scores.

    Initialises dictionaries and evaluates scores of BS.
    """

    def __init__(self):
        """Initialize the dictionary of weights and scoring classes."""
        w = {}
        with open('data/weights.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                w[row[0]] = row[1]
                print(row[0] + ", " + row[1])
        self.explanation = Explanation(w['explanation'])
        self.length = Length(w['length'])
        self.salience = Salience(w['salience'])

    def isBS(self, text):
        """Return a score for BS."""
        total = 0
        scores = []
        scores.append(self.explanation.score(text))
        scores.append(self.length.score(text))
        scores.append(self.salience.score(text))
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

    def parse_scoring(self, text, username):
        """Respond to a query with breakdown of scores."""
        total = 0
        scores = []
        scores.append(self.explanation.score(text))
        scores.append(self.length.score(text))
        scores.append(self.salience.score(text))
        for score in scores:
            total += score
        header = '@{0} '.format(username)
        response = "Explanation = {0}, Length = {1}, Salience variance = {2}. Total: {3}".format(scores[0], scores[1], scores[2], total)
        return header + response

    def analyse(self, text):
        """Respond to a query with breakdown of scores."""
        total = 0
        scores = []
        scores.append(self.explanation.score(text))
        scores.append(self.length.score(text))
        scores.append(self.salience.score(text))
        for score in scores:
            total += score
        response = {'explanation': '{0}'.format(scores[0]),
                    'length': '{0}'.format(scores[1]),
                    'salience_variance': '{0}'.format(scores[2]),
                    'total': '{0}'.format(total)}
        return jsonify(response)
