import os
import json

def create_html_vendor_table(output_file, title, columns, table_data):
    """
    Write Vendor data to HTML table file.
    """

    for column in columns:
        if column.lower() not in [key.lower() for key in table_data[0].keys()]:
            raise ValueError(f"Column '{column}' not found in table data.")

    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, "w") as html_file:
        html_file.write("")

    with open(output_file, "w") as html_file:
        html_file.write(f"<h3>{title}</h3>\n")
        html_file.write("<table>\n")
        html_file.write("    <tbody>\n")
        html_file.write("        <tr>\n")
        for column in columns:
            html_file.write(f"            <th>{column.capitalize()}</th>\n")
        html_file.write("        </tr>\n")
        for row in table_data:
            html_file.write("        <tr>\n")
            for column in columns:
                html_file.write(f"            <td>{row[column]}</td>\n")
            html_file.write("        </tr>\n")
        html_file.write("    </tbody>\n")
        html_file.write("</table>\n")