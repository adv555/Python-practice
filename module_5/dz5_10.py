import re


def find_word(text, word):
    if text == '' or word == '' or text.find(word) == -1:
        result=False
        first_index=None
        last_index=None
        
    else:
        s_result =re.search(word,text)
        first_index=s_result.span()[0]
        last_index=s_result.span()[1]
        result=True
 
    
    dict={'result': result,'first_index': first_index,'last_index': last_index,'search_string': word,'string':text}

    
    return dict


print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))


# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }

# {
#     'result': False,
#     'first_index': None,
#     'last_index': None,
#     'search_string': 'python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }