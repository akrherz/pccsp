# My purpose in life is to REGRID!

import sys, mx.DateTime, os, shutil

ts0 = mx.DateTime.DateTime(1997,1,1)
tsend = mx.DateTime.DateTime(2000,1,1)
#tsend = ts0 + mx.DateTime.RelativeDateTime(months=1)

# chdir into the folder
os.chdir("mm5input")

# Loop over each month!
now = ts0
while now < tsend:
  nts = now + mx.DateTime.RelativeDateTime(months=1,day=1)
  # PREGRID
  os.chdir("/mnt/tera11/pccsp/REGRID/pregrid")
  vars = {}
  vars['path'] = "/mnt/tera11/pccsp/CCAM/processed/%s" % (now.strftime("%Y%m"), )
  vars['ReanDir'] = "/mnt/tera11/pccsp/REAN2/processed/%s" % (now.strftime("%Y%m"), )
  vars['syear'] = now.year
  vars['smonth'] = "%02i" % (now.month,)
  hr = 0
  #if now == ts0:
  #  hr = 6
  vars['shour'] = "%02i" % (hr,)
  vars['sday'] = "%02i" % (now.day,)
  vars['eyear'] = nts.year
  vars['emonth'] = "%02i" % (nts.month,)
  vars['eday'] = "%02i" % (nts.day,)

  data = open('pregrid.tpl', 'r').read()
  out = open('pregrid.csh', 'w')
  out.write( data % vars )
  out.close()
  os.system("csh pregrid.csh >& /mnt/tera11/pccsp/mm5input/logs/pregrid_%s.log" % (
            now.strftime("%Y%m"), ) )

  # REGRID
  os.chdir("/mnt/tera11/pccsp/REGRID/regridder")
  data = open('namelist.tpl', 'r').read()
  out = open('namelist.input', 'w')
  out.write( data % vars )
  out.close()
  os.system("./regridder >& /mnt/tera11/pccsp/mm5input/logs/regrid_%s.log" % (
            now.strftime("%Y%m"), ) )


  # INTERP
  os.chdir("/mnt/tera11/pccsp/INTERPF")
  data = open('namelist.tpl', 'r').read()
  out = open('namelist.input', 'w')
  out.write( data % vars )
  out.close()
  os.system("./interpf >& /mnt/tera11/pccsp/mm5input/logs/interpf_%s.log" % (
            now.strftime("%Y%m"), ) )

  # Move output!
  if now == ts0:
    os.rename("MMINPUT_DOMAIN1", "/mnt/tera11/pccsp/mm5input/MMINPUT_DOMAIN1.%s"%(
            now.strftime("%Y%m"), ) )
  os.rename("LOWBDY_DOMAIN1", "/mnt/tera11/pccsp/mm5input/LOWBDY_DOMAIN1.%s"%(
            now.strftime("%Y%m"), ) )
  os.rename("BDYOUT_DOMAIN1", "/mnt/tera11/pccsp/mm5input/BDYOUT_DOMAIN1.%s"%(
            now.strftime("%Y%m"), ) )
  now += mx.DateTime.RelativeDateTime(months=1,day=1)
