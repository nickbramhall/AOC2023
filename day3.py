input_file = 'input/day3.txt'
import re

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

# Extend the map in all directions by one '.' character to help with edges

width = len(all_lines[0]) + 2

all_lines_extended = []
all_lines_extended.append('.'*width)
for line in all_lines:
    all_lines_extended.append('.'+line+'.')
all_lines_extended.append('.'*width)

# print(all_lines_extended)

# map into a 2d array for later use?

map = []

for line in all_lines_extended:
    line_list = []
    for i, c in enumerate(line):
        line_list.append(c)
    map.append(line_list)

# print(map)

#find numbers, find the coordinates of first digit, and number of digits
#check they are surrounded by . ?

search_numbers = []
search_list = []

for line in all_lines_extended:
    numbers = re.findall(r'\b\d+\b', line)
    search_numbers.append(numbers)
    for number in numbers:
        search_list.append(number)

print(f'Search numbers: {search_numbers}')
print(f'Search list: {search_list}')

search_number_details = []
search_list_details = []

i=0
for line in search_numbers:
    if len(line):
        number_details = []
        start=0
        for number in line:
            number_str = str(number)
            length_of_number = len(number_str)
            first_number = int(number_str[0])
            index_of_number=all_lines_extended[i].find(number,start)
            start=index_of_number+length_of_number
            print(f'first number:{first_number} -- position:{index_of_number} -- length:{length_of_number}')
            number_details.append((index_of_number,length_of_number))
            search_list_details.append((number,i,index_of_number,length_of_number))
        search_number_details.append(number_details)
    else:
        blank=[]
        search_number_details.append(blank)
    i=i+1

print(search_number_details)

success=[]
fail=[]
fail_sum=0
success_sum=0
i=0
line_counter=1

for line in search_number_details:
    if len(line):
        for number in line:
            print(f'Checking {search_list[i]}')
            left_check = True
            right_check = True
            top_check = True
            bottom_check = True
            #check left
            left_string = all_lines_extended[line_counter-1][number[0]-1]
            #print(f'String left: {left_string}')
            if left_string != '.':
                left_check = False
            #check right
            right_string = all_lines_extended[line_counter-1][number[0]+number[1]]
            #print(f'String right: {right_string}')
            if right_string != '.':
                right_check = False
            # check top
            top_string = all_lines_extended[line_counter-2][number[0]-1:number[0]+number[1]+1]
            #print(f'String above: {top_string}')
            for k, c in enumerate(top_string):
                if (c.isdigit() == True) or (c == '.'):
                    top_check = True
                else:
                    top_check = False
                    break
            bottom_string = all_lines_extended[line_counter][number[0]-1:number[0]+number[1]+1]
            #print(f'String below: {bottom_string}')
            for k, c in enumerate(bottom_string):
                if (c.isdigit() == True) or (c == '.'):
                    bottom_check = True
                else:
                    bottom_check = False
                    break
            print(top_string)
            print(left_string+search_list[i]+right_string)
            print(bottom_string)
            if False in [left_check,right_check,top_check,bottom_check]:
                fail.append(search_list[i])
                fail_sum=fail_sum+int(search_list[i])
                print('This is a part!')
            else:
                success.append(search_list[i])
                success_sum=success_sum+int(search_list[i])
                print('Not a part!')
            # input("Press Enter to continue...")
            i=i+1
    line_counter = line_counter + 1

print(fail)
print(fail_sum)

print(f'Correct answer is 536202')

# Part 2

print(search_list_details)

# Find all the * locations
all_star_locations = []

line_counter = 0
for line in all_lines_extended:
    char_counter = 0
    for k, c in enumerate(line):
        if c == "*":
            position = (line_counter,char_counter)
            all_star_locations.append(position)
        char_counter = char_counter + 1
    line_counter = line_counter + 1

print(f'Number of stars to search: {len(all_star_locations)}')
print(all_star_locations)

# Start at above and go clockwise around checking for a number start

ratio_sum = 0

for star in all_star_locations:
    result = []
    # print(f'Checking {all_lines_extended[star[0]-1][star[1]]}')
    if all_lines_extended[star[0]-1][star[1]].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]-1) and (search[2] == star[1]):
                result.append(search[0])
    if all_lines_extended[star[0]-1][star[1]+1].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]-1) and (search[2] == star[1]+1):
                # print(search[0])
                result.append(search[0])
    
    if all_lines_extended[star[0]][star[1]+1].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]) and (search[2] == star[1]+1):
                # print(search[0])
                result.append(search[0])

    if all_lines_extended[star[0]+1][star[1]+1].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]+1) and (search[2] == star[1]+1):
                # print(search[0])
                result.append(search[0])

    if all_lines_extended[star[0]+1][star[1]].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]+1) and (search[2] == star[1]):
                # print(search[0])
                result.append(search[0])

    if all_lines_extended[star[0]+1][star[1]-1].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]+1) and ((search[2] == star[1]-1) or (search[2] == star[1]-2) or (search[2] == star[1]-3)):
                # print(search[0])
                result.append(search[0])



    if all_lines_extended[star[0]][star[1]-1].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            if (search[1] == star[0]) and ((search[2] == star[1]-1) or (search[2] == star[1]-2) or (search[2] == star[1]-3)):
                # print(search[0])
                result.append(search[0])

    # print(f'Checking {all_lines_extended[star[0]-1][star[1]-1]}')
    if all_lines_extended[star[0]-1][star[1]-1].isdigit():
        # print(f'Found a digit!')
        for search in search_list_details:
            # print(f'{star[1]-1},{star[1]-2},{star[1]-3}')
            if (search[1] == star[0]-1) and ((search[2] == star[1]-1) or (search[2] == star[1]-2) or (search[2] == star[1]-3)):
                # print(search[0])
                result.append(search[0])
    if len(result) == 2:
        ratio = int(result[0]) * int(result[1])
        ratio_sum = ratio_sum + ratio
    print(result)

print(ratio_sum)