sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_names = sentence.split()

#number = [len(i) for i in list_names]


counter ={k:len(k) for k in list_names}
"""
for k in list_names:
    counter[k] = len(k)
"""
print(counter)






weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

#conv = temp_c * 9/5) + 32 = temp_f

weather_t = {k:((v*9/5) + 32) for k,v in  weather_c.items()}
print(weather_t)