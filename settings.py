from configparser import ConfigParser
from os.path import isfile

CONFIGFILE = 'coordination.ini'
PARAMETERS = 'parameters'
NUMMATCHES = 'nummatches'
OUTPUTFILE = 'outputfile'
SCREENOUTPUT = 'screenoutput'
MAXNUM = 'maxnum'
DIFFERENCE = 'difference'
MAXMOVES = 'maxmoves'

class Settings:
    def __init__( self ):
        self.nummatches = 10
        self.outputfile = "coordination.csv"
        self.screenoutput = True
        self.maxnum = 100
        self.difference = 0
        self.maxmoves = 100
        
        config = ConfigParser()
        if not isfile( CONFIGFILE ):
            config.add_section( PARAMETERS )
            config.set( PARAMETERS, NUMMATCHES, str( self.nummatches ) )
            config.set( PARAMETERS, OUTPUTFILE, self.outputfile )
            config.set( PARAMETERS, SCREENOUTPUT, str( self.screenoutput ) )
            config.set( PARAMETERS, MAXNUM, str( self.maxnum ) )
            config.set( PARAMETERS, DIFFERENCE, str( self.difference ) )
            config.set( PARAMETERS, MAXMOVES, str( self.maxmoves ) )
            with open( CONFIGFILE, 'w' ) as configfile:
                config.write( configfile )
            return

        config.read( CONFIGFILE )
        self.nummatches = config.getint( PARAMETERS, NUMMATCHES )
        self.outputfile = config.get( PARAMETERS, OUTPUTFILE )
        self.screenoutput = config.getboolean( PARAMETERS, SCREENOUTPUT )
        self.maxnum = config.getint( PARAMETERS, MAXNUM )
        self.difference = config.getint( PARAMETERS, DIFFERENCE )
        self.maxmoves = config.getint( PARAMETERS, MAXMOVES )
