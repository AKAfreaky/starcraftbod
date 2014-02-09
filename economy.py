#!/usr/bin/python
# StarCraft Brood War BOD Bot

# For compatibility with Jython
from __future__ import nested_scopes
from POSH.jython_compat import *

# behaviour base for POSH behaviours
from POSH import Behaviour

class Economy(Behaviour):
    """ Contains behaviours and senses that are concerned with the macro side
    of StarCraft. This includes producing drones, mining minerals, collecting gas
    and handling expansions. """
    def __init__(self, agent):
        # initialise the behaviour by specifying that it provides the action
        # 'change_dir' and the senses 'see_cookie' and 'fail'. These have
        # to correspond to a method of the class.
        Behaviour.__init__(self, agent,
                           ("start_collecting_gas", ), # behaviours
                           ("mineral_count", "gas_count", "supply_total",
                            "supply_used", "supply_available",
                            "predicted_supply_available", 
                            "drone_count",
                            "gas_saturated")) # senses
        # These are behaviour variables
        
    def mineral_count(self):
        return self.agent.BWBot.bot.resourceManager.getMineralCount()
    
    def gas_count(self):
        return self.agent.BWBot.bot.resourceManager.getGasCount()
    
    def drone_count(self):
        return self.agent.BWBot.bot.workerManager.getWorkerCount()
    
    def gas_saturated(self):
        return (self.agent.BWBot.bot.workerManager.getGasWorkerCount() >= 3 * (self.agent.BWBot.bot.buildingManager.getExpansionCount() + 1))
    
    def supply_total(self):
        return self.agent.BWBot.bot.resourceManager.getSupplyTotal()
    
    def supply_used(self):
        return self.agent.BWBot.bot.resourceManager.getSupplyUsed()
    
    def supply_available(self):
        return self.agent.BWBot.bot.resourceManager.getSupplyAvailable()
    
    def predicted_supply_available(self):
        return self.agent.BWBot.bot.resourceManager.getPredictedSupplyAvailable()
    
    def start_collecting_gas(self):
        return self.agent.BWBot.bot.workerManager.startCollectingGas()