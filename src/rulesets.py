
def is_core_composite_or_plate(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data.get("type") == "armor"
            and data["system"].get("group") in ["composite", "plate"]
            and
            data["system"].get("level", {}).get("value") <= 5
            and
            not set(data["system"].get("traits", {}).get("value", [])) & {"bomb", "magical", "intelligent"}
        )
    )

def is_ammunition(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("category") == "ammo"
            and 
            data["system"].get("level", {}).get("value") <= 5
            and
            "magical" not in data["system"].get("traits", {}).get("value")
        )
    )

def is_shield(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
                data.get("type") == "shield"
                and 
                data["system"].get("level", {}).get("value") <= 5
        )
    )

def is_rune(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("usage", {}).get("value") == "etched-onto-a-weapon"
            and
            data["system"].get("level", {}).get("value") <= 2
        )
    )

def is_talisman(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("category") == "talisman"
            and
            data["system"].get("level", {}).get("value") <= 2
        )
    )

def is_consumable_below_level_five(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data.get("type") == "consumable"
            and
            data["system"].get("level", {}).get("value") <= 5
        )
    )

def is_consumable_above_level_five(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data.get("type") == "consumable"
            and
            data["system"].get("level", {}).get("value") > 5
            and
            data["system"].get("level", {}).get("value") <= 10
        )
    )

def is_wand(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            "wand" in data["system"].get("traits", {}).get("value")
            and
            data["system"].get("level", {}).get("value") <= 5
        )
    )

def is_staff(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            "staff" in data["system"].get("traits", {}).get("value")
            and
            data["system"].get("level", {}).get("value") <= 5
        )
    )

def is_martial_weapon(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("category") == "martial"
            and
            data["system"].get("level", {}).get("value") <= 5
            and
            not set(data["system"].get("traits", {}).get("value", [])) & {"bomb", "magical", "intelligent"}
        )
    )

def is_simple_weapon(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("category") == "simple"
            and
            data["system"].get("level", {}).get("value") <= 5
            and
            not set(data["system"].get("traits", {}).get("value", [])) & {"bomb", "divine", "unholy", "magical", "intelligent"}

        )
    )

def is_bladed_weapon(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("group") in ["axe", "flail", "polearm", "knife", "sword", "spear"]
            and
            data["system"].get("level", {}).get("value") <= 5
        )
    )

def is_armor(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data.get("type") == "armor"
            and
            data["system"].get("level", {}).get("value") <= 5
            and 
            data["system"].get("category") != "light-barding"
            and 
            data["system"].get("category") != "heavy-barding"
        )
    )

def is_barding(data):
    return (
        (
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder Player Core"
            or
            data.get("system", {}).get("publication", {}).get("title") == "Pathfinder GM Core"
        )
        and 
        (
            data["system"].get("category") == "light-barding"
            or
            data["system"].get("category") == "heavy-barding"
        )
    )

# Oils
# Barding