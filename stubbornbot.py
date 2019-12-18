from game import Game
from bot import Bot
from random import randint

class StubbornBot( Bot ):
    def __init__( self, id=0, game=None ):
        super().__init__( id, game )
        self.name = "StubbornBot"
    def move( self, moves=[] ):
        if moves == []:
            return randint( 1, self.game.maxnum )
        return moves[0][0]

if __name__ == "__main__":
    b = StubbornBot()
    print( b )
    print( b.move( [] ) )
    print( b.move( [(1,2),(1,5)] ) )
