list =["    +38(050)123-32-34","     0503451234","(050)8889900","38050-111-22-22","38050 111 22 11   ",]
def sanitize_phone_number(phone):
    phone_number=phone.strip().replace(" ","").replace("-","").replace("(","").replace(")","").replace("+","")


for i in list:
    print(sanitize_phone_number(i))
