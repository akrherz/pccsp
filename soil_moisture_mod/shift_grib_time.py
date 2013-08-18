"""
Need to dummy shift ReAnalysis II grib files into the future
"""
import mx.DateTime
import os
sts = mx.DateTime.DateTime(1982, 1, 1)
ets = mx.DateTime.DateTime(2002, 1, 1) # twenty years of data

fnow = mx.DateTime.DateTime(2046, 1, 1)
interval = mx.DateTime.RelativeDateTime(hours=6)

now = sts
while now <= ets:
    olddir = now.strftime("../REAN2/processed/%Y%m")
    if now.day == 1 and now.hour == 0:
        olddir = (now - mx.DateTime.RelativeDateTime(days=1)).strftime("../REAN2/processed/%Y%m")
    oldfp = olddir +"/"+ now.strftime("flx.ft06.%Y%m%d%H.grb")
    
    newdir = fnow.strftime("../REAN2/future/%Y%m")
    if fnow.day == 1 and fnow.hour == 0:
        newdir = (fnow - mx.DateTime.RelativeDateTime(days=1)).strftime("../REAN2/future/%Y%m")
    if not os.path.isdir(newdir):
        os.makedirs(newdir)
    newfp = newdir +"/"+ fnow.strftime("flx.ft06.%Y%m%d%H.grb")
    
    cmd = "cdo setdate,%s %s %s" % (fnow.strftime("%Y-%m-%d"),
            oldfp, newfp)
    if os.path.isfile(oldfp):
        os.system(cmd)
    else:
        print 'MISSING %s' % (oldfp,)
    print now, fnow
    now += interval
    fnow += interval