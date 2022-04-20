# jingle_bells = "Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh"

# jingle_bells_2 = "Jingle bells, jingle bells\fJingle all the way\fOh, what fun it is to ride\fIn a one horse open sleigh"

# jingle_bells_3 = "Jingle bells, jingle bells\tJingle all the way\tOh, what fun it is to ride\tIn a one horse open sleigh"

# jingle_bells_4 = "Jingle bells, jingle bells\vJingle all the way\vOh, what fun it is to ride\vIn a one horse open sleigh"

# jingle_bells_5 = "Jingle bells, jingle bells\rJingle all the way\rOh, what fun it is to ride\rIn a one horse open sleigh"

# one_line_text = "Textual data in Python is handled with str objects, or strings. "\
#                 "Strings are immutable sequences of Unicode code points. "\
#                 "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

# s = "I am learning strings in Python. Some new methods got now."
# sentences = s.split(". ")

# print(sentences[0]) # I am learning strings in Python
# print(sentences[1]) # Some new methods got now.
# print(sentences)

# sentences = ["I am learning strings in Python", "Some new methods got now."]
# text = ". ".join(sentences)
# print(text) # I am learning strings in Python. Some new methods got now.

# print('TestHook'.removeprefix('Test'))   # Hook
# print('TestHook'.removeprefix('Hook'))   # TestHook

# print('TestHook'.removesuffix('Hook'))   # Test
# print('TestHook'.removesuffix('Test'))   # TestHook

# print(jingle_bells)
# print(jingle_bells_2)
# print(jingle_bells_3)
# print(jingle_bells_4)
# print(jingle_bells_5)
# print(one_line_text)

# map = {ord('з'): 'z', ord('ю'): 'u'}
# translated = 'зю'.translate(map)
# print(translated) # zu

# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))