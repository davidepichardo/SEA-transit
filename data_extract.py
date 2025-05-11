from onebusaway import OneBusAwaySDK
import onebusaway
import pandas as pd
import os 
import json 
from datetime import datetime

client = OneBusAwaySDK(
    api_key = "456bef3e-7009-4edd-aced-28993f1fdb96",
)

agencies = client.agencies_with_coverage.list() 

def build_agency_map():
    agencyToID = {}
    for agency in agencies:
        agency_id = agency.id
        agency_name = agency.name
        agencyToID[agency_name] = agency_id 
    return agencyToID

agency_map = build_agency_map() 

for id in agency_map.values():
    routeIDs = client.route_ids_for_agency.list(id)
    stopIDs = client.stop_ids_for_agency.list(id)

def get_trip_details():
    routeIDs = client.route_ids_for_agency.list(agency_id)    