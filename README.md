# foundryvtt-pf2e-vendor-tables

## How to use

This code is intended to be used with the Pathfinder 2e game system for Foundry VTT. In order to use it, you will need to change this line:

```
    equipment_folder = "" #TODO: change this to your path to the foundryvtt pathfinder 2e data folder for equipment
```

In src/main.py to point the equipments pack inside the Pathfinder 2e game system inside Foundry VTT.

Alternatively, you could also clone and use the system locally instead, which can be found [here](https://github.com/foundryvtt/pf2e) on Github.

The equipment folder is found in `packs/equipment` there and should be in a similar location on your FoundryVTT instance if you have the pathfinder 2e package installed.

At this point you can simply run python against `main.py` and generate a set of html tables based on the rule sets that I used for my own vendors.

## Rulesets

The `create_wares_from_ruleset()` function in `create_vendor_tables.py` takes a python expression that is uses to search through the equipment and include items that match those rules. The `rulesets.py` file contains some example rulesets for generating the vendor equipment to be sold by your town vendors. In my case, I was running Abomination Vaults, so I made rules for what I wanted displayed for various vendors in the town of Otari.

You can simply adjust these rulesets or make your own

## Data files

You can also feed `create_wares_from_list()` function in `create_vendor_tables.py` a json file which contains a key:array value pair where the array contains the names of the equipment you want to include in your table. The names of this equipment must match the names as they appear in the Foundryvtt Pathfinder 2e equipment pack.