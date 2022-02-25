# put your python code here
year = int(input())
four_hundred = 400
if year % four_hundred == 0:
    print("Leap")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("Leap")
    else:
        print("Ordinary")
