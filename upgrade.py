#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

# enum for upgrade/tech types
from jnibwapi.types.UpgradeType import UpgradeTypes
from jnibwapi.types.TechType import TechTypes

class Upgrade(Behaviour):
    """ Contains behaviours and senses that are concerned with the research of upgrades"""
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           # Behaviours
                           
                           # Zerg
                           ("upgrade_zergling_speed"    , "upgrade_hydralisk_speed",
                            "upgrade_hydralisk_range"   , "zerg_upgrade_flyer_carapace",
                            "zerg_upgrade_flyer_attacks", "upgrade_overlord_speed",
                            "zerg_upgrade_melee"        , "zerg_upgrade_ranged",
                            "zerg_upgrade_carapace"     , "upgrade_defiler_energy",
                            "upgrade_overlord_sight"    , "upgrade_queen_energy",
                            "upgrade_zergling_atk_spd"  , "upgrade_ultralisk_armor",
                            "upgrade_ultralisk_speed"   , "research_ensnare",                      
                            "research_lurker_aspect"    , "research_broodlings",
                            "research_burrow"           , "research_overlord_transport",
                            "research_plague"           , "research_consume",
                           
                            # Terran
                            "upgrade_marine_range"      , "upgrade_medic_energy",
                            "upgrade_vehicle_weapons"   , "upgrade_vehicle_armor",
                            "upgrade_ship_weapons"      , "upgrade_ship_armor",
                            "upgrade_wraith_energy"     , "upgrade_ghost_sight",
                            "upgrade_ghost_energy"      , "upgrade_infantry_weapons",
                            "upgrade_infantry_armor"    , "upgrade_vulture_speed",
                            "upgrade_goliath_range"     , "upgrade_battlecruiser_energy",
                            "upgrade_sci_vessel_energy" , "research_stimpack",
                            "research_restoration"      , "research_flare",
                            "research_wraith_cloak"     , "research_ghost_cloak",
                            "research_lockdown"         , "research_siege_mode",
                            "research_spider_mines"     , "research_yamato_gun",
                            "research_emp"              , "research_irradiate",     
                           
                            # Protoss
                            "upgrade_ground_weapons"    , "upgrade_ground_armor",
                            "upgrade_arbiter_energy"    , "upgrade_zealot_speed",
                            "upgrade_air_weapons"       , "upgrade_air_armor",
                            "upgrade_dragoon_range"     , "upgrade_scout_sight",
                            "upgrade_scout_speed"       , "upgrade_carrier_capacity",
                            "upgrade_corsair_energy"    , "upgrade_plasma_shields",
                            "upgrade_observer_speed"    , "upgrade_observer_sight",
                            "upgrade_reaver_capacity"   , "upgrade_scarab_damage",
                            "upgrade_shuttle_speed"     , "upgrade_dark_archon_energy",
                            "upgrade_templar_energy"    , "research_recall",
                            "research_stasis_field"     , "research_disruption_web",
                            "research_hallucination"    , "research_psionic_storm",
                            "research_maelstrom"        , "research_mind_control",
                             ), 
                          
                           # Senses
                           
                           # Zerg
                           ("has_zergling_speed"            , "has_hydralisk_speed",                 
                            "has_hydralisk_range"           , "has_overlord_speed",
                            "zerg_flyer_attack_level"       , "zerg_flyer_carapace_level",                             
                            "zerg_melee_level"              , "currently_upgrading_melee",
                            "zerg_ranged_level"             , "currently_upgrading_ranged",
                            "zerg_carapace_level"           , "currently_upgrading_carapace",                            
                            "has_completed_lurker_aspect"   , "has_lurker_aspect", 
                            "has_defiler_energy"            , "has_overlord_sight",
                            "has_queen_energy"              , "has_zergling_atk_spd",
                            "has_ultralisk_armor"           , "has_ultralisk_speed", 
                            "has_ensnare"                   , "has_broodlings", 
                            "has_burrow"                    , "has_overlord_transport", 
                            "has_plague"                    , "has_consume",                            
                            
                            # Terran
                            "has_marine_range"	            , "has_medic_energy",   
                            "vehicle_weapons_level"	        , "vehicle_armor_level",    
                            "ship_weapons_level"	        , "ship_armor_level",   
                            "has_wraith_energy"	            , "has_ghost_sight", 
                            "has_ghost_energy"	            , "infantry_weapons_level",  
                            "infantry_armor_level"          , "has_vulture_speed",  
                            "has_goliath_range"             , "has_battlecruiser_energy", 
                            "has_sci_vessel_energy"         , "has_stimpack",      
                            "has_restoration"               , "has_flare",   
                            "has_wraith_cloak"              , "has_ghost_cloak",  
                            "has_lockdown"                  , "has_siege_mode", 
                            "has_spider_mines"              , "has_yamato_gun",   
                            "has_emp"                       , "has_irradiate",                   
                                           
                            
                            # Protoss
                            "ground_weapons_level"          , "ground_armor_level",            
                            "has_arbiter_energy"            , "has_zealot_speed",              
                            "air_weapons_level"	            , "air_armor_level",               
                            "has_dragoon_range"	            , "has_scout_sight",               
                            "has_scout_speed"	            , "has_carrier_capacity",          
                            "has_corsair_energy"	        , "plasma_shields_level",          
                            "has_observer_speed"	        , "has_observer_sight",            
                            "has_reaver_capacity"	        , "has_scarab_damage",             
                            "has_shuttle_speed"	            , "has_dark_archon_energy",        
                            "has_templar_energy"	        , "has_recall",                    
                            "has_stasis_field"	            , "has_disruption_web",            
                            "has_hallucination"	            , "has_psionic_storm",             
                            "has_maelstrom"	                , "has_mind_control",              
                            ))
        
        # These are behaviour variables
        
        '''
        == Zerg Behaviours ==        
        '''
        
    def zerg_upgrade_flyer_attacks(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Zerg_Flyer_Attacks )
    
    def zerg_upgrade_flyer_carapace(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Zerg_Flyer_Carapace )
    
    def zerg_upgrade_ranged(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Zerg_Missile_Attacks )
    
    def zerg_upgrade_carapace(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Zerg_Carapace )
    
    def research_lurker_aspect(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Lurker_Aspect )
    
    def upgrade_zergling_speed(self):
        self.log.info("Researching zergling speed...")
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Metabolic_Boost )
    
    def upgrade_hydralisk_speed(self):
        self.log.info("Researching hydralisk speed...")
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Muscular_Augments )
    
    def upgrade_hydralisk_range(self):
        self.log.info("Researching hydralisk range...")
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Grooved_Spines )
    
    def upgrade_overlord_speed(self):
        self.log.info("Researching overlord speed...")
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Pneumatized_Carapace )
    
    def zerg_upgrade_melee(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Zerg_Melee_Attacks )
                      
    def upgrade_defiler_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Metasynaptic_Node )
    
    def upgrade_overlord_sight(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Antennae )
    
    def upgrade_queen_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Gamete_Meiosis )
    
    def upgrade_zergling_atk_spd(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Adrenal_Glands )
    
    def upgrade_ultralisk_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Chitinous_Plating )
    
    def upgrade_ultralisk_speed(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Anabolic_Synthesis )
    
    def research_ensnare(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Ensnare )
    
    def research_broodlings(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Spawn_Broodlings )
    
    def research_burrow(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Burrowing )
    
    def research_overlord_transport(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Zerg_Melee_Attacks )
    
    def research_plague(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Plague )
    
    def research_consume(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Consume )

    
    '''
    == Zerg Senses ==
    '''
   
    def zerg_flyer_attack_level(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Zerg_Flyer_Attacks )
    
    def zerg_flyer_carapace_level(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Zerg_Flyer_Carapace )
    
    def zerg_melee_level(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Zerg_Melee_Attacks )
    
    def currently_upgrading_melee(self):
        return self.agent.BWBot.bot.upgradeManager.isUpgrading( UpgradeTypes.Zerg_Melee_Attacks )
    
    def currently_upgrading_ranged(self):
        return self.agent.BWBot.bot.upgradeManager.isUpgrading( UpgradeTypes.Zerg_Missile_Attacks )
    
    def currently_upgrading_carapace(self):
        return self.agent.BWBot.bot.upgradeManager.isUpgrading( UpgradeTypes.Zerg_Carapace )

    def zerg_ranged_level(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Zerg_Missile_Attacks )
    
    def zerg_carapace_level(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Zerg_Carapace )
    
    # There's a bug in jnibwapi / bwapi that means lurker aspect is always set as completed research, which sucks.
    def has_completed_lurker_aspect(self):
        return self.agent.BWBot.bot.upgradeManager.hasLurkerAspect( True )
    
    # So we'll have to use Simon's old methods here
    def has_lurker_aspect(self):
        return self.agent.BWBot.bot.upgradeManager.hasLurkerAspect( False )
    
    def has_zergling_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metabolic_Boost ) > 0 )
    
    def has_hydralisk_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Muscular_Augments ) > 0 )
    
    def has_hydralisk_range(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Grooved_Spines ) > 0 )
    
    def has_overlord_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Pneumatized_Carapace ) > 0 )
   
    def has_defiler_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_overlord_sight(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Antennae ) > 0 )

    def has_queen_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Gamete_Meiosis ) > 0 )

    def has_zergling_atk_spd(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Adrenal_Glands ) > 0 )

    def has_ultralisk_armor(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Chitinous_Plating ) > 0 )

    def has_ultralisk_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Anabolic_Synthesis ) > 0 )

    def has_ensnare(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Ensnare ) > 0 )
                 
    def has_broodlings(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Spawn_Broodlings ) > 0 )

    def has_burrow(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Burrowing ) > 0 )

    def has_overlord_transport(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Ventral_Sacs ) > 0 )

    def has_plague(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Plague ) > 0 )

    def has_consume(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Consume ) > 0 )

    '''
    == Terran Behaviours ==
    '''
    
    def upgrade_marine_range(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.U_238_Shells )
    
    def upgrade_medic_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Caduceus_Reactor )
    
    def upgrade_vehicle_weapons(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Terran_Vehicle_Weapons )
    
    def upgrade_vehicle_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Terran_Vehicle_Plating )
    
    def upgrade_ship_weapons(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Terran_Ship_Weapons )
    
    def upgrade_ship_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Terran_Ship_Plating )
    
    def upgrade_wraith_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Apollo_Reactor )
    
    def upgrade_ghost_sight(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Ocular_Implants )
    
    def upgrade_ghost_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Moebius_Reactor )
    
    def upgrade_infantry_weapons(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Terran_Infantry_Weapons )
    
    def upgrade_infantry_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Terran_Infantry_Armor )
    
    def upgrade_vulture_speed(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Ion_Thrusters )
    
    def upgrade_goliath_range(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Charon_Boosters )
    
    def upgrade_battlecruiser_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Colossus_Reactor )
    
    def upgrade_sci_vessel_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Titan_Reactor )
    
    def research_stimpack(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Stim_Packs )
    
    def research_restoration(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Restoration )
    
    def research_flare(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Optical_Flare )
    
    def research_wraith_cloak(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Cloaking_Field )
    
    def research_ghost_cloak(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Personnel_Cloaking )
    
    def research_lockdown(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Lockdown )
    
    def research_siege_mode(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Tank_Siege_Mode )
    
    def research_spider_mines(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Spider_Mines )
    
    def research_yamato_gun(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Yamato_Gun )
    
    def research_emp(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.EMP_Shockwave )
    
    def research_irradiate(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Irradiate )

    '''
     == Terran Senses
    '''
    def has_marine_range(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_medic_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def vehicle_weapons_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) )

    def vehicle_armor_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) )

    def ship_weapons_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) )

    def ship_armor_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) )

    def has_wraith_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_ghost_sight(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_ghost_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def infantry_weapons_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) )

    def infantry_armor_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) )

    def has_vulture_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_goliath_range(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_battlecruiser_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_sci_vessel_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Metasynaptic_Node ) > 0 )

    def has_stimpack(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Stim_Packs ) > 0 )

    def has_restoration(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Restoration ) > 0 )

    def has_flare(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Optical_Flare ) > 0 )

    def has_wraith_cloak(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Cloaking_Field ) > 0 )

    def has_ghost_cloak(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Personnel_Cloaking ) > 0 )

    def has_lockdown(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Lockdown ) > 0 )

    def has_siege_mode(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Tank_Siege_Mode ) > 0 )

    def has_spider_mines(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Spider_Mines ) > 0 )

    def has_yamato_gun(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Yamato_Gun ) > 0 )

    def has_emp(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.EMP_Shockwave ) > 0 )

    def has_irradiate(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Irradiate ) > 0 )

    '''
    == Protoss Behaviours
    '''

    def upgrade_ground_weapons(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Protoss_Ground_Weapons )
    
    def upgrade_ground_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Protoss_Ground_Armor )
    
    def upgrade_arbiter_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Khaydarin_Core )
    
    def upgrade_zealot_speed(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Leg_Enhancements )
    
    def upgrade_air_weapons(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Protoss_Air_Weapons )
    
    def upgrade_air_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Protoss_Air_Armor )
    
    def upgrade_dragoon_range(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Singularity_Charge )
    
    def upgrade_scout_sight(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Apial_Sensors )
    
    def upgrade_scout_speed(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Gravitic_Thrusters )
    
    def upgrade_carrier_capacity(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Carrier_Capacity )
    
    def upgrade_corsair_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Argus_Jewel )
    
    def upgrade_plasma_shields(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Protoss_Plasma_Shields )
    
    def upgrade_observer_speed(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Gravitic_Boosters )
    
    def upgrade_observer_sight(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Sensor_Array )
    
    def upgrade_reaver_capacity(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Reaver_Capacity )
    
    def upgrade_scarab_damage(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Scarab_Damage )
    
    def upgrade_shuttle_speed(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Gravitic_Drive )
    
    def upgrade_dark_archon_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Argus_Talisman )
    
    def upgrade_templar_energy(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Khaydarin_Amulet )
    
    def research_recall(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Recall )
    
    def research_stasis_field(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Stasis_Field )
    
    def research_disruption_web(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Disruption_Web )
    
    def research_hallucination(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Hallucination )
    
    def research_psionic_storm(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Psionic_Storm )
    
    def research_maelstrom(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Maelstrom )
    
    def research_mind_control(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( TechTypes.Mind_Control )
    
    '''
    == Protoss Senses ==
    '''
    
    def ground_weapons_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Protoss_Ground_Weapons ) )

    def ground_armor_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Protoss_Ground_Armor ) )

    def has_arbiter_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Khaydarin_Core ) > 0 )

    def has_zealot_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Leg_Enhancements ) > 0 )

    def air_weapons_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Protoss_Air_Weapons ) )

    def air_armor_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Protoss_Air_Armor ) )

    def has_dragoon_range(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Singularity_Charge ) > 0 )   

    def has_scout_sight(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Apial_Sensors ) > 0 )

    def has_scout_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Gravitic_Thrusters ) > 0 )

    def has_carrier_capacity(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Carrier_Capacity ) > 0 )

    def has_corsair_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Argus_Jewel ) > 0 )

    def plasma_shields_level(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Protoss_Plasma_Shields ) )

    def has_observer_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Gravitic_Boosters ) > 0 )

    def has_observer_sight(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Sensor_Array ) > 0 )

    def has_reaver_capacity(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Reaver_Capacity ) > 0 )

    def has_scarab_damage(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Scarab_Damage ) > 0 )

    def has_shuttle_speed(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Gravitic_Drive ) > 0 )

    def has_dark_archon_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Argus_Talisman ) > 0 )

    def has_templar_energy(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( UpgradeTypes.Khaydarin_Amulet ) > 0 )

    def has_recall(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Recall ) > 0 )

    def has_stasis_field(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Stasis_Field ) > 0 )

    def has_disruption_web(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Disruption_Web ) > 0 )

    def has_hallucination(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Hallucination ) > 0 )

    def has_psionic_storm(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Psionic_Storm ) > 0 )

    def has_maelstrom(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Maelstrom ) > 0 )

    def has_mind_control(self):
        return ( self.agent.BWBot.bot.upgradeManager.getUpgradeLevel( TechTypes.Mind_Control ) > 0 )
