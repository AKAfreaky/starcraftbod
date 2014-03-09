#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

# enum for unit types
from jnibwapi.types.UnitType import UnitTypes

class Building(Behaviour):
    """ Contains behaviours and senses that are concerned with the placement
    of buildings """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           # Behaviours
                           ("build_spawning_pool", "build_extractor", # Zerg
                            "build_macro_hatchery", "build_hydralisk_den",
                            "build_evolution_chamber", "build_creep_colony", 
                            "send_drone_expansion", "build_expansion_hatchery",
                            "build_spire", "upgrade_to_lair", "upgrade_to_sunken",
                            "build_supply_depot", "build_barracks",    # Terran
                            "build_pylon", "build_gateway", "build_forge" # Protoss
                            ),
                            #Senses
                           ("has_completed_extractor", "has_extractor", # Zerg
                            "has_spawning_pool", "has_completed_spawning_pool", 
                            "has_hydralisk_den", "has_completed_hydralisk_den",
                            "has_spire", "has_completed_spire",
                            "has_lair", "has_completed_lair",
                            "hatchery_count", "check_drone_ready_expand",
                            "colony_count", "creep_colony_count" , "expansion_count", "sunken_count",
                            "all_extractors_completed", "extractor_count", "has_extractor_saturation",
                            "evo_chamber_count", "completed_evo_chamber_count",
                            "barracks_count", # Terran
                            "pylon_count", "gateway_count", "completed_gateway_count", # Protoss
                            "forge_count", "completed_forge_count", "free_forge_count"
                            ))
    
    '''
    == Zerg Behaviours ==
    '''
    
    def build_macro_hatchery(self):
        self.log.info("Attempting to build a macro hatchery")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Hatchery )
    
    def build_spawning_pool(self):
        self.log.info("Attempting to build spawning pool")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Spawning_Pool )
    
    def build_hydralisk_den(self):
        self.log.info("Attempting to build hydralisk den")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Hydralisk_Den )
    
    def build_evolution_chamber(self):
        self.log.info("Attempting to build evolution chamber")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Evolution_Chamber )
    
    def build_creep_colony(self):
        self.log.info("Attempting to build creep colony")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Creep_Colony )
    
    def upgrade_to_sunken(self):
        self.log.info("Attempting to upgrade to sunken colony")
        return self.agent.BWBot.bot.buildingManager.upgradeSunkenColony()
    
    # Sends a drone to morph into an extractor
    def build_extractor(self):
        self.log.info("Attempting to build extractor")
        return self.agent.BWBot.bot.buildingManager.buildExtractor()
    
    # Building expansions, need to do these in order:
    def send_drone_expansion(self):
        return self.agent.BWBot.bot.buildingManager.sendWorkerToExpansionLocation()
    
    # No longer needed, now worker will automatically start building once it reaches the location
    def build_expansion_hatchery(self):
        self.log.info("building expansion ")
        return_value = self.agent.BWBot.bot.buildingManager.buildExpansionHatchery()
        self.log.info("building expansion returned " + str(return_value) )
        return return_value
    
    def build_spire(self):
        self.log.info("Attempting to build spire")
        return self.agent.BWBot.bot.buildingManager.buildSpire()
    
    def upgrade_to_lair(self):
        return self.agent.BWBot.bot.buildingManager.upgradeToLair()
    
    '''
    == Zerg Senses ==
    '''
    
    def hatchery_count(self):
        return self.agent.BWBot.bot.buildingManager.getHatcheryCount()
    
    def has_spawning_pool(self):
        return self.agent.BWBot.bot.buildingManager.hasSpawningPool(False)
    
    def has_completed_spawning_pool(self):
        return self.agent.BWBot.bot.buildingManager.hasSpawningPool(True)
    
    def evo_chamber_count(self):
        return self.agent.BWBot.bot.buildingManager.getEvolutionChamberCount(False)
    
    def completed_evo_chamber_count(self):
        return self.agent.BWBot.bot.buildingManager.getEvolutionChamberCount(True)
    
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
    
    # Once send_drone_expansion has been called, check for expansionDroneReady before building expansion
    def check_drone_ready_expand(self):
        return self.agent.BWBot.bot.buildingManager.expansionDroneReady()
    
    def expansion_count(self):
        return self.agent.BWBot.bot.buildingManager.getExpansionCount()
    
    def has_spire(self):
        return self.agent.BWBot.bot.buildingManager.hasSpire(False)
    
    def has_completed_spire(self):
        return self.agent.BWBot.bot.buildingManager.hasSpire(True)
    
    def has_lair(self):
        return self.agent.BWBot.bot.buildingManager.hasLair(False)
    
    def has_completed_lair(self):
        return self.agent.BWBot.bot.buildingManager.hasLair(True)
    
    '''
    == Terran Behaviours ==
    '''
    
    def build_supply_depot(self):
         return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Supply_Depot )
    
    def build_barracks(self):
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Barracks )
    
    '''
    == Terran Senses ==
    '''
    
    def barracks_count(self):
        return self.agent.BWBot.bot.buildingManager.getBarracksCount()
    
    '''
    == Protoss Behaviours ==
    '''
    
    def build_pylon(self):
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Pylon )
    
    def build_gateway(self):
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Gateway )
    
    def build_forge(self):
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Forge )
    
    '''
    == Protoss Senses ==
    '''
    def pylon_count(self):
        return self.agent.BWBot.bot.buildingManager.getPylonCount()
    
    
    
    def gateway_count(self):
        return self.agent.BWBot.bot.buildingManager.getGatewayCount()
    
    def completed_gateway_count(self):
        return self.agent.BWBot.bot.buildingManager.getCompletedGatewayCount()
    
    
    
    def forge_count(self):
        return self.agent.BWBot.bot.buildingManager.getForgeCount()
    
    def completed_forge_count(self):
        return self.agent.BWBot.bot.buildingManager.getCompletedForgeCount()
    
    def free_forge_count(self):
        return self.agent.BWBot.bot.buildingManager.getFreeForgeCount()
