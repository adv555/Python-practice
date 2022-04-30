import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, '*' * len(word), text, flags=re.IGNORECASE)
    return text


print(replace_spam_words("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", ["Python", "ABC", "Guido"]))
    
 