import unicodedata


def remove_accents(word):
    return "".join(
        (
            c
            for c in unicodedata.normalize("NFD", word)
            if unicodedata.category(c) != "Mn"
        )
    )


def clean_word(word):
    return remove_accents(word).lower()
