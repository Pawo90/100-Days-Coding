
file_1 = open("file1.txt", "r").readlines()
file_2 = open("file2.txt", "r").readlines()

file_1 = [int(number) for number in file_1]
file_2 = [int(number) for number in file_2]

print(file_1)
print(file_2)

result = [int(number) for number in file_1 if number in file_2]
print(result)
