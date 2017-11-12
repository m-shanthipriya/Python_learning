year = int(input("Enter a Year [YYYY]: "))
def yearFunction():
    print (year)
yearFunction()

month = int(input("Enter a month [1-12]: "))
#month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
def monthFunction():
    if month <= 12:
        print (month)
    else:
        print ("Given month is incorrect")
monthFunction()

day = int(input("Input a day [1-31]: "))
day += 1
def dayFunction():
    if day <= 31:
        print (day)
    else:
        print ("Given day is incorrect")
dayFunction()
