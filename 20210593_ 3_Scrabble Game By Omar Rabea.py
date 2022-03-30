try:

    The_mechanism_of_the_game = input("Please Press Enter To Know How To Play The Game.")
    print()


    def Start_the_game():
        print()
        print('Scrabble Game : is played with the list of numbers between 1 and 9.')
        print('Each player takes turn Picking a num from the list.')
        print('Once a number has been picked, it cannot be picked again.')
        print('If a player has picked three numbers that add up to 15, that player wins the game.')
        print('However, if all the numbers are used and no player gets exactly 15, the game is a draw.')
        print()


    Start_the_game()

    The_Start_key = input("Please Press Enter To Play The Game.")
    print()

    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1 = 0
    player2 = 0



    def player1_input():
        global player1
        player1_num = int(input('Player1 please enter a number between 1 ----> 9 '))
        if 1 <= player1_num <= 9 and player1_num in list_of_numbers:
            list_of_numbers.remove(player1_num)
            player1 = player1 + player1_num
            return player1

        else:
            print('The number is not in the range pls try again')
            print()
            player1_num = int(input('Player1 pleas enter a number between 1 ----> 9 '))
            list_of_numbers.remove(player1_num)


    def player2_input():
        global player2
        player2_num = int(input('Player2 please enter a number between 1 ----> 9 '))
        if 1 <= player2_num <= 9 and player2_num in list_of_numbers:
            list_of_numbers.remove(player2_num)
            player2 = player2 + player2_num
            return player2

        else:
            print('the number is not in the range pls try again')
            print()
            player2_num = int(input('Player2 please enter a number between 1 ----> 9 '))
            list_of_numbers.remove(player2_num)


    def player_1_win():
        if player1 == 15:
            print()
            print("---Player 1 is the winner---")


    def player_2_win():
        if player2 == 15:
            print()
            print("---Player 2 is the winner---")








    def the_game():
        count=0

        for player in range(0, 3):
            print()
            print("The List Of Numbers: ", list_of_numbers)
            print()
            player1_input()
            count = count + 1

            if player1 == 15:
                print()
                print("---Player 1 is the winner---")
                break
            player2_input()
            if player2 == 15:
                print()
                print("---Player 2 is the winner---")
                break
            if count == 3:
                for i in range(0, 1):
                    print()
                    print("The List Of Numbers: ", list_of_numbers)
                    print()
                    player1_input()

                    if player1 == 15:
                        print("Player 1 is the winner")
                        break
                    player2_input()
                    player_2_win()

    the_game()

    if player1 != 15 and player2 != 15:
       print("--- Draw ---")


    while True:
        print()
        Restart_the_game = input("If You Want To Play Again\n Press enter\n if you don't type No: ")
        print()

        if Restart_the_game == 'NO' or Restart_the_game =='no' or Restart_the_game =='No' or Restart_the_game == 'No':
            print()
            print("--- Game Over ---")

            print()
            print("--- Thank You For Playing ---")
            break
        else:
            list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            player1 = 0
            player2 = 0
            the_game()





except:
    print('--- Pleas Try Again Later ---')









