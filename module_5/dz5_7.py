CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
    
for c,l in zip(CYRILLIC_SYMBOLS,TRANSLATION):
        TRANS[ord(c)]=l
        TRANS[ord(c.upper())]=l.upper()    


def translate(name):
    # print(name)
    
    name=name.translate(TRANS)
    return name



print(TRANS)
print(translate("Дитрий Коробов"))  # Dmitrij Korobov
print(translate("Александр Иванович"))  # Aleksandr Ivanovich