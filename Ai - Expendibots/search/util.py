"""
This module contains some helper functions for printing actions and boards.
Feel free to use and/or modify them to help you develop your program.
"""
import math
from itertools import permutations

def closest(ntuple, whites):
    wp = list()
    for piece in whites:
        wp.append((piece[1],piece[2]))
    perms_of_wp = list(permutations(wp))
    print(perms_of_wp)

    optimum = dict()
    dist = list()
    for option in perms_of_wp:
        i=0
        for pos in ntuple:
            optimum[option[i]] = pos
            i+=1
        #calculate total distance of dictionary
        dist.append(euclidDictionary(optimum))
    for option in perms_of_wp:
        i=0
        for pos in ntuple:
            optimum[option[i]] = pos
            i+=1
        if(euclidDictionary(optimum)==min(dist)):
            print("testing optimum")
            print(optimum)
            return optimum
    
            
def euclidDictionary(dct):
    dist = 0
    for k, v in dct.items():
        dist += euclideanDistance(k[0],k[1],v[0],v[1])
    return dist
    

def d_comb_whites(ntuple, whites, number_of_whites):
    """
    cumulative distance of the combination of position
    to the white pieces.
    how far do the pices travel to rech this configuration
    """
    distance = 0
    for piece in whites:
        x = piece[1]
        y = piece[2]
        for n in range(number_of_whites):
            distance += euclideanDistance(x,y,ntuple[n][0],ntuple[n][1])
    return distance


def euclideanDistance(x1,y1,x2,y2):
    dist = math. sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist


def kills_all_blacks(ntuple, blacks):
    """
    checks if the whites in a certain comination of 
    positions can kill all blacks when they explode
    """
    #Explosion_zone of the exploded white pieces
    explosion_zone = find_ExplosionZone(ntuple)

    #Explodes any piece? add piece's explosion zone
        #in other words, check if the set explosionZone contains the coordinates of any black piece, if so add its explode zone to the set
    for piece in blacks:
        x = piece[1]
        y = piece[2]

        if(explosion_zone.issuperset({(x,y)})):
            piece_exp_zone = find_ExplosionZone_xy(x,y)
            explosion_zone = explosion_zone.union(piece_exp_zone)

    #Are there any blacks left outside of the final explosion zone- return t or f
    for piece in blacks:
        x = piece[1]
        y = piece[2]
        if(not(explosion_zone.issuperset({(x,y)}))):
            return False

    return True

def find_ExplosionZone_xy(x,y):
    
    explosionZone = set()

    if(x-1>=0 and y-1 >= 0):
        explosionZone.add((x-1,y-1))

    if(x-1 >= 0):
        explosionZone.add((x-1,y))

    if(x-1 >= 0 and y+1 <= 7):
        explosionZone.add((x-1,y+1))

    if(y-1 >= 0):  
        explosionZone.add((x,y-1))

    if(y+1 <= 7):  
        explosionZone.add((x,y+1))

    if(x+1 <= 7 and y-1 >= 0): 
        explosionZone.add((x+1,y-1))

    if(x+1<=7):      
        explosionZone.add((x+1,y))

    if(x+1 <= 7 and y+1 <= 7):   
        explosionZone.add((x+1,y+1))

    return explosionZone

def find_ExplosionZone(ntuples):
    """
    very similar to the kill zone
    finds the explosion zone of the configuration of white pieces
    will be used to check if all blacks are killed
    """
    explosionZone = set()
    for piece in ntuples:
        x = piece[0]
        y = piece[1]
        if(x-1>=0 and y-1 >= 0):
            explosionZone.add((x-1,y-1))

        if(x-1 >= 0):
            explosionZone.add((x-1,y))

        if(x-1 >= 0 and y+1 <= 7):
            explosionZone.add((x-1,y+1))

        if(y-1 >= 0):  
            explosionZone.add((x,y-1))

        if(y+1 <= 7):  
            explosionZone.add((x,y+1))

        if(x+1 <= 7 and y-1 >= 0): 
            explosionZone.add((x+1,y-1))

        if(x+1<=7):      
            explosionZone.add((x+1,y))

        if(x+1 <= 7 and y+1 <= 7):   
            explosionZone.add((x+1,y+1))

    return explosionZone
            


