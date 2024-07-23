
# *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
'''def myFun(*argv):
    for arg in argv:
        print(arg)
myFun("sai","sagar","hello","welcome","sorry")'''


# Python program to illustrate *args with a first extra argument
'''def myFun(arg1, *argv):
    print("First argument: ",arg1)
    for arg in argv:
        print("Second argumant: ",arg)

myFun(10,20,30,40,50,)'''


# **kwargs take keys and values.....
'''def myFun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

myFun(first = 'sai',mid = "for", last = "sagar")'''


# passed a normal argument alongside kwargs...
'''def myFun(arg1, **kwargs):
    for key,value in kwargs.items():
        print("%s = %s"%(key,value))

myFun("hi",first = "Geeks",mid = "For",last = "Geeks")'''


'''def myFun(arg1, arg2,arg3):
    print("arg1: ",arg1)
    print("arg2: ",arg2)
    print("arg3: ",arg3)

args = ("geeks", "for", "geeks")
myFun(*args)

kwargs = {"arg1": "geeks","arg2": "for","arg3": "geeks"}
myFun(**kwargs)'''


# there are still remaining to practice.......


