import datetime

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def mod(x,y):
    return x%y

def divide(x,y):
    return x/y

def gcd(x,y):
    while y:
        x = x%y
        x,y = y,x
    return x

def lcm(x,y):
    return (x*y)/gcd(x,y)

def min(x,y):
    return(x if x<y else y)

def max(x,y):
    return(x if x>y else y)


    

def print_name(name="Munna"):
    print("My name is ",name)

def greet():
    print("Welcome,dear user")
    print_name()
    print()


def sorry():
    print("\nSorry,I can't do this for you.It is beyond my ability\n")


def helpPLz():
    print("\nHeyy user, you can perform all these operations\n")
    for i in operations:
        print(i)
    for i in commands:
        print(i)

def end():
    print("Thanks \nPress enter to exit")
    exit()

def tym():
    ob = datetime.datetime.now().time()
    hrs = ob.hour
    x = ""
    if(hrs>0 and hrs<12):
        x = "am"
    else:
        x = "pm"
    print(f"It's {hrs} : {ob.minute} {x}")

def getDate():
    dt = datetime.datetime.now().date()
    print(f"It's {dt.day} {mnth[dt.month]} {dt.year}")

def extract_data(lst):
    mylist = []
    for i in lst:
        try:
            x = float(i)
            mylist.append(x)
        except:
            pass
    return mylist
    
operations = {
               "ADD" : add,"PLUS" : add,"ADDITION" : add,"SUM" : add,
               "SUBTRACT" : sub,"MINUS" : sub,"DIFFERENCE" : sub,
               "MULTIPLY" : multiply,"PRODUCT" : multiply,
               "GREATER" : max,"LARGER" : max,"MAX" : max,"BIG" : max,
               "MAXIMUM" : max,"SMALLER" : min,"MIN" : min,
               "MINIMUM" : min,
               "DIVIDE" : divide,"LCM" : lcm,"GCD" : gcd,"HCF" : gcd,
               "MODULUS" : mod,"MOD" : mod,"REMAINDER" : mod,
                "+" : add,"-" : sub,"/" : divide,"*" : multiply,"%" : mod,">" : max,
                "<"  : min
             }

mnth = { 1:'january' , 2:'feburary' , 3:'march', 4:'april',5:'may' , 6:'june' , 7:'july' , 8:'august' , 9:'september',10:'october',11:'november',12:'decmber'}

               
commands = {
                "NAME" : print_name,
		"END" : end,"EXIT" : end,
		"TERMINATE" : end,
		"TIME" : tym,
		"DATE" : getDate,
                "CLOSE" : end,"HELP" : helpPLz
            }

