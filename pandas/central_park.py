import pandas

data = pandas.read_csv("pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors =  data["Primary Fur Color"].to_list()
gray = colors.count("Gray")
black = colors.count("Black")
cinnamon = colors.count("Cinnamon")



data_dicts = {
    "Fur color" : ["Gray", "Cinnamon", "black"],
    "Count" : [gray, cinnamon, black,]
}


print(data_dicts)
extracted_to_new = pandas.DataFrame(data_dicts)
extracted_to_new = extracted_to_new.to_csv("pandas//extracted.csv")