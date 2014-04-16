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
                            ("build_extractor"          , "send_drone_expansion", 
                            "build_expansion_hatchery"  ,
                           
                            # Zerg
                            "build_spawning_pool"   , "build_macro_hatchery",
                            "build_hydralisk_den"   , "build_evolution_chamber", 
                            "build_creep_colony"    , "build_spire",
                            "build_defiler_mound"   , "build_queens_nest",
                            "build_ultralisk_cavern", "build_nydus_canal_start",
                            "build_nydus_canal_end" , "upgrade_to_greater_spire",                        
                            "upgrade_to_lair"       , "upgrade_to_hive",
                            "upgrade_to_sunken"     , "upgrade_to_spore",
                            "infest_command_center" , # this one may get moved
                            
                            # Terran
                            "build_supply_depot"    , "build_barracks",
                            "build_academy"         , "build_armory",
                            "build_bunker"          , "build_engineering_bay",
                            "build_factory"         , "build_missle_turret",
                            "build_science_facility", "build_starport",
                            "addon_comsat"          , "addon_nuke_silo", 
                            "addon_control_tower"   , "addon_covert_ops",
                            "addon_machine_shop"    , "addon_physics_lab",
                              
                            # Protoss
                            "build_pylon"               , "build_gateway", 
                            "build_arbiter_tribunal"    , "build_citadel",
                            "build_cybernetics_core"    , "build_fleet_beacon",
                            "build_observatory"         , "build_photon_cannon",
                            "build_robotics_facility"   , "build_robotics_support_bay",
                            "build_shield_battery"      , "build_stargate",
                            "build_templar_archive"     , "build_forge"
                            ),
                            #Senses

                            #General
                            ("has_completed_extractor", "has_extractor", 
                            "check_drone_ready_expand", "expansion_count",
                            "all_extractors_completed", "extractor_count", 
                            "has_extractor_saturation", # Note: This sense can be inaccurate on some maps as
                                                        # it assumes all bases have gas which isn't always true
                           
                            # Zerg
                            "has_spawning_pool"     , "has_completed_spawning_pool", 
                            "has_hydralisk_den"     , "has_completed_hydralisk_den",
                            "has_spire"             , "has_completed_spire",
                            "has_lair"              , "has_completed_lair",
                            "has_hive"              , "has_completed_hive",
                            "hatchery_count"        , 
                            "colony_count"          , "creep_colony_count" ,
                            "sunken_count"          , "spore_count",                
                            "evo_chamber_count"     , "completed_evo_chamber_count",
                            "has_defiler_mound"     , "has_completed_defiler_mound",
                            "has_queens_nest"       , "has_completed_queens_nest",
                            "has_ultralisk_cavern"  , "has_completed_ultralisk_cavern",
                            "has_greater_spire"     , "has_completed_greater_spire",
                            
                            # Terran
                            "barracks_count"        , "completed_barracks_count",
                            "academy_count"         , "completed_academy_count", "have_free_academy",
                            "armory_count"          , "completed_armory_count",
                            "bunker_count"          , "completed_bunker_count",
                            "engineering_bay_count" , "completed_engineering_bay_count", "have_free_bay",
                            "factory_count"         , "completed_factory_count",
                            "missle_turret_count"   , "completed_missle_turret_count",
                            "science_facility_count", "completed_science_facility_count",
                            "starport_count"        , "completed_starport_count",
                            "comsat_count"          , "completed_comsat_count",
                            "nuke_silo_count"       , "completed_nuke_silo_count",
                            "control_tower_count"   , "completed_control_tower_count",
                            "covert_ops_count"      , "completed_covert_ops_count",
                            "machine_shop_count"    , "completed_machine_shop_count",
                            "physics_lab_count"     , "completed_physics_lab_count",
                            
                            # Protoss
                            "pylon_count"               , #completed pylons can be grokd from supply_count
                            "gateway_count"             , "completed_gateway_count", 
                            "forge_count"               , "completed_forge_count", "free_forge_count",
                            "arbiter_tribunal_count"    , "completed_arbiter_tribunal_count",
                            "citadel_count"             , "completed_citadel_count",
                            "cybernetics_core_count"    , "completed_cybernetics_core_count",
                            "fleet_beacon_count"        , "completed_fleet_beacon_count",
                            "observatory_count"         , "completed_observatory_count",
                            "photon_cannon_count"       , "completed_photon_cannon_count",
                            "robotics_facility_count"   , "completed_robotics_facility_count",
                            "robotics_support_bay_count", "completed_robotics_support_bay_count",
                            "shield_battery_count"      , "completed_shield_battery_count",
                            "stargate_count"            , "completed_stargate_count",
                            "templar_archive_count"     , "completed_templar_archive_count",
                            
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
    == General Senses
    '''
   
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
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Greater_Spire )
    
    def upgrade_to_lair(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Lair )
    
    def upgrade_to_hive(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Hive )

    def upgrade_to_sunken(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Sunken_Colony )
                           
    def upgrade_to_spore(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Zerg_Spore_Colony )  
    
    # this one may get moved
    def infest_command_center(self):
        print "Infesting command center not yet implemented"
        return false    
    
    '''
    == Zerg Senses ==
    '''
    
    # Number of hatcheries/lairs/hives
    def hatchery_count(self):
        hatcheries = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Hatchery.ordinal(), False )
        lairs = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Lair.ordinal(), False )
        hives = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Hive.ordinal(), False )
        
        return ( hatcheries + lairs + hives )
    
    def has_spawning_pool(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Spawning_Pool.ordinal(), False) > 0 )
    
    def has_completed_spawning_pool(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Spawning_Pool.ordinal(), True) > 0 )
    
    def evo_chamber_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Evolution_Chamber.ordinal(), False)
    
    def completed_evo_chamber_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Evolution_Chamber.ordinal(), True)
    
    def colony_count(self):
        creeps = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Creep_Colony.ordinal(), True)
        sunkens = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Sunken_Colony.ordinal(), True)
        spores = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Spore_Colony.ordinal(), True)
        
        return ( creeps + sunkens + spores )
    
    def creep_colony_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Creep_Colony.ordinal(), True)
    
    def sunken_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Sunken_Colony.ordinal(), True)
    
    def spore_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Spore_Colony.ordinal(), True)
    
    def has_hydralisk_den(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Hydralisk_Den.ordinal(), False) > 0 )
    
    def has_completed_hydralisk_den(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Hydralisk_Den.ordinal(), True) > 0 )
    
    def has_spire(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Spire.ordinal(), False) > 0 )
    
    def has_completed_spire(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Spire.ordinal(), True) > 0 )
    
    def has_lair(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Lair.ordinal(), False) > 0 )
    
    def has_completed_lair(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Lair.ordinal(), True) > 0 )
    
    def has_hive(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Hive.ordinal(), False) > 0 )
    
    def has_completed_hive(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Hive.ordinal(), True) > 0 )
    
    def has_defiler_mound(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Defiler_Mound.ordinal(), False) > 0 )
    
    def has_completed_defiler_mound(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Defiler_Mound.ordinal(), True) > 0 )
    
    def has_queens_nest(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Queens_Nest.ordinal(), False) > 0 )
    
    def has_completed_queens_nest(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Queens_Nest.ordinal(), True) > 0 )
    
    def has_ultralisk_cavern(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Ultralisk_Cavern.ordinal(), False) > 0 )
    
    def has_completed_ultralisk_cavern(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Ultralisk_Cavern.ordinal(), True) > 0 )
    
    def has_greater_spire(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Greater_Spire.ordinal(), False) > 0 )
    
    def has_completed_greater_spire(self):
        return ( self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Zerg_Greater_Spire.ordinal(), True) > 0 )

    
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
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Nuclear_Silo )    
    
    def addon_control_tower(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Control_Tower )
    
    def addon_covert_ops(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Covert_Ops )
        
    def addon_machine_shop(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Machine_Shop )
    
    def addon_physics_lab(self):
        return self.agent.BWBot.bot.productionManager.produceUnit( UnitTypes.Terran_Physics_Lab )
    
    
    '''
    == Terran Senses ==
    '''
    
    def barracks_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Barracks.ordinal(), False )
    
    def completed_barracks_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Barracks.ordinal(), True )
        
    def academy_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Academy.ordinal(), False )
    
    def completed_academy_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Academy.ordinal(), True )

    def armory_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Armory.ordinal(), False )
    
    def completed_armory_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Armory.ordinal(), True )
    
    def bunker_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Bunker.ordinal(), False )
    
    def completed_bunker_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Bunker.ordinal(), True )
    
    def engineering_bay_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Engineering_Bay.ordinal(), False )
    
    def completed_engineering_bay_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Engineering_Bay.ordinal(), True )
    
    def factory_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Factory.ordinal(), False )
    
    def completed_factory_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Factory.ordinal(), True )
    
    def missle_turret_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Missle_Turret.ordinal(), False )
    
    def completed_missle_turret_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Missle_Turret.ordinal(), True )
    
    def science_facility_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Science_Facility.ordinal(), False )
    
    def completed_science_facility_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Science_Facility.ordinal(), True )
    
    def starport_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Starport.ordinal(), False )
    
    def completed_starport_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Starport.ordinal(), True )
    
    def comsat_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Comsat_Station.ordinal(), False )
    
    def completed_comsat_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Comsat_Stations.ordinal(), True )
    
    def nuke_silo_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Nuclear_Silo.ordinal(), False )
    
    def completed_nuke_silo_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Nuclear_Silo.ordinal(), True )
    
    def control_tower_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Control_Tower.ordinal(), False )
    
    def completed_control_tower_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Control_Tower.ordinal(), True )
    
    def covert_ops_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Covert_Ops.ordinal(), False )
    
    def completed_covert_ops_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Covert_Ops.ordinal(), True )
    
    def machine_shop_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Machine_Shop.ordinal(), False )
    
    def completed_machine_shop_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Machine_Shop.ordinal(), True )
    
    def physics_lab_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Physics_Lab.ordinal(), False )
    
    def completed_physics_lab_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Physics_Lab.ordinal(), True )
    
    def have_free_bay(self):
        return self.agent.BWBot.bot.unitManager.haveFreeUnitofType( UnitTypes.Terran_Engineering_Bay.ordinal() )
    
    def have_free_academy(self):
        return self.agent.BWBot.bot.unitManager.haveFreeUnitofType( UnitTypes.Terran_Academy.ordinal() )
    
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
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Pylon.ordinal(), False )
    
    def gateway_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Gateway.ordinal(), False )
    
    def completed_gateway_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Gateway.ordinal(), True )
    
    def forge_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Forge.ordinal(), False )
    
    def completed_forge_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Forge.ordinal(), True )
    
    def free_forge_count(self):
        return self.agent.BWBot.bot.buildingManager.getFreeForgeCount()
    
    def arbiter_tribunal_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Arbiter_Tribunal.ordinal(), False )
    
    def completed_arbiter_tribunal_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Arbiter_Tribunal.ordinal(), True )
    
    def citadel_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Citadel_of_Adun.ordinal(), False )
    
    def completed_citadel_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Citadel_of_Adun.ordinal(), True )
    
    def cybernetics_core_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Cybernetics_Core.ordinal(), False )
    
    def completed_cybernetics_core_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Cybernetics_Core.ordinal(), True )
    
    def fleet_beacon_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Fleet_Beacon.ordinal(), False )
    
    def completed_fleet_beacon_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Fleet_Beacon.ordinal(), True )
    
    def observatory_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Observatory.ordinal(), False )
    
    def completed_observatory_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Observatory.ordinal(), True )
    
    def photon_cannon_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Photon_Cannon.ordinal(), False )
    
    def completed_photon_cannon_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Photon_Cannon.ordinal(), True )
    
    def robotics_facility_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Robotics_Facility.ordinal(), False )
    
    def completed_robotics_facility_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Robotics_Facility.ordinal(), True )

    def robotics_support_bay_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Robotics_Support_Bay.ordinal(), False )

    def completed_robotics_support_bay_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Robotics_Support_Bay.ordinal(), True )

    def shield_battery_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Shield_Battery.ordinal(), False )

    def completed_shield_battery_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Shield_Battery.ordinal(), True )

    def stargate_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Stargate.ordinal(), False )

    def completed_stargate_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Stargate.ordinal(), True )

    def templar_archive_count(self):
		return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Templar_Archives.ordinal(), False )

    def completed_templar_archive_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Templar_Archives.ordinal(), True )

    
    
    
