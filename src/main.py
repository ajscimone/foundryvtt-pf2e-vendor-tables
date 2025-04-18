import os

from create_vendor_tables import create_wares_from_ruleset, create_wares_from_list
from rulesets import is_shield, is_ammunition, is_rune, is_talisman, is_wand, is_staff, is_simple_weapon, is_martial_weapon, is_armor, is_consumable_below_level_five, is_consumable_above_level_five, is_barding
from attribute_lists import armor_attributes, weapon_attributes, consumable_attributes, adventure_gear_attributes

def make_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def main():
    """
    Main function to create the vendor tables.
    """
    equipment_folder = "" #TODO: change this to your path to the foundryvtt pathfinder 2e data folder for equipment
    
    output_folder = os.path.join(os.path.dirname(__file__), "..", "output")
    make_output_folder(output_folder)

    ammunition_file = os.path.join(output_folder, "ammunition.html")
    create_wares_from_ruleset(equipment_folder, ammunition_file, is_ammunition, "Ammunition", ["name", "price", "quantity", "traits"])

    armor_file = os.path.join(output_folder, "armor.html")
    create_wares_from_ruleset(equipment_folder, armor_file, is_armor, "Armor", armor_attributes)

    barding_file = os.path.join(output_folder, "barding.html")
    create_wares_from_ruleset(equipment_folder, barding_file, is_barding, "Barding", armor_attributes)

    journeyman_consumables_file = os.path.join(output_folder, "journeyman_consumables.html")
    create_wares_from_ruleset(equipment_folder, journeyman_consumables_file, is_consumable_below_level_five, "Journeyman Consumables (Below Level 5)", consumable_attributes)

    market_wares_data = os.path.join(os.path.dirname(__file__), "../data/market_wares.json")
    market_wares_file = os.path.join(output_folder, "market_wares.html")
    create_wares_from_list(equipment_folder, market_wares_file, market_wares_data, "Market Wares", adventure_gear_attributes)

    martial_weapons_file = os.path.join(output_folder, "martial_weapons.html")
    create_wares_from_ruleset(equipment_folder, martial_weapons_file, is_martial_weapon, "Martial Weapons", weapon_attributes)

    masterwork_consumables_file = os.path.join(output_folder, "masterwork_consumables.html")
    create_wares_from_ruleset(equipment_folder, masterwork_consumables_file, is_consumable_above_level_five, "Masterwork Consumables (Above Level 5)", consumable_attributes)

    shields_file = os.path.join(output_folder, "shields.html")
    create_wares_from_ruleset(equipment_folder, shields_file, is_shield, "Shields", armor_attributes)

    simple_weapons_file = os.path.join(output_folder, "simple_weapons.html")
    create_wares_from_ruleset(equipment_folder, simple_weapons_file, is_simple_weapon, "Simple Weapons", weapon_attributes)

    staffs_file = os.path.join(output_folder, "staffs.html")
    create_wares_from_ruleset(equipment_folder, staffs_file, is_staff, "Staffs", ["name", "price", "damage"])

    talismans_file = os.path.join(output_folder, "talismans.html")
    create_wares_from_ruleset(equipment_folder, talismans_file, is_talisman, "Talismans", ["name", "price"])

    thief_wares_file = os.path.join(output_folder, "thief_wares.html")
    thief_wares_data = os.path.join(os.path.dirname(__file__), "../data/thief_wares.json")
    create_wares_from_list(equipment_folder, thief_wares_file, thief_wares_data, "Thief Wares", adventure_gear_attributes)

    wands_file = os.path.join(output_folder, "wands.html")
    create_wares_from_ruleset(equipment_folder, wands_file, is_wand, "Wands", ["name", "price"])


if __name__ == "__main__":
    main()