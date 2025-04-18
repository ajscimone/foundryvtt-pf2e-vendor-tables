import os
import json

from vendor_data_generation import create_table_data_from_list, create_table_data_from_ruleset
from vendor_html_table_generation import create_html_vendor_table

def create_wares_from_list(equipment_folder, output_file, input_json, table_title, item_properties):
    raw_json = {}
    with open(input_json, "r", encoding="utf-8") as f:
        raw_json = json.load(f)
    gear_key = next(iter(raw_json))
    wares = raw_json[gear_key]
    table_data = create_table_data_from_list(wares, item_properties, equipment_folder)
    create_html_vendor_table(output_file, table_title, item_properties, table_data)

def create_wares_from_ruleset(equipment_folder, output_file, ruleset, table_title, item_properties):
    table_data = create_table_data_from_ruleset(ruleset, item_properties, equipment_folder)
    create_html_vendor_table(output_file, table_title, item_properties, table_data)
