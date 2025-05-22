from datetime import datetime
import data_ingest 
import data_load
import os 

def main(agency_ID):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    agency_routes = data_ingest.extract_routes(agency_ID)

    for route in agency_routes:
        route_ID = route['id']     
