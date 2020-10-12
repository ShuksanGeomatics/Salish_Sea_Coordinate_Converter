#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch/Shuksan Geomatics'
__date__ = 'October 2020'
__copyright__ = 'MIT'

from pyproj import Transformer
class SalishSeaCoordConverter:
    
    def __init__(self, in_crs, out_crs, x, y):
            
        #defined Salish Sea EPSG codes...
        epsg = {'WN_HARN': 2855, 
                'WN_NAD83':2285, 
                'WN_NAD27':32048,
                'WS_HARN':2856, 
                'WS_NAD83':2286, 
                'WS_NAD27':32049,
                'UTM10N_WGS84':32610, 
                'UTM10N_NAD83':26910, 
                'UTM10N_NAD27':26710,
                'UTM10N_WGS72':32210,
                'UTM10N_HARN': 32210,
                'WGS84' :4326,
                'WGS72' : 4322
                }
        #Support conversion for any crs...If the user uses an EPSG number for the crs then use the number,
        #otherwise choose from the dictionary
        
        if type(in_crs) == str:
            self.in_epsg = epsg[in_crs]
        else:
            self.in_epsg = in_crs
        if type(out_crs) == str:
            self.out_epsg = epsg[out_crs]
        else:
            self.out_epsg = out_crs
            
        self.x = x
        self.y = y
        
    
        if self.in_epsg == 4326 or self.in_epsg == 4322 : 
            '''Long lat in'''
            transformer = Transformer.from_crs(self.in_epsg, self.out_epsg, self.y, self.x)
            out_coords = transformer.transform(self.y, self.x)
            self.out_x = round(out_coords[0], 1)
            self.out_y = round(out_coords[1], 1)   
        
        elif self.out_epsg == 4326 or self.out_epsg == 4322:
            transformer = Transformer.from_crs(self.in_epsg, self.out_epsg, self.x, self.y)
            out_coords = transformer.transform(self.x, self.y)
            self.out_x = round(out_coords[0], 6)
            self.out_y = round(out_coords[1], 6)  
        else:    
            transformer = Transformer.from_crs(self.in_epsg, self.out_epsg, self.x, self.y)
            out_coords = transformer.transform(self.x, self.y)
            self.out_x = round(out_coords[0], 1)
            self.out_y = round(out_coords[1], 1)  