def find_killZones(board_dict, whites, blacks, killZone):
    for piece in blacks:
        x = piece[1]
        y = piece[2]
        if(x-1>=0 and y-1 >= 0):
            killZone.add((x-1,y-1))
            board_dict[(x-1,y-1)] = "."

        if(x-1 >= 0):
            killZone.add((x-1,y))
            board_dict[(x-1,y)] = "."

        if(x-1 >= 0 and y+1 <= 7):
            killZone.add((x-1,y+1))
            board_dict[(x-1,y+1)] = "."

        if(y-1 >= 0):  
            killZone.add((x,y-1))
            board_dict[(x,y-1)] = "."

        if(y+1 <= 7):  
            killZone.add((x,y+1))
            board_dict[(x,y+1)] = "."

        if(x+1 <= 7 and y-1 >= 0): 
            killZone.add((x+1,y-1))
            board_dict[(x+1,y-1)] = "."

        if(x+1<=7):      
            killZone.add((x+1,y))
            board_dict[(x+1,y)] = "."

        if(x+1 <= 7 and y+1 <= 7):   
            killZone.add((x+1,y+1))
            board_dict[(x+1,y+1)] = "."

def place_pieces(board_dict, whites, blacks):

    # palce white pieces on board
    for stack in whites:
        n = stack[0]
        x = stack[1]
        y = stack[2]
        board_dict[(x,y)] = "w"+str(n)

    # palce black pieces on board
    for stack in blacks:
        n = stack[0]
        x = stack[1]
        y = stack[2]
        board_dict[(x,y)] = "b"+str(n)


def print_move(n, x_a, y_a, x_b, y_b, **kwargs):
    """
    Output a move action of n pieces from square (x_a, y_a)
    to square (x_b, y_b), according to the format instructions.
    """
    print("MOVE {} from {} to {}.".format(n, (x_a, y_a), (x_b, y_b)), **kwargs)


def print_boom(x, y, **kwargs):
    """
    Output a boom action initiated at square (x, y) according to
    the format instructions.
    """
    print("BOOM at {}.".format((x, y)), **kwargs)


def print_board(board_dict, message="", unicode=False, compact=True, **kwargs):
    """
    For help with visualisation and debugging: output a board diagram with
    any information you like (tokens, heuristic values, distances, etc.).

    Arguments:
    board_dict -- A dictionary with (x, y) tuples as keys (x, y in range(8))
        and printable objects (e.g. strings, numbers) as values. This function
        will arrange these printable values on the grid and output the result.
        Note: At most the first 3 characters will be printed from the string
        representation of each value.
    message -- A printable object (e.g. string, number) that will be placed
        above the board in the visualisation. Default is "" (no message).
    unicode -- True if you want to use non-ASCII symbols in the board
        visualisation (see below), False to use only ASCII symbols.
        Default is False, since the unicode symbols may not agree with some
        terminal emulators.
    compact -- True if you want to use a compact board visualisation, with
        coordinates along the edges of the board, False to use a bigger one
        with coordinates alongside the printable information in each square.
        Default True (small board).
    
    Any other keyword arguments are passed through to the print function.
    """
    if unicode:
        if compact:
            template = """# {}
#    ┌───┬───┬───┬───┬───┬───┬───┬───┐
#  7 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  6 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  5 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  4 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  3 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  2 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  1 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    ├───┼───┼───┼───┼───┼───┼───┼───┤
#  0 │{:}│{:}│{:}│{:}│{:}│{:}│{:}│{:}│
#    └───┴───┴───┴───┴───┴───┴───┴───┘
# y/x  0   1   2   3   4   5   6   7"""
        else:
            template = """# {}
# ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,7 │ 1,7 │ 2,7 │ 3,7 │ 4,7 │ 5,7 │ 6,7 │ 7,7 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,6 │ 1,6 │ 2,6 │ 3,6 │ 4,6 │ 5,6 │ 6,6 │ 7,6 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,5 │ 1,5 │ 2,5 │ 3,5 │ 4,5 │ 5,5 │ 6,5 │ 7,5 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,4 │ 1,4 │ 2,4 │ 3,4 │ 4,4 │ 5,4 │ 6,4 │ 7,4 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,3 │ 1,3 │ 2,3 │ 3,3 │ 4,3 │ 5,3 │ 6,3 │ 7,3 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,2 │ 1,2 │ 2,2 │ 3,2 │ 4,2 │ 5,2 │ 6,2 │ 7,2 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,1 │ 1,1 │ 2,1 │ 3,1 │ 4,1 │ 5,1 │ 6,1 │ 7,1 │
# ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
# │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │ {:} │
# │ 0,0 │ 1,0 │ 2,0 │ 3,0 │ 4,0 │ 5,0 │ 6,0 │ 7,0 │
# └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
    else:
        if compact:
            template = """# {}
