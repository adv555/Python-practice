#  2 write a function that takes a string and a length and returns a string that is length characters long, padded with spaces = length - len(string)) // 2 on the left

def format_string(string, length):
    if len(string)>=length:
      return string
    else:
        return " "*((length - len(string)) // 2) + string
        


print(format_string("aaaaannnnb", 5))
print(format_string(string='aaaaannnnb', length=15))

