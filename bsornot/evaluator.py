"""Evaluator engine."""
import re


def evaluate(text, username):
    """Respond to query for a BS evaluation."""
    explanation = re.compile('.+but.+', re.IGNORECASE)
    if explanation.match(text):
        answer = " Explanation is usually BS"
    else:
        answer = " I don't know yet if this is BS or not."
    return '@{0}'.format(username) + answer
