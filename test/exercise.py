import mm5_class
import mx.DateTime
import os

for i in range(1000):
    fp = '../testdata/MMOUT_DOMAIN1_%03i' % (i,)
    if not os.path.isfile( fp ):
        continue
    mm5 = mm5_class.mm5( fp )

    tdict = mm5.reftime
    ts = mx.DateTime.DateTime(tdict['year'], tdict['month'],
                          tdict['day'], tdict['hour'])
    incsec = mm5.timeincrement
    steps = mm5.tsteps
    endminute = mm5.mm5_header[('bhr', 1, 12)][1]
    tsend = ts + mx.DateTime.RelativeDateTime(minutes=endminute)
    print fp, tsend, endminute
    del( mm5 )