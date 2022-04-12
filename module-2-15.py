result = 0
operand = None
operator = None
wait_for_number = True

while wait_for_number:
    # try:
        operand = float(input("Введите число: "))
        operator = input("Знак (+,-,*,/,=): ")
        print(operator)
        
        if operator == '=':
            print(result)
            wait_for_number=False
        if operator in ('+', '-', '*', '/'):
            if operator =='+':
               result+=operand
            if operator =='-':
               result-=operand
            if operator =='*':
               result*=operand
            if operator =='/':
               result/=operand
                #  print(result)
    # except:
        # print("Неверный знак операции!")
# print("q в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == 'q':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")

# result = None
# operand = None
# operator = None
# wait_for_number = True
# while True:
#     user_input = input(“>>> “)
#     if user_input == ‘=’:
#         break
#     if wait_for_number:
#         try:
#             operand = float(user_input)
#         except ValueError:
#             print(“Not a Number”)
#             continue
#         wait_for_number = False
#         if not result:
#             result = operand
#         if operator == “=”:
#             print(result)
#             break
#         else:
#             if operator == ‘+’:
#               result += operand
#             if operator == ‘-’:
#                   result -= operand
#             if operator == ‘*’:
#                   result *= operand
#             if operator == ‘/’:
#                 try:
#                   result /= operand
#                 except ZeroDivisionError:
#                     print(“Ділення на 0”)
#                     continue
#     else:
#         if user_input in (‘+’, ‘-’, ‘*’, ‘/’):
#             operator = user_input
#         else:
#             operator = None
#         if not operator:
#             print(“Not operator”)
#         else:
#              wait_for_number = True