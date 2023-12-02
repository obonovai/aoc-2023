wins = 0
powers = 0
with open('02/input') as f:
    for line in f:
        win, reds, greens, blues = True, 0, 0, 0
        id, bag = line.removeprefix('Game').split(':')
        rounds = bag.split(';')
        for round in rounds:
            round = round.strip().split(',')
            for hand in round:
                count, cube = hand.strip().split(' ')
                if cube == 'red':
                    if int(count) > 12: win = False
                    if int(count) > reds: reds = int(count)
                elif cube == 'green':
                    if int(count) > 13: win = False
                    if int(count) > greens: greens = int(count)
                elif cube == 'blue':
                    if int(count) > 14: win = False
                    if int(count) > blues: blues = int(count)
        if win: wins += int(id)
        powers += reds * greens * blues
print(wins)
print(powers)
