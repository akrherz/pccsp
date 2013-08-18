# Split up the Grib file into one per timestamp

import os, glob
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
os.chdir("dl")

sts = mx.DateTime.DateTime(1981,1,1)
ets = mx.DateTime.DateTime(2001,1,1)
interval = mx.DateTime.RelativeDateTime(months=1)
now = sts

while now < ets:
  basedir = "../processed/%s" % (now.strftime("%Y%m"),)
  os.mkdir( basedir )
  t2 = now + interval
  mins = int( (t2 - now).minutes + 360.0 )
  for prefix in ['uwnd','vwnd','hgt','air','mslp','pres','rhum']:
    grib = "%s-C160b_gfdlcm21_A2-ct-uf-2.%s.grb" % (prefix, now.strftime("%Y%m"))
    print "3D Processing", grib
    for cnt in range(360,mins, 360):
      ts = now + mx.DateTime.RelativeDateTime(minutes=cnt)
      cmd = "wgrib -s %s | grep ':%smin' | wgrib -i %s -grib -o %s/3D.%s.grib -append >& /dev/null" % ( grib, cnt, grib, basedir, ts.strftime("%Y%m%d%H%M") )
      os.system(cmd)

  for prefix in ['tsea',]:
    grib = "%s-C160b_gfdlcm21_A2-ct-uf-2.%s.grb" % (prefix, now.strftime("%Y%m"))
    print "SST Processing", grib
    for cnt in range(360,mins, 360):
      ts = now + mx.DateTime.RelativeDateTime(minutes=cnt)
      cmd = "wgrib -s %s | grep ':%smin' | wgrib -i %s -grib -o %s/SST.%s.grib -append >& /dev/null" % ( grib, cnt, grib, basedir, ts.strftime("%Y%m%d%H%M") )
      os.system(cmd)

  for prefix in ['skt',]:
    grib = "%s-C160b_gfdlcm21_A2-ct-uf-2.%s.grb" % (prefix, now.strftime("%Y%m"))
    print "SKINT Processing", grib
    for cnt in range(360,mins, 360):
      ts = now + mx.DateTime.RelativeDateTime(minutes=cnt)
      cmd = "wgrib -s %s | grep ':%smin' | wgrib -i %s -grib -o %s/SKINT.%s.grib -append >& /dev/null" % ( grib, cnt, grib, basedir, ts.strftime("%Y%m%d%H%M") )
      os.system(cmd)

  now += interval
