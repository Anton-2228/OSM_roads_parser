import sys

from osm_parser import get_tree, get_bounds, get_ways, get_nodes, get_points
from render import render

if __name__ == "__main__":
    args = sys.argv
    # osm_file = args[1]
    # output_file = args[2]
    osm_file = "SPB.osm"
    output_file = "map.png"
    tree = get_tree(osm_file)
    bounds = get_bounds(tree)
    ways = get_ways(tree)
    nodes = get_nodes(tree)
    points = get_points(ways, nodes)
    render(output_file, points, bounds)
