import pytest

from source import controllers


def test_lowercase():
    result = controllers.preprocess("Hello World")
    assert result == ["hello", "world"]


def test_remove_punctuation():
    result = controllers.preprocess("Hello, World!")
    assert result == ["hello", "world"]


def test_remove_numbers():
    result = controllers.preprocess("Hello 123 World")
    assert result == ["hello", "world"]


def test_remove_non_alphanumeric():
    result = controllers.preprocess("Hello @World!")
    assert result == ["hello", "world"]


def test_tokenize():
    result = controllers.preprocess("Hello World")
    assert result == ["hello", "world"]


def test_remove_stopwords():
    result = controllers.preprocess("This is a test sentence")
    assert result == ["test", "sentence"]


def test_lemmatization():
    result = controllers.preprocess("running walks cats dogs")
    assert result == ["run", "walk", "cat", "dog"]
