class Game:
    def __init__( self, maxnum=100, difference=0, name="game" ):
        self.maxnum = maxnum
        self.difference = difference
        self.name = name
        
    def legal( self, value ):
        if value >= 1 and value <= self.maxnum:
            return True
        return False
    
    def won( self, p1, p2 ):
        if p1 >= 1 and p1 <= self.maxnum and abs( p1 - p2 ) == self.difference:
            return True
        return False
        
    def rules( self ):
        return self.name.upper() + "\n" + \
            "Players enter numbers between 1 and {} simultaneously.\n".format( self.maxnum ) + \
            "If the difference between the numbers is {}, the game ends.\n".format( self.difference ) + \
            "Otherwise, the game continues for a new round.\n" + \
            "The goal is to end the game as quickly as possible."
        
    def __repr__( self ):
        return "{}({},{})".format( self.name, self.maxnum, self.difference )
        
if __name__ == "__main__":
    g = Game()
    print( g )
    print( g.rules() )
