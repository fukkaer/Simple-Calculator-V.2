#Simple calculator V. 2.1
#Simple exception handling prints errors
import math
def sum(x,y):
	result = x + y
	return result
def sub(x,y):
	result = x - y
	return result
def mult(x,y):
	result = x * y
	return result
def div(x,y):
	result = x / y
	return result
def sineresult(x,y):
    sine = math.sin(x/y)
    print(sine,'\n\n')
def cosineresult(x,y):
    cosine = math.cos(x/y)
    print(cosine,'\n\n')
def totalresult():
    print('the result is:', end=' ')
def Exception_Error():
    print("ERROR INPUT NOT A NUMBER")
def startuptext():
    print("Calculator V.2.1\n\nStill uses only 2 numbers Max\n")
def looptext():
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos (number1/number2)")
    print("(7)change both numbers\n(8)change second number\n(9)Quit\ncurrent numbers:",num1, num2)
loopback = True
startuptext()
while loopback == True:
    try:
        num1 = int(input("give the first number: "))
        loop_2 = True
        while loop_2 == True:
            try:
                num2 = int(input("give the second number: "))
                loop = True
                while loop == True:
                    looptext()
                    try:
                        z = int(input("please select something: "))
                        if z == 1:
                            totalresult()
                            print(sum(num1,num2),'\n\n')
                        elif z == 2:
                            totalresult()
                            print(sub(num1,num2),'\n\n')
                        elif z == 3:
                            totalresult()
                            print(mult(num1,num2),'\n\n')
                        elif z == 4:
                            totalresult()
                            print(div(num1,num2),'\n\n')
                        elif z == 5:
                            totalresult()
                            sineresult(num1,num2)
                        elif z == 6:
                            totalresult()
                            cosineresult(num1,num2)
                        elif z == 7:
                            loop = False
                            loop_2 = False
                        elif z == 8:
                            loop = False
                        elif z == 9:
                            loopback = False
                            loop_2 = False
                            break
                        elif z != 1 or z != 2 or z != 3 or z != 4 or z != 5 or z != 6 or z != 7 or z != 8 or z != 9:
                            print('ERROR INVALID INPUT\nINPUT MUST BE IN RANGE (1-9)')
                    except Exception as c:
                        print(c)
            except Exception as b:
                print(b)
    except Exception as a:
        print(a)
else:
    print("thank you\n\n")
    input("press ENTER to exit")
