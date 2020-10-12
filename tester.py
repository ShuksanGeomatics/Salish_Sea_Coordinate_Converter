import convert



#conversion = SalishSeaCoordConverter('WGS84', 'WN_NAD83',  -122.537608, 48.801902)
conversion = convert.SalishSeaCoordConverter('WGS84', 'WN_NAD83', 48.801902,  -122.537608)
print(conversion.out_x)
print(conversion.out_y)
print (conversion.out_x, conversion.out_y)

conversion = convert.SalishSeaCoordConverter('WN_NAD83','WGS84', 1229688.770, 661858.635)
print(conversion.out_x)
print(conversion.out_y)

conversion = convert.SalishSeaCoordConverter('UTM10N_NAD83','WN_NAD83', 533954, 5405537)
print(conversion.out_x)
print(conversion.out_y)


conversion = convert.SalishSeaCoordConverter('UTM10N_NAD83','WN_NAD27', 533954, 5405537)
print(conversion.out_x)
print(conversion.out_y)


conversion = convert.SalishSeaCoordConverter('UTM10N_NAD83','UTM10N_NAD27', 533954, 5405537)
print(conversion.out_x)
print(conversion.out_y)