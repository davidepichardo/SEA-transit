import json
from onebusaway import OnebusawaySDK
from datetime import datetime
from pathlib import Path 


client = OnebusawaySDK(
    api_key = "456bef3e-7009-4edd-aced-28993f1fdb96",
)

DATA_LAKE_ROOT = "data_lake/raw"

agency_ID = 1 
routeIDs = client.route_ids_for_agency.list(agency_ID).to_json()
stopIDs = client.stop_ids_for_agency.list(agency_ID).to_json() 

print(client.agency.retrieve(agency_ID))
def make_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True) 

def save_as_json(data, category, entity_id=None):
    """
    Saves data to a JSON file.
    data = API response data
    category = Category of data (e.g., 'routes', 'stops', etc.) 
    entity_id = Entity ID for specific metro  
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if entity_id:
        filename = f"{category}_{entity_id}_{timestamp}.json" 
    else:
        filename = f"{category}_{timestamp}.json"
    
    dir_path = f"{DATA_LAKE_ROOT}/{timestamp}/{category}"
    make_directory(dir_path)
    file_path = f"{dir_path}/{filename}" 

    with open(file_path, "w") as file:
        json.dump({
            "metadata": {
            "timestamp": datetime.now().isoformat(),  # ISO 8601 format
            "agency_id": agency_ID
            },
            "data": data
        }, file, indent=2)

def extract_data():
    """
    Extracts raw data from OneBusAway API and saves it to JSON files
    """
    routes = client.routes_for_agency.list(agency_ID).to_json()
    save_as_json(routes, "routes")

    stops = client.stops_for_agency.list(agency_ID).to_json()
    save_as_json(stops, "stops") 

    for stop in stops:
        stop_ID = stop["id"] 
        arrival_and_departure = client.arrival_and_departure.list(stop_ID).to_json()
        save_as_json(arrival_and_departure, "arrivals_and_departures", stop_ID)        

    for route in routes:
        route_id = route["id"]
        trips = client.trips_for_route.list(route_id).to_json() 
        save_as_json(trips, "trips", route_id) 
    
if __name__ == "__main__":
    extract_data() 


















    

