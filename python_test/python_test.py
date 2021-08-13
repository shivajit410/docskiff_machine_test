import datetime

startDay = inp/ut("Enter start date: ")
# startDay = "20180728"
endDay = input("Enter end date: ")
# endDay = "20180927"

startDay = datetime.datetime.strptime(startDay, "%Y%m%d")
endDay = datetime.datetime.strptime(endDay, "%Y%m%d")

SATURDAY_VAL = 5;
NTH_VAL = 4;

def get_desired_dates(startDay, endDay):

    if (startDay.year < 1900 or endDay.year > 2100):
        print("Dates does not exist in the range from 1900 to 2100")
        return

    def daterange(startDay, endDay):
        for n in range(int ((endDay - startDay).days)+1):
            yield startDay + datetime.timedelta(n)
    
    for dt in daterange(startDay, endDay):
        condition1 = (int(datetime.datetime.strftime(dt, "%d")) % 5 == 0)
        condition2 = (dt.day - 1) // 7 == (NTH_VAL - 1)
        if dt.weekday() == SATURDAY_VAL:
            if (condition1 ^ condition2):
            # if ((condition1 and (not condition2)) or ((not condition1) and condition2)):
                print(dt.strftime("%Y%m%d"))

get_desired_dates(startDay, endDay)
