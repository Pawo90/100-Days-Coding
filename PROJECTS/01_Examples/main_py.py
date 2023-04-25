# region Iterrations through dictionares and dataframe

# region -> Through Dictionares
# mydict = {
#     "James": 49,
#     "Marry": 20
# }
#
# # for (key, value) in dict.items() - .items() - whole items in dict
# for (name, value) in mydict.items():
#     # Printing keys
#     print(name)
#     # Printing values
#     print(value)
# endregion

# region -> Through DataFrame
# import pandas
#
# mydict = {
#     "names": ["James", "Marry"],
#     "age": [32, 25]
# }
# #Create DataFrame
# ndf = pandas.DataFrame(mydict)
# print(f"Dataframe:\n{ndf}\n")
# #
# # #Iteration through rows and columns
# # # for (key, values) in ndf.items():
# # #     print(key)
# #
# for (index, row) in ndf.iterrows():
#     # print(index)
#     # print(row.names)
#     # print(row.age)
#     if row.names == "James":
#         print(row.age)
# endregion

# endregion th

# region Comprehensions

# region -> List

# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
# endregion

# region -> Dictionares

# new_dict = {key:value for (key, value) in dict}
# new_dict = {key:value for (key, value) in dict if}
# endregion

# endregion