ticTac = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

turn = 9
while True:
    turn -= 1
# Title
    print("____________________________")
    print("\t  TIC-TAC-TOE!")
# Board
    for x in ticTac:
        print("\n\t" + str(x))

# Game-------------------------------------------------------------------
    while True:
        if turn % 2 == 0:
            print("PLAYER 1")
            pic = "X"
            try:
                row = int(input("Row: ")) - 1
                col = int(input("Col: ")) - 1
            except ValueError:
                print("ValueError: *Invalid Input*")
        else:
            print("PLAYER 2")
            pic = "O"
            try:
                row = int(input("Row: ")) - 1
                col = int(input("Col: ")) - 1
            except ValueError:
                print("ValueError: *Invalid Input*")
        try:
            if ticTac[row][col] == ' ':
                ticTac[row][col] = pic
                break
        except IndexError:
            print("IndexError: *Row and/or Column out of Range*")
        except NameError:
            print("NameError: *Invalid Input*")

# No winner
    if turn == 0:
        print("____________________________")
        print("       NO WINNER GAME OVER")
        for x in ticTac:
            print("\n\t" + str(x))
        break

# Win condition check
# Row check
    if ticTac[row].count(pic) == 3:
        print("____________________________")
        print("\t    "+pic+" WON!!!")
        for x in ticTac:
            print("\n\t" + str(x))
        break

# Column check
    col_win = 0
    for y in range(len(ticTac)):
        col_win = col_win + ticTac[y][col].count(pic)

    if col_win == 3:
        print("____________________________")
        print("\t    "+pic+" WON!!!")
        for x in ticTac:
            print("\n\t" + str(x))
        break

# Diagnal check
    if pic == ticTac[0][0] and pic == ticTac[1][1] and pic == ticTac[2][2]:
        print("____________________________")
        print("\t    "+pic+" WON!!!")
        for x in ticTac:
            print("\n\t" + str(x))
        break
    if pic == ticTac[0][2] and pic == ticTac[1][1] and pic == ticTac[2][0]:
        print("____________________________")
        print("\t    "+pic+" WON!!!")
        for x in ticTac:
            print("\n\t" + str(x))
        break
