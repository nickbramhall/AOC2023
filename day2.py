input_file = 'input/day2.txt'

# Read in all the data and strip out any whitespace at the end of lines
all_lines = [line.rstrip('\n') for line in open(input_file)]

# print(all_lines)

# only 12 red cubes, 13 green cubes, and 14 blue cubes

red_limit = 12
green_limit = 13
blue_limit = 14
game_id_total= 0

for line in all_lines:
    game_id, game_play = line.split(":")
    # print(game_id)
    game_text,game_id_int = game_id.split(" ")
    games = game_play.split("; ")
    # print(games)
    i=0
    game_valid = True
    for game in games:
        game_dict={'red':0,'green':0,'blue':0}
        balls = game.split(",")
        # print(balls)
        red_limit_ok = False
        green_limit_ok = False
        blue_limit_ok = False
        for ball in balls:
            ball=ball.lstrip()
            # print(ball)
            number, colour = ball.split(" ")
            game_dict[colour]=int(number)
            # print(f'{colour} - {number}')
        if game_dict['red'] <= red_limit:
            # print("game_dict['red'] is below " + str(red_limit))
            red_limit_ok = True
        if game_dict['blue'] <= blue_limit:
            blue_limit_ok = True
        if game_dict['green'] <= green_limit:
            green_limit_ok = True
        # print(f'{red_limit_ok} - {green_limit_ok} - {blue_limit_ok}')
        if red_limit_ok is False:
            game_valid = False
        if green_limit_ok is False:
            game_valid = False
        if blue_limit_ok is False:
            game_valid = False
    if game_valid:
        print(f'Game ID: {game_id} is valid')
        game_id_total = game_id_total + int(game_id_int)

print(game_id_total)
        # red_pos=game.find(" red")
        # print(game[red_pos-1])
        # blue_pos=game.find(" blue")
        # blue_pos=game.find(" green")

## Part 2

power_sum = 0
for line in all_lines:
    game_id, game_play = line.split(":")
    games = game_play.split("; ")
    game_dict={'red':0,'green':0,'blue':0}
    for game in games:
        balls = game.split(",")
        for ball in balls:
            ball=ball.lstrip()
            number, colour = ball.split(" ")
            if int(number) > game_dict[colour]:
                game_dict[colour]=int(number)
    # print(game_dict)
    power = game_dict['red'] * game_dict['green'] * game_dict['blue']
    power_sum = power_sum + power

print(power_sum)