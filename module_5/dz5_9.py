


def formatted_numbers():
    list=[]
    list.append("|{:^10}|{:^10}|{:^10}|".format('decimal','hex','binary'))

    for i in range(0,16):
         list.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i))
   
    # for i in range(1,16):
    #     list.append("{:<10}|{:^10}|{:>10}".format(i,hex(i),bin(i)))

    return list
    


for el in formatted_numbers():
    print(el)