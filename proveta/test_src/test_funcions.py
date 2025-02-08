import pytest

from src import funcions


def test_es_primo_numero_primo():
    assert funcions.es_primo(2) == True


def test_es_primo_numero_primo_No():
    assert funcions.es_primo(2) == False
