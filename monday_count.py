import calendar

#calendar.prcal(2015,w=1,l=1,c=6)
def calculate_monday():
    monday=0;
    for year in range(0,2):
        for month in range(1,12):
            day=calendar.weekday(2015+year,month,1)
            if(day==0):
                monday=monday+1;
    print(monday);

calculate_monday();
