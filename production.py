#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

# enum for unit types
from jnibwapi.types.UnitType import UnitTypes

class Production(Behaviour):
    """ Contains behaviours and senses that are concerned with the macro side
    of StarCraft. This includes producing drones, mining minerals, collecting gas
    and handling expansions. """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
       Behaviour.__init__(self, agent,
                           # Behaviours
                           ("spawn_drone", "spawn_overlord", "spawn_zerglings", # Zerg
                            "spawn_hydralisk", "spawn_mutalisk", "spawn_lurker",
							"train_SCV", "train_marine", # Terran
                            "train_probe", "train_zealot" # Protoss
                            ), 
                           # Senses
                           ("larvae_count", "overlords_morphing")) # Zerg
    
    '''
        Zerg Units
	'''
	
    def spawn_drone(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Drone )
    
    def spawn_zerglings(self):
        #self.log.info("Spawning lings...")
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Zergling )
    
    def spawn_hydralisk(self):
        #self.log.info("Spawning hydra.")
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Hydralisk )
    
    def spawn_mutalisk(self):
        #self.log.info("Spawning muta.")
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Mutalisk )
    
    def spawn_lurker(self):
        self.log.info("Spawning Lurker.")
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Lurker )
    
    def spawn_overlord(self):
        #self.log.info("Spawning overlord.")
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Overlord )
    
    def overlords_morphing(self):
        return self.agent.BWBot.bot.productionManager.getOverlordsInProduction()
    
    def larvae_count(self):
        return self.agent.BWBot.bot.productionManager.getLarvaCount()
    	
    '''
        Terran Units
    '''
    
    def train_SCV(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_SCV )
    
    def train_marine(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Marine )
    
    '''
        Protoss Units
    '''
   
    def train_probe(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Probe )
    
    def train_zealot(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Zealot )
    
