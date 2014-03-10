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
                           
                            # General
                            ("build_extractor","send_drone_expansion", 
                            "build_expansion_hatchery",
                           
                            # Zerg
                            "build_spawning_pool", "build_macro_hatchery",
                            "build_hydralisk_den", "build_evolution_chamber", 
                            "build_creep_colony", "build_spire",
                            "build_defiler_mound", "build_queens_nest",
                            "build_ultralisk_cavern", "build_nydus_canal_start",
                            "build_nydus_canal_end", "upgrade_to_greater_spire",                        
                            "upgrade_to_lair", "upgrade_to_hive",
                            "upgrade_to_sunken", "upgrade_to_spore",
                            "infest_command_center", # this one may get moved
                            
                            # Terran
                            "build_supply_depot", "build_barracks",
                            "build_academy", "build_armory",
                            "build_bunker", "build_engineering_bay",
                            "build_factory", "build_missle_turret",
                            "build_science_facility", "build_starport",
                            "addon_comsat", "addon_nuke_silo", 
                            "addon_control_tower", "addon_covert_ops",
                            "addon_machine_shop", "addon_physics_lab",
                              
                            # Protoss
                            "build_pylon", "build_gateway", 
                            "build_arbiter_tribunal", "build_citadel",
                            "build_cybernetics_core", "build_fleet_beacon",
                            "build_observatory", "build_photon_cannon",
                            "build_robotics_facility", "build_robotics_support_bay",
                            "build_shield_battery", "build_stargate",
                            "build_templar_archive", "build_forge"
                            ),
                            #Senses

                            #General
                            ("has_completed_extractor", "has_extractor", 
                            "check_drone_ready_expand",
                           
                            # Zerg
                            "has_spawning_pool", "has_completed_spawning_pool", 
                            "has_hydralisk_den", "has_completed_hydralisk_den",
                            "has_spire", "has_completed_spire",
                            "has_lair", "has_completed_lair",
                            "hatchery_count", 
                            "colony_count", "creep_colony_count" , "expansion_count", "sunken_count",
                            "all_extractors_completed", "extractor_count", "has_extractor_saturation",
                            "evo_chamber_count", "completed_evo_chamber_count",
                            
                            # Terran
                            "barracks_count", 
                            
                            # Protoss
                            "pylon_count", "gateway_count", "completed_gateway_count", 
                            "forge_count", "completed_forge_count", "free_forge_count"
                            ))
        
    '''
    == General Behaviours ==
    '''
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
    
    def build_spire(self):
        self.log.info("Attempting to build spire")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Spire )
    
    def build_defiler_mound(self):
        self.log.info("Attempting to build defiler mound")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Defiler_Mound )
   
    def build_queens_nest(self):
        self.log.info("Attempting to build queen's nest")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Queens_Nest )
    
    def build_ultralisk_cavern(self):
        self.log.info("Attempting to build ultralisk cavern")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Ultralisk_Cavern )
    
    def build_nydus_canal_start(self):
        self.log.info("Attempting to build start for nydus canal")
        return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Zerg_Nydus_Canal )
    
    def build_nydus_canal_end(self):
        self.log.info("Building a nydus canal end not implemented yet!")
        return false
    
    def upgrade_to_greater_spire(self):
        print "Upgrade to greater spire not yet implemented"
        return false
    
    def upgrade_to_lair(self):
        return self.agent.BWBot.bot.buildingManager.upgradeToLair()
    
    def upgrade_to_hive(self):
        print "Upgrade to hive not yet implemented"
        return false

    def upgrade_to_sunken(self):
        self.log.info("Attempting to upgrade to sunken colony")
        return self.agent.BWBot.bot.buildingManager.upgradeSunkenColony()
                           
    def upgrade_to_spore(self):
        print "Upgrade to spore colony not yet implemented"
        return false    
    
    # this one may get moved
    def infest_command_center(self):
        print "Infesting command center not yet implemented"
        return false    
    
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
    
    def build_academy(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Academy )
        
    def build_armory(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Armory )
    
    def build_bunker(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Bunker )
    
    def build_engineering_bay(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Engineering_Bay )
    
    def build_factory(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Factory )
    
    def build_missle_turret(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Missle_Turret )
    
    
    def build_science_facility(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Science_Facility )
    
    def build_starport(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Terran_Starport )
    
    def addon_comsat(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Comsat_Station )
      
    def addon_nuke_silo(self):
        print "Addons not yet implemented"
        return false    
    
    def addon_control_tower(self):
        print "Addons not yet implemented"
        return false
    
    def addon_covert_ops(self):
        print "Addons not yet implemented"
        return false
        
    def addon_machine_shop(self):
        print "Addons not yet implemented"
        return false
    
    def addon_physics_lab(self):
        print "Addons not yet implemented"
        return false
    
    
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
    
    def build_arbiter_tribunal(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Arbiter_Tribunal )
    
    def build_citadel(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Citadel_of_Adun )
    
    def build_cybernetics_core(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Cybernetics_Core )
    
    def build_fleet_beacon(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Fleet_Beacon )
    
    def build_observatory(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Observatory )
    
    def build_photon_cannon(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Photon_Cannon )
    
    def build_robotics_facility(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Robotics_Facility )
    
    def build_robotics_support_bay(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Robotics_Support_Bay )
    
    def build_shield_battery(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Shield_Battery )
    
    def build_stargate(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Stargate )
    
    def build_templar_archive(self):
		return self.agent.BWBot.bot.buildingManager.buildBuilding( UnitTypes.Protoss_Templar_Archive )
    
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
