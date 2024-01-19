from textblob import TextBlob
from textstat import textstat


class AnalysisModel:
    """ Model for counting words in text """

    def get_word_count(self, text):
        words = text.split()
        return len(words)

    def analyze_sentiment(self, text):
        analysis = TextBlob(text).sentiment
        return analysis

    def readability_analysis(self, text):
        metrics = {
            'flesch_reading_ease': textstat.flesch_reading_ease(text),
            'gunning_fog': textstat.gunning_fog(text),
            'spache_readability': textstat.spache_readability(text),
            'Average Sentence Length': textstat.avg_sentence_length(text),
            'Average Syllables per Word': textstat.avg_syllables_per_word(text),
            'Long Word Count': textstat.long_word_count(text),
            'Sentences': textstat.sentence_count(text),
            'Word per Sentence': textstat.words_per_sentence(text),
            'Syllables': textstat.syllable_count(text)

        }
        return metrics


