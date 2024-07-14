import random

temperatures = []

for i in range(7):
    x = random.randint(26, 41)  
    temperatures.append(x) 

days_of_the_week=["Sunday","Monday","Teusday","Wednesday","Thursday","Friday","Saturday"]


good_days_count = 0
for j in range(len(days_of_the_week)):
    t=temperatures[j]
    if t % 2== 0:
        good_days_count+=1

highest_temp = 0
highest_temp_day = 41
lowest_temp_day = ""

for k in range(len(temperatures)):
    temp=temperatures[k]
    if temp > highest_temp:
        highest_temp_day = days_of_the_week[k]
    if temp < lowest_temp:
        lowest_temp_day = days_of_the_week[k]

sum=0
for i in range(len(temperatures)):
    sum+= temperatures[i]

average = sum/7

above_avg = []
for i in range(len(temperatures)):
    if temperatures[i] > average:
        day = days_of_the_week[i]
        above_avg.append(day)




print("The Weather Report:")
print(f"Temperatures for the week: {days_of_the_week}")
print(f"Good days for Shelly: {good_days_count}")
print(f"Highest temperature was: {highest_temp} on {highest_temp_day}")
print(f"Lowest was: {lowest_temp} on {lowest_temp_day}")
print(f"Average temperature was: {average}")
print(f"Days with temperatures above average: {above_avg}")