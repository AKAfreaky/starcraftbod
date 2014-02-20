#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

class Production(Behaviour):
    """ Contains behaviours and senses that are concerned with the macro side
    of StarCraft. This includes producing drones, mining minerals, collecting gas
    and handling expansions. """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           ("spawn_drone", "spawn_overlord", "spawn_zerglings",
                            "spawn_hydralisk", "spawn_mutalisk", "spawn_lurker",
							"train_SCV"), # behaviours
                           ("larvae_count", "overlords_morphing")) # senses
        # These are behaviour variables
    
	'''
	 Zerg Units
	'''
	
    def spawn_drone(self):
        return self.agent.BWBot.bot.productionManager.spawnDrone()
    
    def spawn_zerglings(self):
        #self.log.info("Spawning lings...")
        return self.agent.BWBot.bot.productionManager.spawnZerglings()
    
    def spawn_hydralisk(self):
        #self.log.info("Spawning hydra.")
        return self.agent.BWBot.bot.productionManager.spawnHydralisk()
    
    def spawn_mutalisk(self):
        #self.log.info("Spawning muta.")
        return self.agent.BWBot.bot.productionManager.spawnMutalisk()
    
    def spawn_lurker(self):
        self.log.info("Spawning Lurker.")
        return self.agent.BWBot.bot.productionManager.spawnLurker()
    
    def spawn_overlord(self):
        #self.log.info("Spawning overlord.")
        return self.agent.BWBot.bot.productionManager.spawnOverlord()
    
    def overlords_morphing(self):
        return self.agent.BWBot.bot.productionManager.getOverlordsInProduction()
    
    def larvae_count(self):
        return self.agent.BWBot.bot.productionManager.getLarvaCount()
    	
    '''
        Terran Units
    '''
    
    def train_SCV(self):
        print "Trying to train SCV!"
        return self.agent.BWBot.bot.productionManager.trainSCV()