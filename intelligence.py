#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

# enum for upgrade/tech types
from jnibwapi.types.RaceType import RaceTypes

class Intelligence(Behaviour):
    """ Contains behaviours and senses that are concerned with the 
    collection of intelligence of the map and the enemy positioning """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           ("scout_drone",), # behaviours
                           ("found_enemy_base","scouting_drone", "is_enemy_zerg",
                            "is_enemy_protoss", "is_enemy_terran")) # senses
        # These are behaviour variables
        self.isDroneScouting = False
        self.isOverlordScouting = False
    # Sends a drone to scout_drone
    def scout_drone(self):
        self.log.info("Attempting to send drone to scout.")
        if(self.agent.BWBot.bot.intelligenceManager.scoutDrone()):
            self.isDroneScouting = True
            return True
        return False
        
    def scouting_drone(self):
        return self.isDroneScouting
    
    # Have we found the enemy base yet?
    def found_enemy_base(self):
        return self.agent.BWBot.bot.intelligenceManager.foundEnemyBase()
    
    def is_enemy_zerg(self):
        return self.agent.BWBot.bot.intelligenceManager.isEnemyRace( RaceTypes.Zerg )
    
    def is_enemy_terran(self):
        return self.agent.BWBot.bot.intelligenceManager.isEnemyRace( RaceTypes.Terran )
    
    def is_enemy_protoss(self):
        return self.agent.BWBot.bot.intelligenceManager.isEnemyRace( RaceTypes.Protoss )
    
