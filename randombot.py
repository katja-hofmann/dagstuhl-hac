from game import Game
from bot import Bot
from random import randint

class RandomBot( Bot ):
    def __init__( self, id=0, game=None ):
        super().__init__( id, game )
        self.name = "RandomBot"
    def move( self, moves=[] ):
        return randint( 1, self.game.maxnum )       

if __name__ == "__main__":
    b = RandomBot()
    print( b )
    print( b.move( [] ) )
