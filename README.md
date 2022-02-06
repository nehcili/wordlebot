# wordlebot

## The game
run `python game.py`

## The bot
Using Monte-Carlo method to predict the next word to guess such that the expected resulting sample space (possible final answers) size is minimized.
- Parameters:
  - sample_limit = max size limit of possible final answers to do Monte-Carlo
  - accept_limit = max size of accept pool of words to do Monte-Carlo
- Sample usage:
```
from main import WordleBot
bot = WordleBot(sample_limit=100, accept_limit=1000) 
bot.condition({position_of_green_char: green_char}, {position_of_yellow_car: yellow_char}, set('unmatched_chars'))
print(bot.get_best_guess())
```
