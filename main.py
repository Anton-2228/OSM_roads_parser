import xml.etree.ElementTree as ET

def get_bounds(tree):
    element = tree.getroot().find("bounds").items()
    bounds = {}
    for i in element:
        match i[0]:
            case "minlat":
                bounds["minlat"] = float(i[1])
            case "maxlat":
                bounds["maxlat"] = float(i[1])
            case "minlon":
                bounds["minlon"] = float(i[1])
            case "maxlon":
                bounds["maxlon"] = float(i[1])
    return bounds

if __name__ == "__main__":
    tree = ET.parse("map.osm")
    bounds = get_bounds(tree)
    print(bounds)