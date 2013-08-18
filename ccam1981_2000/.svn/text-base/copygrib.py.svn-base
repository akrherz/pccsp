# Split up the Grib file into one per timestamp

import os, glob, shutil
import mx.DateTime

base = mx.DateTime.DateTime(1981,1,1,0,0)
"""
3-D
  uwnd-C160b_ncep2-uf-0810.198101.grb
  vwnd-C160b_ncep2-uf-0810.198101.grb
  hgt-C160b_ncep2-uf-0810.198101.grb
  air-C160b_ncep2-uf-0810.198101.grb
  mslp-C160b_ncep2-uf-0810.198101.grb
  pres-C160b_ncep2-uf-0810.198101.grb
  rhum-C160b_ncep2-uf-0810.198101.grb
SST
  skt-C160b_ncep2-uf-0810.198101.grb
  tsea-C160b_ncep2-uf-0810.198101.grb
Snow
Soil

"""
sts = mx.DateTime.DateTime(1981,1,1)
ets = mx.DateTime.DateTime(2001,1,1)
interval = mx.DateTime.RelativeDateTime(months=1)
now = sts

while now < ets:
  for prefix in ['SST','3D','SKINT']:
    t2 = now + interval
    fp = "processed/%s/%s.%s0000.grib" % (now.strftime("%Y%m"), prefix, t2.strftime("%Y%m%d"))
    newfp = "processed/%s/%s.%s0000.grib" % (t2.strftime("%Y%m"), prefix, t2.strftime("%Y%m%d"))
    shutil.copyfile( fp, newfp )
    delfp = "processed/%s/%s.%s0000.grib" % (t2.strftime("%Y%m"), prefix, now.strftime("%Y%m%d"))
    os.unlink(delfp)

  now += interval
