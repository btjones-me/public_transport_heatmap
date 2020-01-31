import os
from datetime import datetime
from pprint import pprint
import googlemaps

key = os.environ['GOOGLE_DIRECTIONS_KEY']
gmaps = googlemaps.Client(key=key)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
home = '20, Grove Hall Court, NW8 9NR'
home_geo = gmaps.geocode(home)
home_latlng = {'lat': 51.52976, 'lng': -0.17746}

departure_time = pd.datetime(2020, 1, 21, 8, 13, 51, 532513)



directions_dict = {}

for i in range(10):
    directions_dict[i] = {'json here': 'and here'}

def get_directions(lat, lng, home, departure_time):
    directions = gmaps.directions(home,
                     {'lat': lat, 'lng': lng},
                     mode="transit",
                     departure_time=departure_time)
    return directions


distance = df.apply(lambda x: get_directions(x['Latitude'], x['Longitude'],
                                               home=home_latlng,
                                               departure_time=departure_time),
                                            axis=1)

# get_data


