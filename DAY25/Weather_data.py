"""
with open("weather_data - Sheet1.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv
with open("weather_data - Sheet1.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data - Sheet1.csv")
data_dict = data.to_dict()
temperatures = data["temp"].to_list()
days = data["day"].to_list()
print(data[data.temp == max(data["temp"])])

print(data.condition)
"""
import pandas as pd
data_dict = {
    "students" : ["Rishi","Rishedra", "Rambo"],
    "scores" : [26,36,46]
}
data = pd.DataFrame(data_dict)
data.to_csv("Mark_List.csv")
