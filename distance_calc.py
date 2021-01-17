#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:15:47 2021

@author: matthiasboeker
"""
import numpy as np 
import pandas as pd
import random
import string

def great_circle_dist(lat1, lon1, lat2, lon2):
    #Function to calculate the great circle distance
    r = 6372.8  # Earth radius in kilometers
    #Calculate the distance between longitude and latitude and transform to radian 
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    #Transform the latitude to radian
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
 
    a = np.sin(dLat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dLon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
 
    return r * c


def imp():
    #Function to import the .csv file 
    locs = pd.read_csv('geoloc.csv', decimal = ',',delimiter = ';')
    return locs

def random_loc(n):
    #Create random locations
    names = np.array([])
    long = np.array([])
    lat = np.array([])
    for i in range(n):
        #Draw the Longitude randomly from a uniform distribution
        long = np.append(long, np.random.uniform(-180.0,180.0))
        #Draw the Latitude randomly from a uniform distribution
        lat = np.append(lat, np.random.uniform(-90.0,90.0))
        #Create random strings as names 
        names = np.append(names, ''.join(random.choice(string.ascii_letters) for k in range(10)))
    dic = {'Name': names, 'Latitude': lat, 'Longitude':long}
    return pd.DataFrame(dic)
    
def calc_distances(n='import'):
    locations = None
    # Get data dependent on the input parameter
    
    if type(n) == int: 
        
        locations = random_loc(n)
        
    elif n == 'import': 
        locations = imp()
        
    else: 
        print('Wrong input! Use an integer or default')
    
    
        
    # Calculate distances for each pair 
    dist = np.array([])
    first_place = np.array([])
    second_place = np.array([])
    s = '-'
    i = 0
    j = 1
    while i < j:
        for j in range(i+1, len(locations)):
            dist = np.append(dist, great_circle_dist(locations.Latitude[i],locations.Longitude[i],locations.Latitude[j],locations.Longitude[j]))
            first_place = np.append(first_place, [locations.Name[i]])
            second_place = np.append(second_place, [locations.Name[j]])
        i = i+1
    dist =  np.around(dist,decimals = 1)
    
    #Create a DataFrame including the pairs of locations and the according distances. 
    dic =   {'Location_1': first_place,'Location_2':second_place, 'Distance': dist}
    return pd.DataFrame(dic)

# Calculate the mean squared distance for each distance
# Return the index of the closest pair to the mean distance 
def closest_to_average(locations):
    sqrt_dist = (locations.Distance-np.mean(locations.Distance))**2
    closest = np.argmin(np.array(sqrt_dist))
    return closest
        
def main():
    
    res = calc_distances(n='import')
    res_print = res.copy().sort_values('Distance')
    
    index_closest_pair = closest_to_average(res)
    
    res_print.Distance = res_print.Distance.astype(str) +' ' +'km'
    print(res_print)
    print('Average Distance: ', np.around(np.mean(res.Distance),decimals = 1),' km. ','Closest pair: ', res.iloc[index_closest_pair,0], ' - ', res.iloc[index_closest_pair,1] )

if __name__ == '__main__':
    main()