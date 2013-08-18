
import mm5_class
import numpy
import Nio
import pygrib
import Ngl
import random
import sys

# two levels, lat_98 , lon_98
grbs = pygrib.open('flx.ft06.2046010100.grb')
print grbs[6]['values']
print grbs[7]['values']
lats, lons = grbs[6].latlons()
lats = lats[:,0]
lons = lons[0,:]


# Our final values
emm5 = mm5_class.mm5('MMOUT_DOMAIN1_46')
edata = numpy.ravel(emm5.get_field('soil_m_1',0)["values"])
edata4 = numpy.ravel(emm5.get_field('soil_m_4',0)["values"])
elats = numpy.ravel(emm5.get_field('latitcrs',0)["values"])
elons = numpy.ravel(emm5.get_field('longicrs',0)["values"])
for i in range(len(elats)):
  elats[i] += (random.random()  * 0.01)

newdata = Ngl.natgrid(elons, elats, edata, lons, lats)
grbs[6]['values'] = newdata
newdata = Ngl.natgrid(elons, elats, edata4, lons, lats)
grbs[7]['values'] = newdata

o = open('flx.ft06.2046010100.grb-new', 'wb')
grbs.rewind()
for grb in grbs:
  o.write( grb.tostring() )
o.close()
