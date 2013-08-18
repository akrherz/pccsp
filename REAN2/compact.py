# Extract the tar files found, place just the fields I need
# in a resulting file
# Lets process one year at a time

import glob, os, mx.DateTime, sys, re

lookup = {
 'pgb': [15,16,18,19,21,22,24,25],
 'dg3': [5,9,10],
 'si': [1],
 'sst': [1]
}

YEAR = sys.argv[1]
# Either pgb or flx
TYP = sys.argv[2]

# Find all my tar files
DIR="/mnt/tera11/pccsp/REAN2/download"
tars = glob.glob("%s/flx.ft06.%s??.tar" % (DIR, YEAR) )
#tars = glob.glob("%s/pgb.anl.%s??.tar" % (DIR, YEAR) )

#DIR="/tera2/reanalysis-2/pircs1c/%s" % (YEAR,)
#DIR="."
#tars = glob.glob("%s/%s.s*.tar" % (DIR, YEAR) )

for file in tars:
  print "Processing tar file: %s" % (file,)
  # Extract them
  os.system("tar -xf %s" % (file, ))
  gribs = glob.glob("*.grb")
  for grib in gribs:
    yyyymmddhh = re.findall("([0-9]{10})", grib)[0]
    ts = mx.DateTime.strptime(yyyymmddhh, '%Y%m%d%H')
    newfp = grib
    # Files are 6 hour forecasts
    if TYP == "flx":
      ts += mx.DateTime.RelativeDateTime(hours=6)
      newfp = ts.strftime("flx.ft06.%Y%m%d%H.grb")

    if not os.path.isdir("processed/%s" % (ts.strftime("%Y%m"),)):
      os.mkdir("processed/%s" % (ts.strftime("%Y%m"),))

    if ts.day == 1 and ts.hour == 0:
      yest = ts - mx.DateTime.RelativeDateTime(days=1)
      if not os.path.isdir("processed/%s" % (yest.strftime("%Y%m"),)):
        os.mkdir("processed/%s" % (yest.strftime("%Y%m"),))
      os.system("cp %s processed/%s/%s" % (grib, yest.strftime("%Y%m"),newfp ))
    os.system("mv %s processed/%s/%s" % (grib, ts.strftime("%Y%m") , newfp))
