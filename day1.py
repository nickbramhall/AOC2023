input_file = 'input/day1.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

calibration_total = 0

# Read through each line
for line in all_lines:
    for i, c in enumerate(line):
        if c.isdigit():
            first_digit=c
            # print(f'First digit: {first_digit}')
            break
    reverse_line = line[::-1]
    for i, c in enumerate(reverse_line):
        if c.isdigit():
            last_digit=c
            # print(f'Last digit: {last_digit}')
            break
    calibration_value = int(first_digit + last_digit)
    # print(calibration_value)
    calibration_total = calibration_total + calibration_value

print(f'The answer to Part 1 is: {calibration_total} ')

## Part 2

# Convert strings to texts

numbers_list = ['1','2','3','4','5','6','7','8','9']
numbers_sp_list = ['one','two','three','four','five','six','seven','eight','nine']
replace_list = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

calibration_total = 0

for line in all_lines:
    result_dict = {}
    # Use enumerate to find all of the digits and their position in the string, store these in result_dict
    for i, c in enumerate(line):
        if c.isdigit():
            result_dict[i]=c
    # Use a search to find all instances of each 'number' and store their position in result_dict
    for number in numbers_sp_list:
        results = [i for i in range(len(line)) if line.startswith(number, i)]
        # If there are results then iterate through to get each position
        if results:
            for result in results:
                result_dict[result]=number
    #Sort the dictionary containing the positions of each digit/number
    result_dict=dict(sorted(result_dict.items()))
    # Get the first and last entry from the sorted dictionary
    first_digit = list(result_dict.values())[0]
    last_digit = list(result_dict.values())[-1]
    # Now convert any 'numbers' to digits
    try:
        first_digit_int = int(first_digit)
    except:
        first_digit_int = replace_list[first_digit]
    try:
        last_digit_int = int(last_digit)
    except:
        last_digit_int = replace_list[last_digit]
    # Now concatenate the first and last digit to get the calibration value
    calibration_value = int(str(first_digit_int) + str(last_digit_int))
    # Now add the new value to the running total
    calibration_total = calibration_total + calibration_value

print(f'The answer to Part 2 is: {calibration_total} ')