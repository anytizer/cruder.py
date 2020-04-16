#!/bin/python
# Capitalize frequent words

import requests


caches = []


def _cached_words() -> []:
    csv_url = "https://raw.githubusercontent.com/anytizer/capitalizer.php/master/src/anytizer/words.csv"
    csv = requests.get(csv_url)
    words = csv.text.splitlines()
    return words


def _capitalize(w=""):
    capitalized = w.title()
    for entity in caches:
        if w.upper() == entity:
            capitalized = entity
    return capitalized


def capitalize(word=""):
    capitalized = " ".join([_capitalize(w) for w in word.split("_")])
    return capitalized
                           

caches = _cached_words()
if __name__ == "__main__":
    c = capitalize('id')
    d = capitalize('country')
    e = capitalize('country_id')
    assert c == "ID", "Not capitalized properly"
    assert d == "Country", "Wrongly capitalized"
    assert e == "Country ID", "Splitting not managed"

    print(c, d, e, sep=" | ")
