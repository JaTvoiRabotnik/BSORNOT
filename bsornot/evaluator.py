"""Evaluator engine."""
import re


def evaluate(text):
    """Return a score for BS."""
    explanation = re.compile('.+but.+', re.IGNORECASE)
    if explanation.match(text):
        return float(0.9)
    else:
        return float(0.7)


def parse_evaluation(text, username):
    """Respond to query for a BS evaluation."""
    score = evaluate(text)
    response = '@{0}'.format(username)
    if score >= 0.8:
        return response + " Explanation is usually BS"
    else:
        return response + " I don't know yet if this is BS or not."
