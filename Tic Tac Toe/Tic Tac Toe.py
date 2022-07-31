"""
projekt_2: Druhý projekt do ENGETO Online Akademie

Author: Lukáš Horák
email: tatranka520@gmail.com
discord: Vypyx#2641
"""

import time
# Program přivítá uživatele a sdělí pravidla hra
print("Welcome to Tic Tac Toe")
time.sleep(2)
print("=" * 50)
print("GAME RULES:")
print("Each player can place one mark (or stone)\nper turn on the 3x3 grid.")
print("The WINNER is who succeeds in placing \nthree of their marks in a:")
print("* horizontal \n* vertical or \n* diagonal row")
print("Also note that the playspace will \nbe defined in numpad notation")
print("=" * 50)
time.sleep(2)
input("Press ENTER to continue")
print("=" * 50)
print("Alright, let's start the game!")
print("-" * 50)
time.sleep(1)
# Program načte herní plochu a hra začíná
gameboard = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
currentplayer = "O"
winconditions = {
    0: [0,1,2],
    1: [3,4,5],
    2: [6,7,8],
    3: [0,4,8],
    4: [6,4,2],
    5: [6,3,0],
    6: [7,4,1],
    7: [8,5,2]
    }
# Zde je jádro hry
while True:
    print("+---+---+---+")
    print("| " + gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8] + " |")
    print("+---+---+---+")
    print("| " + gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] + " |")
    print("+---+---+---+")
    print("| " + gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] + " |")
    print("+---+---+---+")
    print("=" * 50)
    for x in range(8): # Zde je kontrola výhry
        wincheck = []
        for y in range(3): 
            wincheck.append(gameboard[winconditions[x][y]]) 
        if wincheck[0] == wincheck[1] and wincheck[1] == wincheck[2] and wincheck[1] != " ":
            print("Congratulations, player " + currentplayer + "  won.")
            print("=" * 50)
            quit(0)
    draw_check = [] # Zde je kontrola remízy
    for z in range(9):
        if gameboard[z] != " ":
            draw_check.append(" ") 
    if len(draw_check) == 9:
        print("draw")
        print("=" * 50)
        quit(0)
    if currentplayer == "X": # Přepínání hráčů
        currentplayer = "O"
    else:
        currentplayer = "X"
    pos = int(input("Player " + currentplayer + " | Please enter your move number: ")) -1 # "Ovládání"
    if gameboard[pos] == " ":
        gameboard[pos] = currentplayer
        print("=" * 50)
    else:
        print(" Invalid position, choose again.")
