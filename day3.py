input_file = 'input/day3-test.txt'
import re

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

print(all_lines)

# map into a 2d array for later use?

map = []

for line in all_lines:
    line_list = []
    for i, c in enumerate(line):
        line_list.append(c)
    map.append(line_list)

print(map)

#find numbers, find the coordinates of first digit, and number of digits
#check they are surrounded by . ?

search_numbers = []

for line in all_lines:
    numbers = re.findall(r'\b\d+\b', line)
    search_numbers.append(numbers)

print(search_numbers)

search_number_details = []

i=0
for line in search_numbers:
    if len(line):
        number_details = []
        for number in line:
            number_str = str(number)
            length_of_number = len(number_str)
            first_number = int(number_str[0])
            index_of_number=all_lines[i].find(number)
            print(f'first number:{first_number} -- position:{index_of_number} -- length:{length_of_number}')
            number_details.append((index_of_number,length_of_number))
        search_number_details.append(number_details)
    else:
        blank=[]
        search_number_details.append(blank)
    i=i+1

print(search_number_details)

for line in search_number_details:
    if len(line):
        for number in line:
            #check left
            try:
                if map[i][number[0]] != '.':
                    check = False
            except:
                continue
