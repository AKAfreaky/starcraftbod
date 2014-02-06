#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

class Building(Behaviour):
    """ Contains behaviours and senses that are concerned with the placement
    of buildings """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           ("build_spawning_pool", "build_extractor",
                            "build_macro_hatchery", "build_hydralisk_den",
                            "build_evolution_chamber", "build_creep_colony", 
                            "send_drone_expansion", "build_expansion_hatchery",
                            "build_spire", "upgrade_to_lair", "upgrade_to_sunken"), # behaviours
                           ("has_completed_extractor", "has_extractor",
                            "has_spawning_pool", "has_completed_spawning_pool", 
                            "has_hydralisk_den", "has_completed_hydralisk_den",
                            "has_spire", "has_completed_spire",
                            "has_lair", "has_completed_lair",
                            "hatchery_count", "check_drone_ready_expand",
                            "colony_count", "creep_colony_count" , "expansion_count", "sunken_count",
                            "all_extractors_completed", "extractor_count", "has_extractor_saturation",
                            "evo_chamber_count", "completed_evo_chamber_count"
                            )) # senses
    
    def build_macro_hatchery(self):
        self.log.info("Attempting to build a macro hatchery")
        return self.agent.BWBot.bot.buildingManager.buildMacroHatchery()
    
    def hatchery_count(self):
        return self.agent.BWBot.bot.buildingManager.getHatcheryCount()
    
    def build_spawning_pool(self):
        self.log.info("Attempting to build spawning pool")
        return self.agent.BWBot.bot.buildingManager.buildSpawningPool()
    
    def has_spawning_pool(self):
        return self.agent.BWBot.bot.buildingManager.hasSpawningPool(False)
    
    def has_completed_spawning_pool(self):
        return self.agent.BWBot.bot.buildingManager.hasSpawningPool(True)
    
    def build_hydralisk_den(self):
        self.log.info("Attempting to build hydralisk den")
        return self.agent.BWBot.bot.buildingManager.buildHydraliskDen()
    
    def build_evolution_chamber(self):
        self.log.info("Attempting to build evolution chamber")
        return self.agent.BWBot.bot.buildingManager.buildEvolutionChamber()
    
    def evo_chamber_count(self):
        return self.agent.BWBot.bot.buildingManager.getEvolutionChamberCount(False)
    
    def completed_evo_chamber_count(self):
        return self.agent.BWBot.bot.buildingManager.getEvolutionChamberCount(True)
    
    def build_creep_colony(self):
        self.log.info("Attempting to build creep colony")
        return self.agent.BWBot.bot.buildingManager.buildCreepColony()
    
    def upgrade_to_sunken(self):
        self.log.info("Attempting to upgrade to sunken colony")
        return self.agent.BWBot.bot.buildingManager.upgradeSunkenColony()
    
    def colony_count(self):
        return self.agent.BWBot.bot.buildingManager.getCompletedColonyCount()
    
    def creep_colony_count(self):
        return self.agent.BWBot.bot.buildingManager.getCompletedCreepColonyCount()
    
    def sunken_count(self):
        return self.agent.BWBot.bot.buildingManager.getSunkenColonyCount()
    
    def has_hydralisk_den(self):
        return self.agent.BWBot.bot.buildingManager.hasHydraliskDen(False)
    
    def has_completed_hydralisk_den(self):
        return self.agent.BWBot.bot.buildingManager.hasHydraliskDen(True)
    
    # Sends a drone to morph into an extractor
    def build_extractor(self):
        self.log.info("Attempting to build extractor")
        return self.agent.BWBot.bot.buildingManager.buildExtractor()
    
    # Do we have a completed extractor
    def has_completed_extractor(self):
        return self.agent.BWBot.bot.buildingManager.hasExtractor(True)
    
    # Are all extractors completed
    def extractor_count(self):
        return self.agent.BWBot.bot.buildingManager.extractorCount()
    
    # Are all extractors completed
    def all_extractors_completed(self):
        return self.agent.BWBot.bot.buildingManager.allExtractorsCompleted()
    
    # Do we have an extractor in production, or one already completed
    def has_extractor(self):
        return self.agent.BWBot.bot.buildingManager.hasExtractor(False)
    
    # Does number of extractors == number of bases?
    def has_extractor_saturation(self):
        return self.agent.BWBot.bot.buildingManager.hasExtractorSaturation()
    
    # Building expansions, need to do these in order:
    def send_drone_expansion(self):
        return self.agent.BWBot.bot.buildingManager.sendDroneToExpansionLocation()
    
    # Once send_drone_expansion has been called, check for expansionDroneReady before building expansion
    def check_drone_ready_expand(self):
        return_value = self.agent.BWBot.bot.buildingManager.expansionDroneReady()
        #if(return_value == True):
            #self.log.info("drone ready to build expansion")
        #else:
            #self.log.info("drone not ready to build expansion")
        return return_value
    
    def build_expansion_hatchery(self):
        self.log.info("building expansion ")
        return_value = self.agent.BWBot.bot.buildingManager.buildExpansionHatchery()
        self.log.info("building expansion returned " + str(return_value) )
        return return_value
    
    def expansion_count(self):
        return self.agent.BWBot.bot.buildingManager.getExpansionCount()
    
    def build_spire(self):
        self.log.info("Attempting to build spire")
        return self.agent.BWBot.bot.buildingManager.buildSpire()
     
    def has_spire(self):
        return self.agent.BWBot.bot.buildingManager.hasSpire(False)
    
    def has_completed_spire(self):
        return self.agent.BWBot.bot.buildingManager.hasSpire(True)
    
    def upgrade_to_lair(self):
        return self.agent.BWBot.bot.buildingManager.upgradeToLair()
    
    def has_lair(self):
        return self.agent.BWBot.bot.buildingManager.hasLair(False)
    
    def has_completed_lair(self):
        return self.agent.BWBot.bot.buildingManager.hasLair(True)
    