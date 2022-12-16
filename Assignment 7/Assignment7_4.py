def Sum(n):
    if n==0:
        return 0
    return(n%10+Sum(int(n/10)))
num=int(input("Enter any number:"))
result=Sum(num)
print("Sum of Digit in",num,"is",result)