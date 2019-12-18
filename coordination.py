# Coordination Game
# Pieter Spronck, December 2019.

from game import Game
from bot import Bot
from settings import Settings
from os import listdir
from os.path import isfile, join
from itertools import permutations, combinations_with_replacement
import importlib
from sys import argv

NO_ERROR = 0
ILLEGAL_MOVE_B1 = 1
ILLEGAL_MOVE_B2 = 2
NO_WINNER = 3
EXCEPTIONB1 = 98
EXCEPTIONB2 = 99

def importBot( filename ):
    bots = []
    modulename = filename
    if '.' in filename:
        modulename, ext = filename.split( '.' )
        if ext != "py":
            return []
        if filename == argv[0]:
            return []
    module = importlib.import_module( modulename )
    for b in dir( module ):
        if hasattr( module, '__all__' ) and not b in module.__all__: 
            continue
        if b.startswith( '__' ) or b == 'Bot' or b == 'HumanBot': 
            continue
        cls = getattr( module, b )
        try:
            if issubclass( cls, Bot ) and cls not in bots:
                bots.append( cls )
        except TypeError:
            pass
    return bots
    
def getBots():
    bots = []
    files = listdir( '.' )
    for filename in files:
        if not isfile( filename ):
            continue
        botlist = importBot( filename )
        for b in botlist:
            if b not in bots:
                bots.append( b )
    return bots

def str_players( b1, b2 ):
    return b1.name+" vs. "+b2.name

def screen( text, settings ):
    if not settings.screenoutput:
        return
    print( text )

def play_match( b1, b2, game, settings, matchnum, fp ):
    b1.initialize( b2.id )
    b2.initialize( b1.id )
    movecount = 0
    movelist1 = []
    movelist2 = []
    error = NO_ERROR
    score = 0

    while True:
        try:
            move1 = b1.move( movelist1 )
        except Exception as e:
            error = EXCEPTIONB1
            errmsg = str( e.args )
            break
            
        if not game.legal( move1 ):
            error = ILLEGAL_MOVE_B1
            break
        
        try:
            move2 = b2.move( movelist2 )
        except Exception as e:
            error = EXCEPTIONB2
            errmsg = str( e.args )

        if not game.legal( move2 ):
            error = ILLEGAL_MOVE_B2
            break

        play = (move1, move2)
        movelist1.append( play )
        play = (move2, move1)
        movelist2.append( play )

        movecount += 1
        if game.won( move1, move2 ):
            break
            
        if movecount > settings.maxmoves:
            error = NO_WINNER
            break

    score = movecount
    if error != NO_ERROR:
        score = settings.maxmoves+1
    screen( str( matchnum )+":"+str_players( b1, b2 )+":"+str( score ), settings )
    
    b1.score += score
    b2.score += score
    b1.matches += 1
    b2.matches += 1
    
    s = str( matchnum )+","+b1.name+","
    for m in movelist1:
        s += str( m[0] )+","
    if error == EXCEPTIONB1:
        s += "Exception:"+errmsg
    if error == ILLEGAL_MOVE_B1:
        s += "Illegal move"
    if error == NO_WINNER:
        s += "Maximum moves exceeded"
    s += '\n'
    
    s += str( matchnum )+","+b2.name+","
    for m in movelist2:
        s += str( m[0] )+","
    if error == EXCEPTIONB2:
        s += "Exception:"+errmsg
    if error == ILLEGAL_MOVE_B2:
        s += "Illegal move"
    s += '\n'

    fp.write( s )

    b1.deinitialize()
    b2.deinitialize()
    
    return error

def main():
    settings = Settings()
    game = Game( settings.maxnum, settings.difference )
    fp = open( settings.outputfile, "w" )
    
    botclasses = getBots()
    bots = []
    for i in range( len( botclasses ) ):
        bots.append( botclasses[i]( i+1 ) )

    s = "maxnum,{}\ndifference,{}\n".format( settings.maxnum, settings.difference )
    fp.write( s )

    for b in bots:
        b.score = 0
        b.matches = 0

    matchups = list( combinations_with_replacement( bots, 2 ) )
    matchcount = 0
    for i in range( settings.nummatches ):
        # run matches between all pairs of bots
        for m in matchups:
            matchcount += 1 
            play_match( m[0], m[1], game, settings, matchcount, fp )
        
    for b in bots:
        s = b.name+","+str( b.score )+','+str( b.score/b.matches)
        fp.write( s+'\n' )
        print( s )
        
    fp.close()
    
if __name__ == "__main__":
    main()