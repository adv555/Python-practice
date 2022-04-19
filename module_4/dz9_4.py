pin_codes=['1101', '9034', '0A11']


def is_valid_pin_codes(pin_codes):
    
    for pin in pin_codes:
        
        if type (pin) != str:
            return False
        if len(pin) != 4:
            return False
        for i in pin:
            if i not in '0123456789':
                return False
        
        
      


print(is_valid_pin_codes(pin_codes))

