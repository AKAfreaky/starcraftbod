#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# Import from the JNIBWAPI Client
from scbod import AIClient

# behaviour base for POSH behaviours
from POSH import Behaviour

import time

class BWBot(Behaviour):
    """ Utility class that establishes connection to the JNIBWAPI interface
    used for connecting to StarCraft : Brood War. """
    def __init__(self, agent):
        Behaviour.__init__(self, agent,
                           (), # behaviours
                           ("game_over", "life")) 
        # These are behaviour variables
        self.displayInfo = True
        self.bot = AIClient()
        
    def reset(self):
        AIClient.runBot(self.bot)
        self.log.info("Connected to BWAPI")
        self.log.info("Waiting for game to start...")
        while(not self.bot.isGameStarted()):
            time.sleep(1)
        return True;

    # This method is called by the scheduled POSH implementation to make sure
    # that the behaviour is OK every cycle. Returns False if everything is OK.
    # We can assign error codes or something similar.
    def check_error(self):
        return False

    # The agent has received a request for exit. Stop running everything.
    def exit_prepare(self):
        pass
    
    def game_over(self):
        if(self.bot.isGameStarted()):
            return False
        else:
            return True
    
    # Returns the life of the bot.
    #If the the game has finished, this will return false, 
    # and the bot will terminate.
    def life(self):
        if(self.bot.isGameStarted()):
            return True
        else:
            return False

    

	print "Hello World"