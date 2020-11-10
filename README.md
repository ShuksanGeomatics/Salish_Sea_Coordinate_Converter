**Coordinate_Converter_Salish_Sea
Gerry Gabrisch 11/2020**
Tested and working on:
Python v.3.6
Ubuntu 18.04
Windows 10


**An Python tool to convert coordiantes common to Washington and lower BC Canada.**



This project includes a graphic user interface called converter_gui.py.  converter_gui only accepts common CRS for the Salish Sea from drop-down menues. 
To run the gui open converter_gui.py in your favorite Python IDE or run at the command prompt.
To run at the command line:

$python converter_gui.py

If the gui returns values as inf, inf then pyproj was not able to convert those coordinates.

The Salish Sea coordinate Converter also contains convert.py as an interface to converting coordinates using PyProj.  convert.py will accept any EPSG code as integers but also includes intuitive text inputs for southern B.C and Washington State.

The units of measure for the in CRS and out CRS will always use the native units of measure of the output CRS (ft for State Plane, meters for UTM).

**Installation:**
Download or clone this project from GitHub.
From this directory run
python setup.py install


Alternatively you can install the required pyproj libarary with pip
$pip install pyproj



You can also import convert into other Python projects.  See the example below...

import convert
#conversion = convert.SalishSeaCoordConverter(inCRS, outCRS, x,  y)
conversion = convert.SalishSeaCoordConverter('WGS84', 'WN_NAD83', 48.801902,  -122.537608)
print (conversion.out_x, conversion.out_y)'
	
Example using any EPSG codes:

import convert
conversion = convert.SalishSeaCoordConverter(4326, 2285, 48.801902,  -122.537608)
print (conversion.out_x, conversion.out_y)'

Shortcuts include the following CRS and are available using the gui or the convert.py:
WN_HARN - Washington State Plane North (international feet)
WN_NAD83 - Washington State Plane North (US feet)
WN_NAD27 - Washington State Plane North (US feet)
WS_HARN  Washington State Plane South (international feet)
WS_NAD83 - Washington State Plane South (US feet)
WS_NAD27 - Washington State Plane NSouth(US feet)
UTM10N_WGS84 - UTM (meters)
UTM10N_NAD83 - UTM (meters)
UTM10N_NAD27 - UTM (meters)
UTM10N_WGS72 - UTM (meters)
UTM10N_HARN - UTM (meters)
WGS84 - Longitude, Latitude in decimal degrees
WGS72 - Longitude, Latitude in decimal degrees
