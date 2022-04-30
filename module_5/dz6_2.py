articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    """
    Функция поиска статей по заданному ключу.
    Возвращает список статей, которые содержат заданный ключ.
    Если ключ не найден, то возвращает None.
    :param key: ключ для поиска
    :param letter_case: нужно ли учитывать регистр букв
    :return: список статей, которые содержат заданный ключ
    """
    # if letter_case:
    #     return [article for article in articles_dict if key in article.values()]
    # else:
    #     return [article for article in articles_dict if key.lower() in article.values()]
    new_dict = []
    if letter_case:
        for article in articles_dict:  
            for val in article.values():
                if type(val) == str and val.find(key) != -1:
                    # print(val, article)
                    new_dict.append(article)
                
        print("требуется строгое соответствие")
                   
            
    else:
        for article in articles_dict:  
            for val in article.values():
                if type(val) == str and val.lower().find(key.lower()) != -1:
                    # print(val, article)
                    new_dict.append(article)
    return new_dict


print(find_articles("Love", True))
