import sys
import json

from search.util import print_move, print_boom, print_board, place_pieces, find_killZones, kills_all_blacks
from search.util import d_comb_whites, closest, euclideanDistance
from itertools import combinations

def main():
    with open(sys.argv[1]) as file:
        data = json.load(file)
    
    board_dict = {}

    whites = data['white'] # array of arrays
    number_of_whites = 0
    for piece in whites:
        number_of_whites+=piece[0]
    print("number of whites: " + str(number_of_whites))

    blacks = data['black'] # array of arrays

    place_pieces(board_dict,whites,blacks)

    killZone = set()
    find_killZones(board_dict,whites,blacks,killZone)

    place_pieces(board_dict, whites, blacks)

    print_board(board_dict)
    print(killZone)

    # find a combination of white positions within the killzone that when they explode they kill every black piece
    # results gives us the positions for white pieces
    possible_white_positions = list(combinations(killZone, number_of_whites))
    for tupl in possible_white_positions:
        for piece in blacks:
            if ((piece[1],piece[2]) in tupl):
                possible_white_positions.remove(tupl)
                break

    combinations_success = set() # combinations of postiton that kill all blacks
    for tupl in possible_white_positions:
        if(kills_all_blacks(tupl, blacks)):
            combinations_success.add(tupl)

    print("combinations that killed all the black pieces:")
    print(combinations_success)
    print(combinations_success.issuperset({((1,1),(1,1),(1,1))}))

    for e in combinations_success:
        for n in range(number_of_whites):
            board_dict[(e[n][0],e[n][1])] = "!"
    print_board(board_dict)

    # Finally, move whites to the optimum positions in the least amount of moves
        #1st find combination that is closest
        #2nd move peices there

    comb_dsitances = set()
    for ntuple in combinations_success:
        comb_dsitances.add(d_comb_whites(ntuple, whites, number_of_whites))

    print(comb_dsitances)
    print(min(comb_dsitances))

    mintuple = tuple()
    for ntuple in combinations_success:
        if (d_comb_whites(ntuple, whites, number_of_whites)==(min(comb_dsitances))):
            mintuple = ntuple
    
    print(mintuple)
        
    #which picece is closest to which point?
    #goal_dict = closest(mintuple, whites, number_of_whites)
    goal_dict = closest(mintuple, whites)

    #last step is to actually move the pices to their optimum position and BOOM!
    endconfig = list()
    for piece in whites:
        spos = (piece[1],piece[2])
        endpos = goal_dict[(piece[1],piece[2])]
        # print("start position: {}, goal position: {}".format((piece[1],piece[2]),goal_dict[(piece[1],piece[2])]))
        # print(goal_dict[(piece[1],piece[2])][0])
        while(not(spos==endpos)):
            if(spos[0]>endpos[0] and (not(board_dict.get({(spos[0]-1, spos[1])})[0]=='b'))):
                print_move(1, spos[0], spos[1], spos[0]-1, spos[1])
                spos = (spos[0]-1, spos[1])
            if(spos[0]<endpos[0]):
                print_move(1, spos[0], spos[1], spos[0]+1, spos[1])
                spos = (spos[0]+1, spos[1])
            if(spos[1]>endpos[1]):
                print_move(1, spos[0], spos[1], spos[0], spos[1]-1)
                spos = (spos[0], spos[1]-1)
            if(spos[1]<endpos[1]):
                print_move(1, spos[0], spos[1], spos[0], spos[1]+1)
                spos = (spos[0], spos[1]+1)
        endconfig.append(spos)
    for spos in endconfig:
        print_boom(spos[0], spos[1])
    


if __name__ == '__main__':
    main()
