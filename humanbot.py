from bot import Bot
from game import Game

class HumanBot( Bot ):
    def __init__( self ):
        super().__init__( id=0, game=None )
        self.name = "Human"
    def move( self, moves=[] ):
        while True:
            try:
                value = int( input( "\nYour move: " ) )
            except ValueError:
                print( "Please enter an integer." )
                continue
            if not self.game.legal( value ):
                print( "This is not a legal value." )
                continue
            break
        return value

if __name__ == "__main__":
    b = HumanBot()
    print( b.move( [] ) )