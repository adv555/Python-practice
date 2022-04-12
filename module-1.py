first = int(input("print your number: "))
second = int(input("print your number: "))


if first % 2:
    print(first % 2)
    
    print(f"this number {first} is odd")
    
else:
    print(first % 2)
    
    print(f"this number {first} is even")

num = int(input("print your number: "))
print(num)
length = len(str(num))

if length == 2 and num % 2 ==0:
    print(f"this number {length} and {num} ")