import nltk

from .preprocess import preprocess


# Download NLTK dependencies
packages = [
    "averaged_perceptron_tagger",
    "punkt",
    "stopwords",
    "wordnet",
]
for package in packages:
    nltk.download(package)


__all__ = ["preprocess"]
