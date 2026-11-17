
# Snake and ladder

import random

jump = {
    4:25,
    21:39,
    26:67,
    30:7,
    47:13,
    59:80,
    71:89,
    73:51,
    82:42,
    92:75,
    98:55
}
player1 = 0
player2 = 0
print("Snake and Ladder")

while(True):
    dice = random.randint(1,6)
    print(f"Player 1 Roll Dice : {dice}")
    if player1:
        if player1 + dice > 100:
            pass
        else:
            while(dice == 6):
                player1+=dice
                if player1 == 100:
                    print("Player1 Won")
                    break
                elif player1 in jump:
                    if player1 < jump[player1]:
                        print(f"Player 1 use ladder to go from {player1} to {jump[player1]}")
                    else:
                        print(f"Player 1 caught snake  to go from {player1} to {jump[player1]}")

                    player1=jump[player1]
                else:
                    print(f"Player 1 reached {player1} by double 6")
                dice = random.randint(1,6)
                print(f"Player 2 Roll Dice : {dice}")
            player1+=dice
            if player1 == 100:
                print("Player1 Won")
                break
            elif player1 in jump:
                if player1 < jump[player1]:
                    print(f"Player 1 use ladder to go from {player1} to {jump[player1]}")
                else:
                    print(f"Player 1 caught snake  to go from {player1} to {jump[player1]}")

                player1=jump[player1]
            else:
                print(f"Player 1 reached {player1}")
            
    elif player1 == 0:
        if dice == 1:
            player1 =+ 1
            print(f"Player 1 started game" )
    dice = random.randint(1,6)
    print(f"Player 2 Roll Dice : {dice}")
    if player2:
        if player2 + dice > 100:
            pass
        else:
            while(dice == 6):
                player2+=dice
                if player2 == 100:
                    print("Player2 Won")
                    break
                elif player2 in jump:
                    if player2 < jump[player2]:
                        print(f"Player 2 use ladder to go from {player2} to {jump[player2]}")
                    else:
                        print(f"Player 2 caught snake  to go from {player2} to {jump[player2]}")

                    player2=jump[player2]
                else:
                    print(f"Player 2 reached {player2} by double six")
                dice = random.randint(1,6)
                print(f"Player 2 Roll Dice : {dice}")
            player2+=dice
            if player2 == 100:
                print("Player2 Won")
                break
            elif player2 in jump:
                if player2 < jump[player2]:
                    print(f"Player 2 use ladder to go from {player2} to {jump[player2]}")
                else:
                    print(f"Player 2 caught snake  to go from {player2} to {jump[player2]}")

                player2=jump[player2]
            else:
                print(f"Player 2 reached {player2}")
    elif player2 == 0:
        if dice == 1:
            player2 =+ 1
            print(f"Player 2 started game" )

    