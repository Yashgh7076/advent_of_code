import re
# Read stacks

file = open('test_5.txt', 'r')

lines = file.readlines()

file.close()

buffer = []
instruction_line = 1

for line in lines:

    if len(line) == 1:
        break
    else:
        new_line = line.replace('[',' ')
        new_line = new_line.replace(']',' ')
        buffer.append(new_line)

    instruction_line += 1

stack_ids = buffer[-1]
pos = []
idx = 0
for char in stack_ids:
    if char != ' ' and char != '\n':
        pos.append(idx)
    idx += 1

stacks = []
for i in range(len(pos)):
    el_list = []
    stacks.append(el_list)

for i in range(len(buffer) - 1):
    s_inp = buffer[i]
    for j in range(len(pos)):
        if s_inp[pos[j]] != ' ':
            stacks[j].append(s_inp[pos[j]])

print('Original stacks', stacks)

nbr = []
src = []
dst = []

for i in range(instruction_line, len(lines)):
    
    temp = lines[i].replace(' ', '')
    temp = re.sub("\D", "", temp)
    nbr.append(temp[0])
    src.append(temp[1])
    dst.append(temp[2])
    
file = open('instructions_5.txt', 'w')
for instruction in range(len(nbr)):
    pipe_output = 'move ' + str(nbr[instruction]) + 'from ' + str(src[instruction]) + 'to' + str(dst[instruction])
    file.write(pipe_output)
file.close()

for instruction in range(len(nbr)):
    
    number_boxes = int(nbr[instruction])
    source = int(src[instruction]) - 1
    destination = int(dst[instruction]) - 1

    while number_boxes > 0:
        pop_elem = stacks[source].pop(0)
        stacks[destination].insert(0, pop_elem)
        #stacks[source].pop(0)
        number_boxes -= 1
        
    
print(stacks)


    

    