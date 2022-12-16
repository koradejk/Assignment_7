def Factorial(x):
    if x==1:
        return 1
    else:
        return(x*Factorial(x-1))
num=int(input("Enter any number:"))
result=Factorial(num)
print("The Factorial of",num,"is",result)