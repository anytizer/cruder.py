#!/bin/python
# Capitalize frequent words

import requests


def _cache_csv_in_words() -> []:
    csv_url = "https://raw.githubusercontent.com/anytizer/capitalizer.php/master/src/anytizer/words.csv"
    csv = requests.get(csv_url)
    internet = csv.text.splitlines()
    return internet


def capitalize(word=""):
    capitalized = word

    for entity in caches:
        if word.upper() == entity:
            capitalized = entity
            break
    return capitalized


caches = _cache_csv_in_words()
if __name__ == "__main__":
    c = capitalize('id')
    d = capitalize('country')
    assert c == "ID", "Not capitalized properly"
    assert d == "country", "Wrongly capitalized"
