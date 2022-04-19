
password='123G5a78'

def is_valid_password(password):
    if len(password) != 8:
        return False
    if not any(symbol.isdigit() for symbol in password):
        return False
    if not any(symbol.isupper() for symbol in password):
        return False
    if not any(symbol.islower() for symbol in password):
        return False
    return True


print(is_valid_password(password))