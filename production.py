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
    """ Contains behaviours and senses that are concerned with the production of units """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
       Behaviour.__init__(self, agent,
                           # Behaviours
                           # Zerg
                           ("spawn_drone", "spawn_overlord", "spawn_zerglings", 
                            "spawn_hydralisk", "spawn_mutalisk", "spawn_lurker",
                            "spawn_queen", "spawn_ultralisk", "spawn_defiler",
                            "spawn_devourer", "spawn_guardian", "spawn_scourge",
                            "spawn_infested_terran",
                            # Terran
							"train_SCV", "train_marine", "train_medic", 
                            "train_firebat", "train_battlecruiser", "train_ghost",
                            "train_goliath", "train_dropship", "train_science_vessel",
                            "train_siege_tank", "train_valkyrie", "train_vulture",
                            "train_wraith",
                            # Protoss
                            "train_probe", "train_zealot", "train_archon", 
                            "train_carrier", "train_corsair", "train_dark_archon",
                            "train_dark_templar", "train_dragoon", "train_templar",
                            "train_observer", "train_reaver", "train_scout",
                            "train_shuttle", "train_arbiter"
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
    
    def spawn_queen(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Queen )
     
    def spawn_ultralisk(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Ultralisk )
    
    def spawn_defiler(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Defiler )
    
    def spawn_devourer(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Devourer )
    
    def spawn_guardian(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Guardian )
    
    def spawn_scourge(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Scourge )   
                    
    def spawn_infested_terran(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Infested_Terran )
    
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
    
    def train_medic(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Medic )
    
    def train_firebat(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Firebat )

    def train_battlecruiser(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Battlecruiser )

    def train_ghost(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Ghost )
  
    def train_goliath(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Goliath )

    def train_dropship(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Dropship )

    def train_science_vessel(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Science_Vessel )

    def train_siege_tank(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Siege_Tank_Tank_Mode )        
    
    def train_valkyrie(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Valkyrie )

    def train_vulture(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Vulture )

    def train_wraith(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Wraith )
    
    '''
        Protoss Units
    '''
   
    def train_probe(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Probe )
    
    def train_zealot(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Zealot )
    
    def train_archon(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Archon )
        
    def train_carrier(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Carrier )
        
    def train_corsair(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Corsair )
        
    def train_dark_archon(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Dark_Archon )
        
    def train_dark_templar(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Dark_Templar )

    def train_dragoon(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Dragoon )
        
    def train_templar(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_High_Templar )
        
    def train_observer(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Observer )
         
    def train_reaver(self): 
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Reaver )
        
    def train_scout(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Scout )
        
    def train_shuttle(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Shuttle )
    
    def train_arbiter(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Protoss_Arbiter )

