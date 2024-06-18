import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    # maxi = [60.1044, 30.1108]
    # mini = [59.7961, 30.5695]
    minlat = args[1]
    minlon = args[2]
    maxlat = args[3]
    maxlon = args[4]
    file = args[5]
    maxi = [maxlat, maxlon]
    mini = [minlat, minlon]

    query = f"""
    [out:xml];
    way["highway"]({minlat},{minlon},{maxlat},{maxlon});
    out body;
    >;
    out skel qt;
    """

    overpass_url = "http://overpass-api.de/api/interpreter"

    response = requests.post(overpass_url, data={'data': query})

    if response.status_code == 200:
        osm_data = response.text
        bounds = f'<bounds minlat="{minlat}" minlon="{minlon}" maxlat="{maxlat}" maxlon="{maxlon}"/>'
        insert_position = osm_data.find('>', osm_data.find('<osm')) + 1
        osm_data_with_bounds = osm_data[:insert_position] + bounds + osm_data[insert_position:]

        with open(file, "w", encoding="utf-8") as f:
            f.write(osm_data_with_bounds)
    else:
        print(f"Ошибка выполнения запроса: {response.status_code}")
        print(response.text)