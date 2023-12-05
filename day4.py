input_file = 'input/day4.txt'
import re

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

# The first match makes the card worth one point and 
# each match after the first doubles the point value of that card.

win_score = 0

for card in all_lines:
    match_count = 0
    card_score = 0
    card_details,winnings = card.split(' | ')
    # print(winnings)
    # winning_numbers = winnings.split(' ')
    winning_numbers = re.findall(r'\b\d+\b', winnings)
    # print(winning_numbers)
    game_no,all_entry_numbers = card_details.split(': ')
    # entry_numbers = all_entry_numbers.split(' ')
    entry_numbers = re.findall(r'\b\d+\b', all_entry_numbers)
    card_no = re.search(r'\b\d+\b', game_no).group(0)
    print(card_no)
    # print(entry_numbers)
    for entry_number in entry_numbers:
        if entry_number in winning_numbers:
            match_count = match_count + 1
    if match_count == 1:
        card_score = 1
    elif match_count > 1:
        card_score = 1
        for i in range(match_count-1):
            card_score = card_score * 2
    # print(f'Winning Matches: {match_count} -- Card score: {card_score}')
    win_score = win_score + card_score

print(win_score)

# Part 2

results={}

i=1
for card in all_lines:
    results[f'{i}']=1
    i+=1

print(results)

for card in all_lines:
    match_count = 0
    card_details,winnings = card.split(' | ')
    winning_numbers = re.findall(r'\b\d+\b', winnings)
    game_no,all_entry_numbers = card_details.split(': ')
    entry_numbers = re.findall(r'\b\d+\b', all_entry_numbers)
    card_no = re.search(r'\b\d+\b', game_no).group(0)
    print(f'Checking card: {card_no}')
    for entry_number in entry_numbers:
        if entry_number in winning_numbers:
            match_count = match_count + 1
    if match_count > 0:
        for match in range(int(card_no)+1,int(card_no)+match_count+1):
            print(match)
            results[str(match)]=results[str(match)]+(1*results[card_no])

print(results)

total_cards=0

for k,v in results.items():
    total_cards=total_cards+v

print(total_cards)