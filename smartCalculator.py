import mylib


mylib.greet()

while True:
    text = input('Enter some text :')
    lst = text.split(' ')
    for i in lst:
        if i.upper() in mylib.operations.keys():
            try :
                data = mylib.extract_data(lst)
                res = mylib.operations[i.upper()](data[0],data[1])
                print(res)
            except :
                print("Something went wrong,Please retry")
            finally:
                break
        elif i.upper() in mylib.commands.keys():
            mylib.commands[i.upper()]()
            break
    else:
        mylib.sorry()
            
    
