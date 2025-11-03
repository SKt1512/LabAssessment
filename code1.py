#abc= input("Enter the string : ")
abc =" This is a test string and editting it"
length =len(abc)
last_char = abc[-3:]
if length >=3 :
    if last_char.lower() =='ing':
        new_str = abc+"ly"
        print(new_str)
    else:
        new_str = abc+"ing"
        print(new_str)
else:
    print("String length is short") 
