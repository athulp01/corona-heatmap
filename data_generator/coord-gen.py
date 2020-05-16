import geocoder
import json

API_KEY = "###########################"

coor_data = {}
coor_file = open("coord.json", "w+")

data = json.load(open("state_district_wise.json"))

try:
    for state in data:
        for district in data[state]["districtData"]:
            if district == "Unknown":
                continue
            query = district + "," + state
            ans = geocoder.opencage(query, key=API_KEY, no_annotations=1, pretty=1).json
            coor_data[district] = {"lat":ans["lat"], "lng":ans["lng"]}
finally:
    coor_file.write(json.dumps(coor_data))
    coor_file.close()
