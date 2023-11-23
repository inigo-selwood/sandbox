import nltk

from .preprocess import preprocess


# Download NLTK dependencies
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")


__all__ = ["preprocess"]
