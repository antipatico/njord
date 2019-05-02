import json
import random
from .exceptions import *
from urllib import request
from pprint import pprint

API_URL="https://airvpn.org/api/?service=status&format=json"

def get_api_data(filein):
    if filein:
        try:
            with open(filein, "r") as f:
                return json.load(f)
        except:
            raise JsonParseException("Can't load JSON from file")

    try:
        req = request.Request(API_URL)
        resp = request.urlopen(req)
        if resp.getcode() != 200:
            raise ConnectionException("API server returned bad HTTP status code: {}" % resp.getcode())
        encoding = resp.headers.get_content_charset() or "utf-8"
        jstr = resp.read().decode(encoding)
        resp.close()
    except Exception as e:
        raise ConnectionException("Can't connect to the AirVPN API server:\n{}" % str(e))
    try:
        return json.loads(jstr)
    except:
        raise JsonParseException("Can't parse JSON from AirVPN")
    

def selserv(best, country, continent, filein):
    # 1. Retrieve and parse API data
    data = get_api_data(filein)
    
    # 2. Crunch the data
    if country:
        try:
            cdata = next(cdata for cdata in data["countries"] if cdata["country_code"] == country)
        except:
            raise InvalidCountryException([ country["country_code"] for country in data["countries"] ])
        pool = [ server for server in data["servers"] if server["country_code"] == country ]
        best_name = cdata["server_best"]
    elif continent:
        try:
            cdata = next(cdata for cdata in data["continents"] if cdata["public_name"] == continent)
        except:
            raise InvalidContinentException([ continent["public_name"] for continent in data ["continents"] ])
        pool = [ server for server in data["servers"] if server["continent"] == continent ]
        best_name = cdata["server_best"]
    else:
        pool = data["servers"]
        best_name = data["planets"][0]["server_best"]

    # 3. Return the results
    if best:
        return next(server["ip_v4_in2"] for server in data["servers"] if server["public_name"] == best_name)
    else: 
        return random.choice(pool)["ip_v4_in2"]
