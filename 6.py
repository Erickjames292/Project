n=int(input("enter the number:"));
c=0;
for i in range(2,n):
    if(n%i==0):
        c=1;
if(c==1):
    print(n,"is not a prime number");
else:
    print(n,"is a prime number");
