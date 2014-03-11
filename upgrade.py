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
        Behaviour.__init__(self, agent,# Behaviours
                           ("upgrade_zergling_speed", #Zerg
                            "upgrade_hydralisk_speed",
                            "upgrade_hydralisk_range",
                            "zerg_upgrade_flyer_attacks", "zerg_upgrade_flyer_carapace",
                            "upgrade_overlord_speed",
                            "zerg_upgrade_melee",
                            "zerg_upgrade_ranged",
                            "zerg_upgrade_carapace",
                            "research_lurker_aspect", 
                            "upgrade_ground_weapons","upgrade_ground_armor"), # Protoss
                           # Senses
                           ("has_zergling_speed", #Zerg
                            "has_hydralisk_speed",
                            "has_hydralisk_range",
                            "zerg_flyer_attack_level", "zerg_flyer_carapace_level",
                            "zerg_melee_level", "currently_upgrading_melee",
                            "zerg_ranged_level", "currently_upgrading_ranged",
                            "zerg_carapace_level", "currently_upgrading_carapace",
                            "has_overlord_speed",
                            "has_completed_lurker_aspect", "has_lurker_aspect",
                            "ground_weapons_level", "ground_armor_level")) # Protoss
        # These are behaviour variables
        
    def zerg_flyer_attack_level(self):
        return self.agent.BWBot.bot.upgradeManager.getZergFlyerAttackLevel()
    
    def zerg_upgrade_flyer_attacks(self):
        return self.agent.BWBot.bot.upgradeManager.upgradeAirFlyerAttack()
    
    def zerg_upgrade_flyer_carapace(self):
        return self.agent.BWBot.bot.upgradeManager.upgradeAirFlyerCarapace()
    
    def zerg_flyer_carapace_level(self):
        return self.agent.BWBot.bot.upgradeManager.getZergFlyerCarapaceLevel()

    def zerg_melee_level(self):
        return self.agent.BWBot.bot.upgradeManager.getZergMeleeLevel()
    
    def zerg_upgrade_melee(self):
        return self.agent.BWBot.bot.upgradeManager.upgradeMelee()
    
    def currently_upgrading_melee(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradingMelee()
    
    def zerg_upgrade_ranged(self):
        return self.agent.BWBot.bot.upgradeManager.upgradeRanged()
    
    def currently_upgrading_ranged(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradingRanged()
    
    def zerg_upgrade_carapace(self):
        return self.agent.BWBot.bot.upgradeManager.upgradeCarapace()
    
    def currently_upgrading_carapace(self):
        return self.agent.BWBot.bot.upgradeManager.getUpgradingCarapace()

    def zerg_ranged_level(self):
        return self.agent.BWBot.bot.upgradeManager.getZergRangedLevel()

    def zerg_carapace_level(self):
        return self.agent.BWBot.bot.upgradeManager.getZergCarapaceLevel()
    
    def has_completed_lurker_aspect(self):
        return self.agent.BWBot.bot.upgradeManager.hasLurkerAspect(True)
    
    def has_lurker_aspect(self):
        return self.agent.BWBot.bot.upgradeManager.hasLurkerAspect(False)
    
    def research_lurker_aspect(self):
        return self.agent.BWBot.bot.upgradeManager.researchLurkerAspect()
    
    def upgrade_zergling_speed(self):
        self.log.info("Researching zergling speed...")
        return self.agent.BWBot.bot.upgradeManager.upgradeZerglingSpeed()
    
    def upgrade_hydralisk_speed(self):
        self.log.info("Researching hydralisk speed...")
        return self.agent.BWBot.bot.upgradeManager.upgradeHydraliskSpeed()
    
    def upgrade_hydralisk_range(self):
        self.log.info("Researching hydralisk range...")
        return self.agent.BWBot.bot.upgradeManager.upgradeHydraliskRange()
    
    def upgrade_overlord_speed(self):
        self.log.info("Researching overlord speed...")
        return self.agent.BWBot.bot.upgradeManager.upgradeOverlordSpeed()
    
    def has_zergling_speed(self):
        return self.agent.BWBot.bot.upgradeManager.hasZerglingSpeed()
    
    def has_hydralisk_speed(self):
        return self.agent.BWBot.bot.upgradeManager.hasHydraliskSpeed()
    
    def has_hydralisk_range(self):
        return self.agent.BWBot.bot.upgradeManager.hasHydraliskRange()
    
    def has_overlord_speed(self):
        return self.agent.BWBot.bot.upgradeManager.hasOverlordSpeed()
    
    '''
        Protoss!    
    '''
    
    def upgrade_ground_weapons(self):
        return self.agent.BWBot.bot.upgradeManager.upgrade( UpgradeTypes.Protoss_Ground_Weapons )
    
    def ground_weapons_level(self):
        return self.agent.BWBot.bot.upgradeManager.getGroundWeaponsLevel()

    def upgrade_ground_armor(self):
        return self.agent.BWBot.bot.upgradeManager.upgradeGroundArmor()
    
    def ground_armor_level(self):
        return self.agent.BWBot.bot.upgradeManager.getGroundArmorLevel()
