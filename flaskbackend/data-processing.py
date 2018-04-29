from pymongo import MongoClient
from bson.son import SON

database = 'CrashesDB'
collection = 'crashes'

client = MongoClient()

db = client[database]

collection = db[collection]

def stuff(raw_data):
#raw_data = "(40.768890000000006, -73.96457000000001),(40.76921, -73.96535),(40.76794, -73.96625),(40.76671, -73.96717000000001),(40.76545, -73.96808),(40.7642, -73.96900000000001),(40.762950000000004, -73.96988),(40.76231000000001, -73.97035000000001),(40.762240000000006, -73.97017000000001),(40.7616, -73.96863),(40.75901, -73.97054),(40.757580000000004, -73.97159),(40.7565, -73.97237000000001),(40.7558, -73.97290000000001),(40.75527, -73.97329),(40.75462, -73.97373),(40.754020000000004, -73.97419000000001),(40.75276, -73.97511),(40.752, -73.97566),(40.75016, -73.97699),(40.74573, -73.98022),(40.74327, -73.98199000000001),(40.7408, -73.98382000000001),(40.740170000000006, -73.98426),(40.740100000000005, -73.98411)"

    processed_data = round(raw_data)



    for coords in processed_data:
        print(list(collection.find({"NUMBER OF PERSONS INJURED": "2", "CONTRIBUTING FACTOR VEHICLE 1": "Bicycle", "LAT": coords[0], "LONG": coords[1]})))


def round(raw_data):
    processed_data = []

    for coords in raw_data.split(')'):
        coords = coords.replace(',', '').replace('(', '')
        if coords[:6] != '':
            processed_data.append([
                round(float(coords[:7]), 3),
                round(float(coords[coords.find(' ') + 1: coords.find(' ') + 9]), 3)])

    return processed_data


# def fix_database():