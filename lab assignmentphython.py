# NAME: Alok Kumar
# Roll No.: 2501350016
# Date: 10/10/25
# Project: Building a Calorie Tracking Console App

print("welcome to daily calorie tracker")
print("enter your daily calorie intake")
Meal=[]
Calorie=[]
no=int(input("enter the number of meal you ate:"))
for i in range(no):
    m=(i+1)
    c=(i+1)
    m=input("enter meal:")
    c=float(input("enter calorie:"))
    Meal.append(m)
    print(Meal)
    Calorie.append(c)
    print(Calorie)

total_calorie=sum(Calorie)
print(total_calorie)

average=(total_calorie)
average=total_calorie/no
print(average)

daily_limit=float(input("enter daily limit calorie"))
if total_calorie > daily_limit:
    print("warning")

else:
    print("success")

    print("control your calorie limit")