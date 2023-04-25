# region Exercise I - students and thier score
# import random
#
# students = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# # score = {student:random.randint(1,100) for student in students}
# # print(score)
#
# students_scores = {'Alex': 43, 'Beth': 32, 'Caroline': 88, 'Dave': 84, 'Eleanor': 52, 'Freddie': 9}
#
# # new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# #Student pass dict
# passed_student = {student:score for (student, score) in students_scores.items()
#                   if score > 50}
# print(passed_student)
# endregion

# region Exercise II - Sentences and letters in sentence
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word:len(word) for word in sentence.split(" ")}
#
# print(result)
# endregion

# region Exercise III - Conver temperature from Celcius to Farenheit
weater_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednsday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
#To convert temp_c into temp_f:
#(temp_c * 9/5) + 32 = temp_f

weater_f = {day:(temp_c * 9/5)+32 for (day, temp_c) in weater_c.items()}
print(weater_f)
# endregion


