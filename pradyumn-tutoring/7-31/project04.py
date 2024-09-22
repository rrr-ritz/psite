"""
PROJECT: Guess the Number Game

Description:
In this project, you'll create a "Guess the Number" game. The computer will 
think of a random number from 1 to 100, and the player has to guess it. The 
game should provide hints like 'too high' or 'too low' after each guess.

Instructions (READ CAREFULLY!):
[ v1.0 ]

1. Program starts by printing an introduction message explaining the game.

2. Generate a random number between 1 and 100 (Hint: you'll have to look up 
the appropriate Python function to do this).

3. Use a while loop to allow the player to make guesses.

4. After each guess, compare the player's guess to the generated number. 
If the guess is too high, print "too high", and if it's too low, print 
"too low".

5. If the player guesses the number correctly, congratulate them and print 
the number of attempts it took.

[ v2.0 ]
6. Extend your program to allow the user to play again without 
restarting the program.

7. Track the number of games the player has won and lost, and display 
these statistics to the player when they decide to stop playing.

8. Add a feature where if the player's guess is way off (for instance, 
30 or more numbers away from the answer), the program tells them 
they're "way off".

9. Handle any edge cases, such as the user entering something that 
isn't a number.

10. Add any other features you like...always be creative.
"""