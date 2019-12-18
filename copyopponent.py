from game import Game
from bot import Bot
from random import randint

class CopyOpponentBot( Bot ):
    def __init__( self, id=0, game=None ):
        super().__init__( id, game )
        self.name = "CopyOpponentBot"
    def move( self, moves=[] ):
        if moves == []:
            return randint( 1, self.game.maxnum )
        return moves[-1][1]

if __name__ == "__main__":
    b = CopyOpponentBot()
    print( b )
    print( b.move( [] ) )
    print( b.move( [(1,2),(1,5)] ) )
