"""Salience scorer."""
import math
import sys

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six


class Salience:
    """
    Scorer for salience variance.

    The more distributed the importance of the entities, the higher the score.
    """

    def __init__(self, name):
        """Initialise the class."""
        self.weight = name

    def score(self, text):
        """
        Calculate the distribution of the salience of a sentence.

        Return value between 0 and 1.
        """
        saliences = self.entity_sentiment_text(text)
        N = len(saliences)
        variance = 0
        if N == 1:
            variance = 1
        else:
            for salience in saliences:
                variance += math.pow(salience - (1/N), 2)
            variance *= (1/(N - 1))
        return variance * self.weight

    def entity_sentiment_text(self, text):
        """Detect entity sentiment in the provided text."""
        client = language.LanguageServiceClient()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        document = types.Document(
            content=text.encode('utf-8'),
            type=enums.Document.Type.PLAIN_TEXT)

        """
        Detect and send native Python encoding to receive correct word offsets.
        """
        encoding = enums.EncodingType.UTF32
        if sys.maxunicode == 65535:
            encoding = enums.EncodingType.UTF16

        result = client.analyze_entity_sentiment(document, encoding)

        saliences = []

        for entity in result.entities:
            print('Mentions: ')
            print(u'Name: "{}"'.format(entity.name))
            for mention in entity.mentions:
                print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
                print(u'  Content : {}'.format(mention.text.content))
                print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
                print(u'  Sentiment : {}'.format(mention.sentiment.score))
                print(u'  Type : {}'.format(mention.type))
            print(u'Salience: {}'.format(entity.salience))
            print(u'Sentiment: {}\n'.format(entity.sentiment))
            saliences.append(entity.salience)
        return saliences
