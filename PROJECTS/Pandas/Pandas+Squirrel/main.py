import pandas
import csv

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# "Primary Fur Color"

fur_color = "Primary Fur Color"

# Find only Grey Squirrels
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(len(grey_squirrels))

# TODO 0.1: Count how many grey, cinamon and black squirrels are
count = data.pivot_table(columns=["Primary Fur Color"], aggfunc="size")

# print(count)
print(type(count))

print(count["Black"])
print(count["Cinnamon"])
print(count["Gray"])

# Create CSV file
count.to_csv("Squirrel_count.csv")
