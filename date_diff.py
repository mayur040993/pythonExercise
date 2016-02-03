import datetime

def diff_date():
    year1=input("Input Year of date 1 : ")
    month1=input("Input month of date 1 (1-12) : ")
    day1=input("Input day of date 1 : ")
    p=datetime.date(year1,month1,day1)
    print p;
    year2=input("Input Year of date 2 : ")
    month2=input("Input month of date 2 (1-12) : ")
    day2=input("Input day of date 2 : ")
    k=datetime.date(year2,month2,day2)
    print k;
    print k-p;

diff_date()
