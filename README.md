# public_transport_heatmap

The start of an application to produce public transport journey times as a heatmap - interpolated from API data using a proprietary ML model.  

---
**NOTE**

Decomissioned and superceded by project on GitLab
---

London public transport heatmap displaying journey times 

WIP model that takes data from the Google Maps API for random coordinates across a city, and then uses the journey times to predict any journey time between two locations. 

Will create a heatmap of the journey times from a given location to all locations in the given city. 

Useful for deciding where to live based on journey times (not distance) from areas of interest. 

Will work in a similar way to [mapnificent](https://www.mapnificent.net/london/) which is very useful, except this will be capable of visualising an extra dimension (all journey times displayed, not slicing at a given journey time for a given location). It will also have better data, since this model takes into account average traffic on a given day of the year, all modes of public transport etc.
