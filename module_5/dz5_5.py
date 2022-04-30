list =["    +38(050)123-32-34","     0503451234","(050)8889900","38050-111-22-22","38050 111 22 11   ","    +81123-32-34",]

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    ...
    


print(get_phone_numbers_for_countries(list))
