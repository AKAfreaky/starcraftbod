#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

# enum for unit types
from jnibwapi.types.UnitType import UnitTypes

class Military(Behaviour):
    """ Contains behaviours and senses that are concerned with the placement
    of buildings """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           ("attack", "defend"), # behaviours
                           ("force_size", "is_attacking",
                            "hydralisk_count", "zealot_count",
                            "observer_count", "marine_medic_count",
                            "marine_medic_ratio"
                            )) # senses
        # These are behaviour variables
    
    def attack(self):
        self.log.info("ATTACK ATTACK ATTACK")
        return self.agent.BWBot.bot.militaryManager.attackEnemyBase()
    
    def defend(self):
        self.log.info("DEFEND FALL BACK")
        return self.agent.BWBot.bot.militaryManager.defend()
    
    def force_size(self):
        return self.agent.BWBot.bot.militaryManager.getForceSize()
    
    def hydralisk_count(self):
        return self.agent.BWBot.bot.militaryManager.getHydraliskCount()
    
    def is_attacking(self):
        return self.agent.BWBot.bot.militaryManager.isAttacking()
    
    def zealot_count(self):
        return self.agent.BWBot.bot.militaryManager.getZealotCount()
    
    def observer_count(self):
        return self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Protoss_Observer.ordinal(), False )
    
    def marine_medic_count(self):
        marines = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Marine.ordinal(), False )
        medics = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Medic.ordinal(), False )
        return (marines + medics)
    
    def marine_medic_ratio(self):
        marines = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Marine.ordinal(), False )
        medics = self.agent.BWBot.bot.unitManager.getUnitCount( UnitTypes.Terran_Medic.ordinal(), False )
        # Don't want to divide by zero
        if(medics == 0):
            medics = 1
        
        return (marines / medics)
        
        
    