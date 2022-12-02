file = open('p2.txt', 'r')

lines = file.readlines()

total_score = 0

scores = {
    "AX": 3,
    "AY": 1,
    "AZ": 2,
    "BX": 1,
    "BY": 2,
    "BZ": 3,
    "CX": 2,
    "CY": 3,
    "CZ": 1
}


for line in lines:

    shape_score = 0
    round_score = 0

    words = line.strip().split()

    opponent, player = words[0], words[1]

    if player == 'X':
        round_score = 0
    elif player == 'Y':
        round_score = 3
    elif player == 'Z':
        round_score = 6

    print(opponent+player)
    shape_score = scores[opponent+player]

    print(shape_score, round_score)

    total_score = total_score + shape_score + round_score


print(total_score)



    

    