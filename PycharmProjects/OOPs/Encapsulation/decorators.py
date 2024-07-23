# 1. Python program to illustrate functions
# can be treated as objects
'''def shout(text):
    return text.upper()

print(shout("hello"))
yell = shout # created an object
print(yell("hello"))'''

# 2. Python program to illustrate functions
# can be passed as arguments to other functions
'''def shout(text): # string comes into function(3)
    return text.upper() # returns in uppercase(4)
def greet(fun): # greet calls fun(shout) function(2)
    greeting = fun("hi, I am created by a function passed as an argument.")
    print(greeting) # returned string displayed(5)
    
greet(shout) # greet calls greet definition (1)'''


# 3. Python program to illustrate functions
# can return another function

'''def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(20))'''



'''def hello_decorator(func):
    def inner1():
        print("hello,this is before function exection")
        func()
        print("This is after function exection")
    return inner1


def function_to_be_used():
    print("This is inside the function !!")
    
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()'''


