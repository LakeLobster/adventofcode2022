
LOSS = 0
DRAW = 3
WIN = 6

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

shapescores = {ROCK:1, PAPER:2, SCISSORS:3}
keys = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
outcomes = {'X': LOSS, 'Y': DRAW, 'Z': WIN}

moves = { #opponents move, what player throws
    (ROCK, WIN) : PAPER,
    (ROCK, DRAW): ROCK,
    (ROCK, LOSS): SCISSORS,

    (PAPER, WIN): SCISSORS,
    (PAPER, DRAW): PAPER,
    (PAPER, LOSS): ROCK,

    (SCISSORS, WIN): ROCK,
    (SCISSORS, DRAW): SCISSORS,
    (SCISSORS, LOSS): PAPER,
}



def score(player, opponent):
    return shapescores[player] + outcomes[(player,opponent)]



if __name__ == "__main__":
    #for a in ['A','B','C']:
    #    for b in ['X','Y','Z']:
    #        print(f"{a} {b} {score(keys[b],keys[a])}")



    #exit(0)
    total = 0
    linesRead = 0
    with open('input.txt','r') as input:
        while True:
            line = input.readline()
            linesRead += 1
            if line == "" or line == "\n":
                break
            opponent = keys[line[0]]
            outcome = outcomes[line[2]]
            player = moves[(opponent,outcome)]
            total += shapescores[player] + outcome
    print(f"Total Score: {total}. Lines read: {linesRead}")
