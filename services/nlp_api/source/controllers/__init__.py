import nltk

from .preprocess import preprocess


# Download NLTK dependencies
nltk.download("punkt")


__all__ = ["preprocess"]
