player_one= input("Player 1 enter rock, paper or scissors: ")
player_two= input("Player 2 enter rock, paper or scissors: ")

if player_one == player_two:
	print('Tie')

if player_one =='rock':
	if player_two == 'paper' and player_two !='scissors' and player_two !='rock':
		print('Player 2 wins')
	else:
       		print('Player 1 wins')
elif player_one == 'scissors':
	if player_two =='rock'and player_two !='paper' and player_two !='scissors':
		print('Player 2 wins')
	else:
        	print('Player 1 wins')
elif player_one == 'paper':
	if player_two =='rock' and player_two !='scissors' and player_two !='paper':

		print('Player 1 wins')
    
	else:
       		print('Player 2 wins')







