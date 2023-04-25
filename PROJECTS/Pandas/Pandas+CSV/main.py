# Third solution

import pandas

data = pandas.read_csv("weather_data.csv")

# # Get whole column
# temperatures = data["temp"].to_list()
# print(temperatures)
#
# # First solution for calculate average temperature
# average_temp = sum(temperatures) / len(temperatures)
# print(f"Solution one -> Average temp: {average_temp}")
#
# # Secon solution for calculate average temperature
# print(f"""Solution one -> Average temp: {data["temp"].mean()}""")
#
# # Get maxium value of series
# print(f"""Maximum value is {data["temp"].max()}""")
#
# # Solutions how to get data from the specific column/row
# print(data["temp"])
# # or
# print(data.temp)

# # Solution how to get a data from the speficic row
# print(data[data.day == "Monday"])

# # Get whole row from the day where the themperature was maximum
# print(data[data.temp == data["temp"].max()])
# # or
# print(data[data.temp == data.temp.max()])
# # this 1: check the max "data["temp"].max()" and then check in which column it is "data.temp"
#
# monday = data[data.day == "Monday"]
# print(monday.condition)

# # Get temperature form monday and print it in farenheit
# monday_data = data[data.day == "Monday"]
# print(f"data type of monday_data: {type(monday_data.temp)}")
#
# monday_temp_C = int(monday_data.temp)
# monday_temp_F = monday_temp_C * 1.8 + 32
#
# print(f"On monday was {monday_temp_F}[F]")

# Create new data and file from scratch
data_dict = {
    "students": ["Pawel", "Michal", "Wojtek"],
    "scores": [100, 50, 0]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


# First solution
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# The results:
# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

# Second solution
#
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

