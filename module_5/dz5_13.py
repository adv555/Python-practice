import re

list = ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org',
        'first.middle.last@iana.or', 'abc111@test.com']





def find_all_emails(text):
    for email in list:
       text = re.findall(r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", email)
    return text

print(find_all_emails(list))