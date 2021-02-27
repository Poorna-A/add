def add(a,b):
    c=a+b
    print(c)

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


a=int(input("enter two numbers"))
b=int(input("enter a num"))


add(a,b)
result=sub(a,b)
print(result)
mulresult=mul(a,b)
print(mulresult)
divresult=div(a,b)
print(divresult)