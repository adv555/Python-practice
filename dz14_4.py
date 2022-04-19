import sys


def parse_args():
    result = ""
   
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result = result + arg + " "
        

    return result[:-1]

print(parse_args())