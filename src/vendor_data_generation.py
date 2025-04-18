import json
import os

def create_table_data_from_list(item_list, item_properties, equipment_folder):
    equipment = []
    found_items = []
    for filename in os.listdir(equipment_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(equipment_folder, filename)
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                    if data.get("name") in item_list:
                        item = {}
                        item['_id'] = data['_id']
                        found_items.append(data["name"])
                        item["key"] = data["name"]
                        for property in item_properties:
                            if property == "name":
                                item["name"] = f'@Compendium[pf2e.equipment-srd.{data["_id"]}]{{{data["name"]}}}'
                            if property == "price":
                                price_data = data["system"].get("price", {}).get("value", {})
                                item[property] = ", ".join(f"{key}: {value}" for key, value in price_data.items())
                            if property == "quantity":
                                item[property] = data["system"].get("quantity", "N/A")
                            if property == "level":
                                item[property] = data["system"].get("level", {}).get("value", "N/A")
                        equipment.append(item)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")
    
    not_found_items = [item for item in found_items if item not in item_list]
    if not_found_items:
        raise ValueError(f"Items not found in equipment pack for pf2e: {', '.join(not_found_items)}")
    
    return sorted(equipment, key=lambda x: x["key"])

def create_table_data_from_ruleset(ruleset, item_properties, equipment_folder):
    equipment = []
    found_items = []
    for filename in os.listdir(equipment_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(equipment_folder, filename)
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                    if ruleset(data):
                        item = {}
                        item['_id'] = data['_id']
                        found_items.append(data["name"])
                        for property in item_properties:
                            if property == "name":
                                item["name"] = f'@Compendium[pf2e.equipment-srd.{data["_id"]}]{{{data["name"]}}}'
                            if property == "price":
                                price_data = data["system"].get("price", {}).get("value", {})
                                item[property] = ", ".join(f"{key}: {value}" for key, value in price_data.items())
                            if property == "level":
                                item[property] = data["system"].get("level", {}).get("value", "N/A")
                            if property == "acBonus":
                                item[property] = data["system"].get("acBonus", "N/A")
                            if property == "dexCap":
                                item[property] = data["system"].get("dexCap", "N/A")
                            if property == "checkPenalty":
                                item[property] = data["system"].get("check", {}).get("value", "N/A")
                            if property == "speedPenalty":
                                item[property] = data["system"].get("speedPenalty", "N/A")
                            if property == "strength":
                                item[property] = data["system"].get("strength", "N/A")
                            if property == "bulk":
                                item[property] = data["system"].get("bulk", {}).get("value", "N/A")
                            if property == "group":
                                item[property] = data["system"].get("group", "N/A")
                                if not item[property]:
                                    item[property] = "None"
                            if property == "traits":
                                item[property] = ", ".join(data["system"].get("traits", {}).get("value", []))
                            if property == "hardness":
                                item[property] = data["system"].get("hardness", "N/A")
                            if property == "hp":
                                item[property] = data["system"].get("hp", {}).get("value", "N/A")
                            if property == "quantity":
                                item[property] = data["system"].get("quantity", "N/A")
                            if property == "description":
                                item[property] = data["system"].get("description", {}).get("value", "N/A")
                            if property == "damage":
                                dice = data['system'].get('damage', {}).get('dice', "N/A")
                                die = data['system'].get('damage', {}).get('die', "N/A")
                                damage_type = data['system'].get('damage', {}).get('damageType', "N/A")
                                item[property] = f"@Damage[{dice}{die}[{damage_type}]]"
                            if property == "usage":
                                item[property] = data["system"].get("usage", {}).get("value", "N/A")
                        equipment.append(item)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")
    if "group" in item_properties:
        return sorted(equipment, key=lambda x: x["group"])
    if "level" in item_properties:
        return sorted(equipment, key=lambda x: x["level"])
    return sorted(equipment, key=lambda x: x["name"])