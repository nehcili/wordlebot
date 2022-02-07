# wordlebot

## First word to guess
YOU SHOULD USE `ROATE` (for wordle) and 'RAISE' for (wordhoot)!!

## The game
run `python game.py`

## The bot
Using Monte-Carlo method to predict the next word to guess such that the expected resulting sample space (possible final answers) size is minimized.
- Parameters:
  - sample_limit = max size limit of possible final answers to do Monte-Carlo
  - accept_limit = max size of accept pool of words to do Monte-Carlo
- Sample usage:
```
python main.py
green: type all green letters at their position, use space ' ' for non green characters
yellow: same as green
gray: type all gray letters in a roll, no space
best_guess: result of bot's play
```
