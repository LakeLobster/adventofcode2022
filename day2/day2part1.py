
LOSS = 0
DRAW = 3
WIN = 6

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

shapescores = {ROCK:1, PAPER:2, SCISSORS:3}
keys = {'A': ROCK, 'X': ROCK, 'B': PAPER, 'Y': PAPER, 'C': SCISSORS, 'Z': SCISSORS}

outcomes = {
    (ROCK, SCISSORS) : WIN,
    (ROCK, ROCK): DRAW,
    (ROCK, PAPER): LOSS,

    (PAPER, SCISSORS): LOSS,
    (PAPER, ROCK): WIN,
    (PAPER, PAPER): DRAW,

    (SCISSORS, SCISSORS): DRAW,
    (SCISSORS, ROCK): LOSS,
    (SCISSORS, PAPER): WIN,
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
            player = keys[line[2]]
            opponent = keys[line[0]]
            total += score(player,opponent)
    print(f"Total Score: {total}. Lines read: {linesRead}")
