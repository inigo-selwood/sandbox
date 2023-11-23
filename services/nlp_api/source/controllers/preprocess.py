import string
import re

import nltk


def preprocess(text: str) -> list[str]:
    """Preprocess a block of text

    Arguments
    ---------
    text: str
        the text to process

    Returns
    -------
    text: list[str]
        the preprocessed text, split into tokens

    To do
    -----
    - Remove URLs
    - Handle contractions
    - Remove emojis and special characters
    - Remove rare words
    - Perform spell checking
    - Handle negations
    """

    # Make lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove non alphanumeric/space characters, and consolidate whitespace
    text = re.sub(r"[^a-zA-Z0-9 ]+", " ", text)
    text = re.sub(r"[ \n\r\t\v]+", " ", text)

    # Tokenize
    words = nltk.word_tokenize(text)

    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words("english")
    words = [word for word in words if word not in stopwords]

    # Lemmatize
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tag_parts = {
        "J": nltk.corpus.wordnet.ADJ,
        "V": nltk.corpus.wordnet.VERB,
        "N": nltk.corpus.wordnet.NOUN,
        "R": nltk.corpus.wordnet.ADV,
    }
    tagged_words = nltk.pos_tag(words)

    temporary = []
    for word, tag in tagged_words:
        part = tag_parts.get(tag[0], nltk.corpus.wordnet.NOUN)
        lemma = lemmatizer.lemmatize(word, part)
        temporary.append(lemma)
    words = temporary

    # Return result
    return words
