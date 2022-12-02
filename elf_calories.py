file = open('p1.txt', 'r')

sum = 0
calories = []

while True:

    line = file.readline()

    if not line:
        line_1 = file.readline()
        if not line_1:
            print(sum)
            calories.append(sum)
            break
    
    if line == '\n':
        print(sum)
        calories.append(sum)
        sum = 0
        print("Hooray!")
    else:
        sum = sum + int(line)

    
print(calories)

max_value = max(calories)
max_index = calories.index(max_value)

print(max_index + 1, max_value)

calories.sort(reverse=True)
print(calories)



    