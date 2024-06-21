import sys
import time

from osm_parser import get_tree, get_bounds, get_ways, get_nodes, get_points
from render import render

if __name__ == "__main__":
    a = time.time()
    args = sys.argv
    osm_file = args[1]
    output_file = args[2]
    # osm_file = "test.osm"
    # output_file = "map.png"
    tree = get_tree(osm_file)
    b = time.time()
    bounds = get_bounds(tree)
    c = time.time()
    ways = get_ways(tree)
    d = time.time()
    nodes = get_nodes(tree)
    e = time.time()
    points = get_points(ways, nodes)
    print(len(points))
    f = time.time()
    render(output_file, points, bounds)
    g = time.time()

    all = g-a
    print(b-a)

    print(f"Время выполнения парсинга дерева: {b-a};    {(b-a)/all}%")
    print(f"Время выполнения парсинга границ: {c-b};    {(c-b)/all}%")
    print(f"Время выполнения парсинга путей: {d-c};     {(d-c)/all}%")
    print(f"Время выполнения парсинга нод: {e-d};   {(e-d)/all}%")
    print(f"Время выполнения создания точек: {f-e};     {(f-e)/all}%")
    print(f"Время рендера пикчи: {g-f};     {(g-f)/all}%")
    print(f"Итоговое время: {g-a}")
