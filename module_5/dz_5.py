test='Alex\nKdfe23\t\f\v.\r'
test_2='Al\nKdfe23\t\v.\r'


def real_len(text):
    string=text
          
    for i in string:
        if i=='\n':
            string=string.replace('\n','')
        if i=='\t':
            string=string.replace('\t','')
        if i=='\f':
            string=string.replace('\f','')
        if i=='\v':
            string=string.replace('\v','')
        if i=='\r':
            string=string.replace('\r','')
      
    return len(text)
   
    
    


print(real_len(test))
# print(real_len(test_2))