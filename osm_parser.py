import xml.etree.ElementTree
import xml.etree.ElementTree as ET

way_types = ['service', 'residential', 'tertiary', 'motorway',
             'trunk', 'primary', 'secondary', 'tertiary',
             'motorway_link', 'trunk_link', 'primary_link', 'secondary_link',
             'tertiary_link', 'footway']

railway_types = []

def get_attr(element, key):
    for i in element.items():
        if i[0] == key:
            return i

def get_bounds(tree):
    element = tree.getroot().find("bounds")
    bounds = {}
    bounds["minlat"] = float(get_attr(element, "minlat")[1])
    bounds["maxlat"] = float(get_attr(element, "maxlat")[1])
    bounds["minlon"] = float(get_attr(element, "minlon")[1])
    bounds["maxlon"] = float(get_attr(element, "maxlon")[1])
    # bounds["minlon"] = 36.7767
    # bounds["maxlon"] = 38.7048
    # bounds["minlat"] = 55.2720
    # bounds["maxlat"] = 56.2738

    bounds["delt_lat"] = bounds["maxlat"] - bounds["minlat"]
    bounds["delt_lon"] = bounds["maxlon"] - bounds["minlon"]
    return bounds

def get_ways(tree):
    elements:[xml.etree.ElementTree.Element] = tree.getroot().findall("way")
    ways = []
    for way in elements:
        tags = way.findall("tag")
        for tag in tags:
            if get_attr(tag, 'k')[1] == 'highway' and get_attr(tag, 'v')[1] in way_types:
                ways.append(way)
                break
            elif get_attr(tag, 'k')[1] == 'railway':
                ways.append(way)
                break
    return ways

def get_nodes(tree):
    elements = tree.getroot().findall("node")
    nodes = {}
    for node in elements:
        id = get_attr(node, 'id')
        nodes[id[1]] = node
    return nodes

def get_points(ways, nodes):
    points = []
    for way in ways:
        nds = way.findall("nd")
        points.append({"nodes": []})
        for nd in nds:
            ref = get_attr(nd, 'ref')
            node = nodes[ref[1]]
            lat = get_attr(node, 'lat')
            lon = get_attr(node, 'lon')
            points[-1]["nodes"].append({"lat":float(lat[1]),
                                        "lon":float(lon[1])})
    return points

def get_tree(file):
    return ET.parse(file)
