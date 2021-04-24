
list = [1, 5, 6, 8]

print("list: ", list)


convertedArray = []
sum = 0
for i in list:
    sum = sum +i
    convertedArray.append(sum)

result = convertedArray[0: len(convertedArray)-1]
print("result: ", result)
print("I love CI/CD pipelines")