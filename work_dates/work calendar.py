
import datetime
today = datetime.datetime.now() 
print(today.strftime("%y, %m, %d"))
print(today.strftime('%j'))   #j

year_date = []
day_num = "1"
x = int(day_num) 
day_num.rjust(3 + len(day_num), '0')
year = "2022"
for i in range(0,365):
   res = datetime.datetime.strptime(year + "-" + f'{x}', "%Y-%j").strftime("%m-%d-%Y %a") 
   x += 1
   year_date.append(res)
print("Resolved date : " + str(res))


one_to_eight = ["OFF","OFF","OFF","OFF","ON","ON","ON","ON"] 

work = {}
x = 0
for i in year_date:
   
   work[i] =one_to_eight[x]
   if x == 7:
      x = 0
   else:  
      x += 1

with open("dates.txt", "w") as work_dates:
   for k,v in work.items():
      work_dates.write(f"{k} --> {v} \n")




