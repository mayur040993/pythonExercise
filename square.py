def square1(p):
    c=p*(p+1)/2;
    d=p*(p+1)*(2*p+1)/6
    c=c**2;
    print c-d;

p=input("Enter the number n : ");
square1(p)

