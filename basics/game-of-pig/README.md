# The Game of Pig

## Description

TODO

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Variables
* `if` and `else`
* `while`
* Functions
* Libraries
* Programs

### Performance Objectives

After completing this assignment, you should be able to:

* Write a Python script
* Generate a random number
* Ask for input
* Print output

## Details

### Deliverables

* A GitHub repo called game-of-pig containing at least:
  * This `README.md` file
  * a file called `pig.py`

### Requirements  

Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:

* If the player rolls a 1, they score nothing and it becomes the next player's turn.
* If the player rolls any other number, it is added to their turn total and the player's turn continues.
* If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.

The first player to score 100 or more points wins.

## Normal Mode

Create a program in the file `pig.py` that runs one game of Pig in the terminal. This is a two player game, so play should alternate between both players but will use the same screen.

## Hard Mode

Once the game is done, ask if the players would like to play again. Keep a record of each player's wins and let them know the number of wins for each player after each game.

## Additional Resources

* [Pig on Wikipedia](https://en.wikipedia.org/wiki/Pig_%28dice_game%29)