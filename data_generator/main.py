#!/usr/bin/env python3
import json

map_data = []
live_data_file = open("state_district_wise.json", "r")
coord_file = open("coord.json", "r")
map_file = open("../data/heat.json", "w+")

data = json.load(live_data_file)
coord = json.load(coord_file)
try:
    for state in data:
        for district in data[state]["districtData"]:
            if district == "Unknown":
                continue
            ans = coord[district]
            map_data.append({"lat":ans["lat"], "lng":ans["lng"], "count":data[state]["districtData"][district]["active"]})
finally:
    map_file.write(json.dumps(map_data))
    coord_file.close()
    map_file.close()
    live_data_file.close()