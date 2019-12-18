from game import Game
from random import randint

class IllegalMove( Exception ):
    pass

class Bot:
    def __init__( self, id=0, game=None ):
        self.id = id # unique identifier given by the game engine
        if self.id == 0:
            self.id = randint( 1, 9999999 )
        self.game = game
        if self.game == None:
            self.game = Game()
        self.name = "Player{:03d}".format( id )
        self.history = {}

    # The initialize method is called at the start of a match.
    # opponentid is the id of the opponent.
    # game may override the game that is being played.
    def initialize( self, opponentid=0, game=None ):
        self.opponentid = opponentid
        if game != None:
            self.game = game

    # Called at the end of a match.
    def deinitialize( self ):
        pass

    # This method asks you to make a move.
    # moves is a list of tuples, which contains the list of all moves that
    # were made in the game until now. Of each tuple, the first element 
    # (index 0) is the move of the bot itself, the second element is the
    # move made by the opponent.
    def move( self, moves=[] ):
        raise NotImplementedError
        
    # This loads a history file in which every line consists of game number,
    # player name, and all the moves made. Every two lines are a game.
    # The load_history method creates a dictionary of which the key is
    # the game number, and the value is a list of tuples of all the
    # moves made. Player names are ignored. If already a history
    # is loaded, the new history is added (overriding old
    # history where game numbers overlap).
    def load_history( self, filename ):
        try:
            fp = open( filename )
            while True:
                line = fp.readline().strip()
                if line == "":
                    break
                items1 = line.split(',')
                line = fp.readline().strip()
                if line == "":
                    break
                items2 = line.split(',')
                if items1[0] != items2[0]:
                    break
                if len( items1 ) != len( items2 ):
                    break
                try:
                    key = int( items1[0] )
                except:
                    break
                movelist = []
                i = 2
                while i < len( items1 ):
                    try:
                        play = int( items1[i] ), int( items2[i] )
                    except:
                        fp.close()
                        return
                    movelist.append( play )
                    i += 1
                self.history[key] = movelist
            fp.close()
        except:
            return
    
    def __repr__( self ):
        return "Bot[#{},{}]".format( self.id, self.name )
        
    def __str__( self ):
        return self.name

if __name__ == "__main__":
    b = Bot( 1 )
    print( b )
    b.load_history( "Coordination_100_on_paper.csv" )
    print( b.history )
