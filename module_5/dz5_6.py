import re;

def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        word =word.lower()
        text=text.lower()
        if space_around==True:
            print("space_around=True")
            if word in text:
                if re.search(r'\b' + word + r'\b', text) or re.search(r'\b' + word + r'/.', text):
                    return True
            return False


        if space_around==False:
            print("space_around=False")
            if word in text:     
                return True
            return False
    

    
       

print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["мох"], True))  # False
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True

# print(is_spam_words("Молох", ["лх"]))  # False
# print(is_spam_words("Молох", ["лох"],True))  # False
# print(is_spam_words("Молох мох", ["мох"], True))  # True
# print(is_spam_words("Молох", ["Лох"]))  # True