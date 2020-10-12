# Coordinate_Converter_Salish_Sea
Gerry Gabrisch 10/2020

The Salish Sea coordinate Converter contains convert.py as an interface to converting coordinates using PyProj.  convert.py will accept any EPSG code as integers but also includes intuitive text inputs for southern B.C and Washington State.


This project aslo includes a graphic user interface to the converter using converter_gui.py.  converter_gui only accepts common CRS for the Salish Sea. 
If the gui returns values as inf, inf then pyproj was not able to convert those coordinates.
To run the gui open converter_gui.py in your favorite Python IDE or run at the command prompt.
To run at the command line with Linux:
	$python converter_gui.py


The units of measure for the in CRS and out CRS will always use the native units of measure - ft for State Plane, meters for UTM.

Installation:
This tool uses PyProj to do the conversions.
To install PyProj use:
	pip install pyproj

If you want to be make the convert available accross all of Python:
	For ArcMap users place the contents of the Salish_Sea_Coordinate_Converter directory into C:\Python27\ArcGIS10.x\Lib
	For ArcPro users place the contents of the Salish_Sea_Coordinate_Converter directory in the Lib file of your cloaned version of Python3.
	For Debian users place the contents of the Salish_Sea_Coordinate_Converter in  /home/yournamehere/.local/lib/python3.x/site-packages/

Example using shortcuts (strings):

	import convert
	#conversion = convert.SalishSeaCoordConverter(inCRS, outCRS, x,  y)
	conversion = convert.SalishSeaCoordConverter('WGS84', 'WN_NAD83', 48.801902,  -122.537608)
	print (conversion.out_x, conversion.out_y)
	
Example using EPSG codes:

	import convert
	conversion = convert.SalishSeaCoordConverter(4326, 2285, 48.801902,  -122.537608)
	print (conversion.out_x, conversion.out_y)

Shorecuts include the following CRS and are available using the gui or the convert.py:
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
