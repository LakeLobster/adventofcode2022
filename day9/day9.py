# 6332 for part 1
# 2551 for part 2

N = (0, 1)
S = (0, -1)
W = (-1, 0)
E = (1, 0)

NW = (-1, 1)
SW = (-1, -1)
NE = (1, 1)
SE = (1, -1)

Z = (0, 0)
K = ['H', '1', '2', '3', '4', '5', '6', '7', '8', '9']

DIRECTIONS = {
    'U': N,
    'D': S,
    'L': W,
    'R': E
}

# (direction,displacement)
MOTIONS = {
    (N, SW): NE,
    (N, S): N,
    (N, SE): NW,

    (W, E): W,
    (W, NE): SW,
    (W, SE): NW,

    (S, NW): SE,
    (S, N): S,
    (S, NE): SW,

    (E, W): E,
    (E, NW): SE,
    (E, SW): NE,

    # part two motions
    (NW, SE): NW,
    (NW, S): NW,
    (NW, SW): N,
    (NW, E): NW,
    (NW, NE): W,

    (NE, NW): E,
    (NE, W): NE,
    (NE, SW): NE,
    (NE, S): NE,
    (NE, SE): N,

    (SE, SW): E,
    (SE, W): SE,
    (SE, NW): SE,
    (SE, N): SE,
    (SE, NE): S,

    (SW, NW): S,
    (SW, N): SW,
    (SW, NE): SW,
    (SW, E): SW,
    (SW, SE): W,
}


def translate(p, s):
    return p[0] + s[0], p[1] + s[1]


def move(head_position, tail_position, motion):
    displacement = (tail_position[0] - head_position[0], tail_position[1] - head_position[1])
    head_position = translate(head_position, motion)
    dd = (motion, displacement)
    movement = Z
    if dd in MOTIONS:
        movement = MOTIONS[dd]
        tail_position = translate(tail_position, movement)

    return head_position, tail_position, movement


def compute_position_spot(position, size, center):
    (x, y) = position[0] + center[0], size[1] - position[1] - 1 - center[1]
    return x, y


def compute_position_char(coordinate, positions, size, center):
    (x,y) = coordinate
    (cx, cy) = center[0], size[1] - center[1] - 1
    char = 's' if cx == x and cy == y else '.'
    for c in range(len(K) - 1, -1, -1):
        (px, py) = compute_position_spot(positions[c], size, center)
        if px == x and py == y:
            char = K[c]
    return char


def visualize(positions, size, center = (0,0)):
    for y in range(size[1]):
        print("".join([compute_position_char((x, y), positions, size, center) for x in range(size[0])]))
    print(" ")


if __name__ == "__main__":
    rope_length = 10
    vizsize = (26,20)
    vizoffset = (11,5)

    with open('input','r') as input:
      moves = [line.rstrip().split(' ') for line in input]

    positions = [(0,0) for i in range(rope_length)]
    # print(" == Initial State ==")
    # visualize(positions, vizsize, vizoffset)

    visited = {}
    for m in moves:
        # print(f" == {m[0]} {m[1]} ==")
        (mv, num) = (m[0],int(m[1]))
        for i in range(num):
            knot_motion = DIRECTIONS[mv]
            knot1 = positions[0]
            knot2 = positions[1]
            for knot in range(rope_length - 1):
                (first, second, knot_motion) = move(knot1, knot2, knot_motion)
                positions[knot] = first
                knot1 = knot2
                if knot <= rope_length - 3:
                    knot2 = positions[knot+2]
            positions[rope_length - 1] = second
            visited[positions[rope_length-1]] = True
        # visualize(positions,vizsize,vizoffset)

    print(len(visited))
