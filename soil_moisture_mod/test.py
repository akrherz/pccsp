import pygrib

grbs = pygrib.open('flx.ft06.1981010100.grb')
#print grbs[6]
o = open('new.grb', 'wb')
for grb in grbs:
 o.write( grb.tostring() )
o.close()