#    +---+---+---+---+---+---+---+---+
#  7 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  6 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  5 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  4 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  3 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  2 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  1 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
#  0 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|{:}|
#    +---+---+---+---+---+---+---+---+
# y/x  0   1   2   3   4   5   6   7"""
        else:
            template = """# {}
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,7 | 1,7 | 2,7 | 3,7 | 4,7 | 5,7 | 6,7 | 7,7 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,6 | 1,6 | 2,6 | 3,6 | 4,6 | 5,6 | 6,6 | 7,6 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 7,5 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,4 | 1,4 | 2,4 | 3,4 | 4,4 | 5,4 | 6,4 | 7,4 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,3 | 1,3 | 2,3 | 3,3 | 4,3 | 5,3 | 6,3 | 7,3 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,2 | 1,2 | 2,2 | 3,2 | 4,2 | 5,2 | 6,2 | 7,2 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,1 | 1,1 | 2,1 | 3,1 | 4,1 | 5,1 | 6,1 | 7,1 |
# +-----+-----+-----+-----+-----+-----+-----+-----+
# | {:} | {:} | {:} | {:} | {:} | {:} | {:} | {:} |
# | 0,0 | 1,0 | 2,0 | 3,0 | 4,0 | 5,0 | 6,0 | 7,0 |
# +-----+-----+-----+-----+-----+-----+-----+-----+"""
    # board the board string
    coords = [(x,7-y) for y in range(8) for x in range(8)]
    cells = []
    for xy in coords:
        if xy not in board_dict:
            cells.append("   ")
        else:
            cells.append(str(board_dict[xy])[:3].center(3))
    # print it
    print(template.format(message, *cells), **kwargs)


# def closest(ntuple, whites, number_of_whites):
#     overall_close = dict() # the closest for each x 
#     for piece in whites:
#         x = piece[1]
#         y = piece[2]
#         distances = set() # all distances from one piece to possible positions
#         closest_position = set()
#         for n in range(number_of_whites):
#             distances.add(euclideanDistance(x,y,ntuple[n][0],ntuple[n][1]))
#         for n in range(number_of_whites):
#             if(euclideanDistance(x,y,ntuple[n][0],ntuple[n][1])==min(distances)):
#                 closest_position = (ntuple[n][0],ntuple[n][1])
#                 overall_close[(x,y)] = closest_position
#     print(overall_close) 
#     return overall_close

# def closest(mintuple, whites, number_of_whites):
#     overall_close = dict()

#     for pos in mintuple:
#         distances = set()
#         for piece in whites:
#             x = piece[1]
#             y = piece[2]
#             distances.add(euclideanDistance(x,y,pos[0],pos[1]))
#         for piece in whites:
#             x = piece[1]
#             y = piece[2]
#             if(euclideanDistance(x,y,pos[0],pos[1])==min(distances)):
#                 #overall_close[(x,y)] = (pos[0],pos[1])
#                 overall_close[(pos[0],pos[1])] = (x,y)
                
#     print(overall_close)
#     return(overall_close)