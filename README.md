# dagstuhl-hac
Interface and bots for Human-AI Coordination project at Dagstuhl

This Python 3 program plays the Coordination game with bots.

Place the following files in a single folder:
coordination.py
settings.py
game.py
bot.py
coordination.ini

Add any bots that you like. Included bots (which are all stupid) are:
randombot.py
copyopponent.py
stubbornbot.py

You need at least one bot. If you want to write your own, examine one of the given bots to see how it is done. You only really need to implement the move() method, but it is a good idea to also implement __init__() to give a name to the bot.

When you run the coordination.py file, it will let all the bots in the folder play against each other. Bots also play against themselves. To control the matches, you can edit the coordination.ini file. It contains the following parameters:
nummatches = 10 (the number of matches which each bot plays against each other bot)
outputfile = coordination.csv (the name of the output file which stores all the matches)
screenoutput = False (whether or not you should screen output)
maxnum = 100 (the maximum number which is used in the coordination game)
difference = 0 (the exact difference which the bots need to achieve)
maxmoves = 100 (the maximum number of moves in each match)

At the end of a tournament, you see the total number of moves used by each bot, and the average number of moves per match. This is also stored at the end of the output file.

As far as the bot AI is concerned:

At the start of a match the initialize() method is called. It gets the opponent id, and the game which is currently played (game contains the maxnum and difference as game.maxnum and game.difference -- this is also given to the __init__() method). During a tournament, opponent ids will not change.

A move gets a list of all the moves that have been made during the match, as a list of tuples. The first value of each tuple is the move of the bot itself.

At the end of a match, deinitialize() is called.

During a tournament, the program keeps track of a bot's score in the bot itself, in attributes score and nummatches. You are, of course, not supposed to change those.
