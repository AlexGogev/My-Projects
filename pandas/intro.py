
"""
data = []
with open("pandas\\weather_data.csv") as weather:
    weather_list = (weather.readlines())
    for i in weather_list:
        data.append(i[0:-1])

#print(data)
"""

"""
import csv
temperatures = []
with open("pandas//weather_data.csv") as data:
    data = csv.reader(data) #obejct
    
    for i in data:
        if i[1] != "temp":
            temperatures.append(int(i[1]))
    
print(temperatures)
"""

import pandas

data = pandas.read_csv("pandas//weather_data.csv")
print(data)
print(data["temp"].to_list())

#data.frame is all table
#series is the colunm like a list

data_dict  = data.to_dict()
print(data_dict)


#### calc average temp 
average_temp = data["temp"].to_list()
total_tamp = sum(average_temp) / len(average_temp)
print(total_tamp)

 ##or
av_temp = data["temp"].mean()
print(av_temp)

 #or max
av_max = data["temp"].max()
print(av_max)


##get data in Rows
data_row = data[data.day == "Monday"] # or data["day" == "Monday"]
print(data_row)



##How to Create data frame
data_dict = {
    "students": ["az", "ti"],
    "scores" : [5,6]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("pandas//new_data.csv")