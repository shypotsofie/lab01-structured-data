from pathlib import Path
import json
import xml.etree.ElementTree as ET
import yaml

ROOT = Path(__file__).parent
DATA = ROOT / "data"

def load_xml():
    root = ET.parse(DATA / "course.xml").getroot()
    return {
        "id": root.attrib["id"],
        "title": root.findtext("title"),
        "credits": int(root.findtext("credits")),
        "students": len(root.findall("./students/student")),
    }

def load_json():
    with open(DATA / "course.json", encoding="utf-8") as file:
        data = json.load(file)
    return {
        "id": data["id"],
        "title": data["title"],
        "credits": data["credits"],
        "students": len(data["students"]),
    }

def load_yaml():
    with open(DATA / "course.yaml", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return {
        "id": data["id"],
        "title": data["title"],
        "credits": data["credits"],
        "students": len(data["students"]),
    }

xml_data = load_xml()
json_data = load_json()
yaml_data = load_yaml()

print("XML:", xml_data)
print("JSON:", json_data)
print("YAML:", yaml_data)

if xml_data == json_data == yaml_data:
    print("\nRESULT: core data are equivalent")
else:
    print("\nRESULT: data mismatch")