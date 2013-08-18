# My purpose in life is to generate good netcdf files from 
# output from our MM5 runs

import sys
import os
import glob
import mm5_class
import netCDF3
import mx.DateTime
import numpy
import lib

ts0 = mx.DateTime.DateTime(1981,1,1,3)
tsend = mx.DateTime.DateTime(2001,1,1,0)

NCOUT, MMOUT = range(2)
datasources = ["NCOUT_DOMAIN1_???_interp.nc", "MMOUTP_DOMAIN1_???_interp.nc"]

META = {
    'REAN2' : {'fp': 'REAN2',
'title': 'ISU MM5 model output prepared for PCCSP using REAN2 input',
'experiment_id': 'NCEP Reanalysis Run 1',
'forcing_data': 'NCEP Reanalysis II',               
               },
    'CCAM'  : {'fp': 'CCAM81',
'title': 'ISU MM5 model output prepared for PCCSP using CCAM input',
'experiment_id': 'CCAM Run 1',
'forcing_data': 'CCAM 1981-2000',  
               },
        }
metadata = META[ sys.argv[1] ]

outputvars = {
 'tas': {'source': MMOUT,
         'vname' : 't2',
         'units' : 'K', 
         'coord' : 'lon lat height',
         'cellm' : 'time: Instantaneous',
         'lname' : 'Surface Air Temperature',
         'sname' : 'air_temperature'},
 'psl' : {'source' : NCOUT, 
          'vname'  : 'pmsl',
          'units'  : 'Pa',
          'coord' : "lon lat",
          'cellm'  : 'time: Instantaneous',
          'lname'  : 'Sea Level Pressure',
          'sname'  : 'air_pressure_at_sea_level'},
 'uas' : {'source' : MMOUT,
          'vname'  : 'u10',
          'units'  : 'm s-1',
          'coord'  : 'lon lat height',
          'cellm'  : 'time: Instantaneous',
          'lname'  : 'Zonal Surface Wind Speed',
          'sname'  : 'eastward_wind'},
 'vas' : {'source' : MMOUT,
          'vname'  : 'v10',
          'units'  : 'm s-1',
          'coord'  : 'lon lat height',
          'cellm'  : 'time: Instantaneous',
          'lname'  : 'Meridional Surface Wind Speed',
          'sname'  : 'northward_wind'},
 't850' : {'source' : MMOUT,
            'vname'  : 't', 
            'vindex' : 2, #!important, as it supports 3d var
            'units'  : 'K',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '850 hPa Air Temperature',
            'coord'  : 'lon lat plev',
            'sname'  : 'air_temperature'},
 't700' : {'source' : MMOUT,
            'vname'  : 't', 
            'vindex' : 3, #!important, as it supports 3d var
            'units'  : 'K',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '700 hPa Air Temperature',
            'coord'  : 'lon lat plev',
            'sname'  : 'air_temperature'},
 't500' : {'source' : MMOUT,
            'vname'  : 't', 
            'vindex' : 4, #!important, as it supports 3d var
            'units'  : 'K',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '500 hPa Air Temperature',
            'coord'  : 'lon lat plev',
            'sname'  : 'air_temperature'},
 't300' : {'source' : MMOUT,
            'vname'  : 't', 
            'vindex' : 5, #!important, as it supports 3d var
            'units'  : 'K',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '300 hPa Air Temperature',
            'coord'  : 'lon lat plev',
            'sname'  : 'air_temperature'},
 'v850' : {'source' : MMOUT,
            'vname'  : 'v', 
            'vindex' : 2, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '850 hPa Meridional Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'northward_wind'},
 'v700' : {'source' : MMOUT,
            'vname'  : 'v', 
            'vindex' : 3, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '700 hPa Meridional Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'northward_wind'},
 'v500' : {'source' : MMOUT,
            'vname'  : 'v', 
            'vindex' : 4, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '500 hPa Meridional Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'northward_wind'},
 'v300' : {'source' : MMOUT,
            'vname'  : 'v', 
            'vindex' : 5, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '300 hPa Meridional Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'northward_wind'},
 'u850' : {'source' : MMOUT,
            'vname'  : 'u', 
            'vindex' : 2, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '850 hPa Zonal Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'eastward_wind'},
 'u700' : {'source' : MMOUT,
            'vname'  : 'u', 
            'vindex' : 3, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '700 hPa Zonal Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'eastward_wind'},
 'u500' : {'source' : MMOUT,
            'vname'  : 'u', 
            'vindex' : 4, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '500 hPa Zonal Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'eastward_wind'},
 'u300' : {'source' : MMOUT,
            'vname'  : 'u', 
            'vindex' : 5, #!important, as it supports 3d var
            'units'  : 'm s-1',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '300 hPa Zonal Wind Speed',
            'coord'  : 'lon lat plev',
            'sname'  : 'eastward_wind'},
 'zg850' : {'source' : MMOUT,
            'vname'  : 'h', 
            'vindex' : 2, #!important, as it supports 3d var
            'units'  : 'm',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '850 hPa Geopotential Height',
            'coord'  : 'lon lat plev',
            'sname'  : 'geopotential_height'},
 'zg700' : {'source' : MMOUT,
            'vname'  : 'h', 
            'vindex' : 3, #!important, as it supports 3d var
            'units'  : 'm',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '700 hPa Geopotential Height',
            'coord'  : 'lon lat plev',
            'sname'  : 'geopotential_height'},
 'zg500' : {'source' : MMOUT,
            'vname'  : 'h',
            'vindex' : 4, #!important, as it supports 3d var
            'units'  : 'm',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '500 hPa Geopotential Height',
            'coord'  : 'lon lat plev' ,
            'sname'  : 'geopotential_height'},
 'zg300' : {'source' : MMOUT,
            'vname'  : 'h',
            'vindex' : 5, #!important, as it supports 3d var
            'units'  : 'm',
            'cellm'  : 'time: Instantaneous',
            'lname'  : '200 hPa Geopotential Height',
            'coord'  : 'lon lat plev' ,
            'sname'  : 'geopotential_height'},
 'rsds': {'source' : NCOUT,
          'vname'  : 'gsw1',
          'units'  : 'W m-2',
             'coord' : "lon lat",
          'cellm'  : 'time: mean (interval: 3 hours)',
          'lname'  : 'Surface Downwelling Shortwave Radiation',
          'sname'  : 'surface_downwelling_shortwave_flux_in_air'},
 'tasmax': {'units'  : 'K',
            'source' : NCOUT,
            'vname'  : 'tmax',
            'coord' : 'lon lat height',
            'cellm' : 'time: maximum (interval: 3 hours)',
            'lname' : 'Maximum Surface Air Temperature',
            'sname'  : 'air_temperature'},
 'tasmin': {'units'  : 'K',
            'source' : NCOUT,
            'vname'  : 'tmin',
            'coord' : 'lon lat height',
            'lname' : 'Minimum Surface Air Temperature',
            'cellm' : 'time: minimum (interval: 3 hours)',
            'sname'  : 'air_temperature'},
}




def interpb_step(datadir):
    os.chdir(datadir)
    # Figure out a list of MMOUT files
    files = glob.glob("MMOUT_DOMAIN1_???")
    files.sort()
    # Move us to interpb
    os.chdir("../INTERPB")
    for file in files:
        # We don't wish to convert this file, it is just along for the ride
        if file == "MMOUT_DOMAIN1_000":
            continue
        # Figure out time axis
        taxis = lib.extract_times(datadir+file)

        # Setup variable substitution values
        vars = {}
        vars['mm5file'] = datadir+file
        vars['syear'] = taxis[0].year
        vars['smonth'] = taxis[0].month
        vars['sday'] = taxis[0].day
        vars['shour'] = taxis[0].hour
        vars['eyear'] = taxis[-1].year
        vars['emonth'] = taxis[-1].month
        vars['eday'] = taxis[-1].day
        vars['ehour'] = taxis[-1].hour

        # Edit the namelist.input for interb
        data = open('namelist.tpl', 'r').read()
        out = open('namelist.input', 'w')
        out.write( data % vars )
        out.close()
        
        # Run interb for each file
        print "Running INTERPB for %s [%s - %s]" % (file,
              taxis[0].strftime("%Y-%m-%d %H"), 
              taxis[-1].strftime("%Y-%m-%d %H"))
        os.system("./interpb >& interpb.log")

        # Move output file to right location
        os.rename("MMOUTP_DOMAIN1", datadir + file.replace("UT", "UTP"))
        # Cleanup
        os.system("rm -rf FILE_*")


def special_precip( datadir ):
    """
    Need a special function to compute precip
    """
    os.chdir( datadir  )
    fname = generate_filename("pr")
    nc = netCDF3.Dataset( fname , 'w')
    nc_setup( nc , 'pr')

    myvar = nc.createVariable('pr', 'f', ('time','lat','lon'))
    myvar.units = 'kg m-2 s-1'
    myvar.standard_name = 'precipitation_flux'
    myvar.long_name = "Precipitation"
    myvar._FillValue = 1.e20
    myvar.coordinates = "lon lat"
    myvar.cell_methods = "time: average (interval: 3 hours)"
    myvar.original_name = 'raincon+rainnon'
    myvar.history = 'v2 code 20090806'

    files = glob.glob( datasources[ MMOUT ])
    files.sort() # Make sure time lines up this way!
    tcounter = 0
    for file in files:
        tnc = netCDF3.Dataset( file )
        # Values are in cm
        non = tnc.variables['rain_non']
        tsteps = non.shape[0]
        for i in range(tsteps):
            con = tnc.variables['rain_con'][i]
            non = tnc.variables['rain_non'][i]
            tot = non + con
            #print tcounter, max( max( tot ) )
            # Write out! Convert to kg m-2 and divide by 10800 secs
            # Input is cm need to x10 to get to mm == kg m^-2
            myvar[tcounter] = (tot * 10.0 / 10800.0).astype('f')
            tcounter += 1
        tnc.close()
        del(tnc)

    nc.close()


def special_spechumidity( datadir ):
    """
    Special function to compute Specific Humidity
    """
    os.chdir( datadir )
    fname = generate_filename("huss")
    nc = netCDF3.Dataset( fname , 'w')
    nc_setup( nc , 'huss')

    myvar = nc.createVariable('huss', 'f', ('time','lat','lon'))
    myvar.units = 'kg kg-1'
    myvar.standard_name = 'specific_humidity'
    myvar.long_name = "Surface Specific Humidity"
    myvar.cell_methods = "time: instantaneious"
    myvar._FillValue = 1.e20
    myvar.coordinates = "lon lat height"
    myvar.original_name = 'q2/(1+q2)'

    files = glob.glob( datasources[ MMOUT ])
    files.sort() # Make sure time lines up this way!
    tcounter = 0
    for file in files:
        tnc = netCDF3.Dataset( file )
        # 2m mixing ratio kg kg-1
        q2 = tnc.variables['q2'][:]
        tsteps = q2.shape[0]
        myvar[tcounter:(tcounter+tsteps)] = (q2 / (1.0 + q2)).astype('f')
        tcounter += tsteps
        tnc.close()
        del(tnc)

      # Compute Dew Point
      #d2 = t2[i] / (1+ 0.000425 * t2[i] * -(Numeric.log10(rh[i]/100.0)) )
      # Compute Saturation vapor pressure
      #pws = Numeric.exp( 77.3450 + (0.0057 * d2) - (7235 / d2)) / Numeric.power(d2,8.2)  
      #sh = 0.62198 * pws / (100000 + pws)

    nc.close()


def generate_filename(varname):
    """
    Return the filename that should be used given a variable name
    """
    return "%s_IMM5_%s.nc" % (varname, metadata['fp'])


def rename_files( datadir ):
    """
    We want to rename any files with two digit number values
    """
    os.chdir( datadir )
    for p in ["NC", "MM"]:
        for i in range(100):
            fp = "%sOUT_DOMAIN1_%02i" % (p, i)
            if os.path.isfile( fp ):
                fp2 = "%sOUT_DOMAIN1_%03i" % (p, i)
                os.rename( fp , fp2)

def finalize_step( datadir ):
    """
    This is going to be the most complicated, have to generate the necessary
    output files with everything set A-OK
    """
    os.chdir( datadir )
    # Loop over each variable
    for vname in outputvars.keys():
        meta = outputvars[ vname ]
        # Create the NetCDF File
        fname = generate_filename(vname)
        nc = netCDF3.Dataset( fname , 'w')
        nc_setup( nc , vname)
        # Now we create the variable of interest
        myvar = nc.createVariable(vname, 'f', ('time','lat','lon'))
        # Assign Units
        myvar.units = meta['units']
        # Assign Standard Name
        myvar.standard_name = meta['sname']
        # Assign Long Name
        myvar.long_name = meta["lname"]
        # Fill Value
        myvar._FillValue = 1.e20
        # Coordinate Singleton
        if meta.has_key('coord'):
            myvar.coordinates = meta['coord']
        # Cell Methods
        if meta.has_key('cellm'):
            myvar.cell_methods = meta['cellm']
        # Positive
        if meta.has_key('positive'):
            myvar.positive = meta['positive']
        # Original Name of the variable in the MM5 file
        myvar.original_name = meta['vname']

        # Lets get data already!
        files = glob.glob( datasources[ meta['source'] ])
        files.sort() # Make sure time lines up this way!
        tcounter = 0
        for file in files:
            tnc = netCDF3.Dataset( file )
            # Get the variable from the NetCDF File
            tvar = tnc.variables[ meta['vname'] ][:,:,:]
            if meta.has_key('vindex'):
                tvar = tnc.variables[ meta['vname'] ][:,meta['vindex'],:,:]
            # Figure out the time dimension length, always first
            tlen = tvar.shape[0]
            print '%s [%s,%s] %s sample: %.2f shape: %s' % (
                 vname, tcounter,
                  tcounter+tlen, file, tvar[0,10,10],
                  tvar.shape )
            if meta.has_key('quo'):
                tvar = tvar / meta['quo']
            myvar[tcounter:(tcounter+tlen)] = tvar
            tcounter += tlen
            tnc.close()
            del(tnc)

        # Done with var
        nc.close()


def nc_setup(nc, varname):
    """
    Standard setup of a netCDF output file
    """
    # Requirements
    nc.institution   = "Iowa State University, Ames, IA, USA"
    nc.source        = "MM5 (2009): atmosphere: MM5v3.6.3 non-hydrostatic, split-explicit; sea ice: Noah; land: Noah"
    nc.project_id    = "PCCSP"
    #nc.table_id      = "Table 2"
    nc.realization   = 1
    nc.forcing_data  = metadata['forcing_data']
    nc.experiment_id = metadata['experiment_id'] 
    # Optional
    nc.Conventions   = 'CF-1.0'
    nc.contact       = "Daryl Herzmann, akrherz@iastate.edu, 515-294-5978"
    nc.history       = "%s Generated" % (mx.DateTime.now().strftime("%d %B %Y"),)
    nc.comment       = "Runs processed on cystorm@ISU, output processed on mtarchive@ISU"
    nc.title         = metadata['title']
    
    # Setup Dimensions
    tsteps = int( (tsend - ts0).days * 8 ) # 3 hourly
    nc.createDimension('time', tsteps)
    nc.createDimension('lat', 71)
    nc.createDimension('lon', 91)
    nc.createDimension('bnds', 2)

    # Generate the coordinate variables
    tm = nc.createVariable('time', 'd', ('time',) )
    tm.units = "days since %s 00:00:00.0" % (ts0.strftime("%Y-%m-%d"),)
    tm.calendar = "gregorian"
    tm.long_name = "time"
    tm.standard_name = "time"
    tm.axis = "T"
    tm[:] = numpy.arange(0.125, (tsend - ts0).days + 0.125, 0.125)

    # Compute the time_bnds variable, somewhat yucky
    if varname in ['cuhusa', 'cvhusa', 'hfls', 'hfss', 'mrro',
                   'pr', 'psl', 'rsds', 'rlds', 'mrros']:
        tm.bounds = "time_bnds"

        tb = nc.createVariable('time_bnds', 'd', ('time','bnds') )
        val = numpy.zeros( (tsteps,2), 'd' )
        val[:,0] = numpy.arange(0, (tsend - ts0).days , 0.125)
        val[:,1] = numpy.arange(0.125, (tsend - ts0).days + 0.125, 0.125)
        tb[:] = val

    lat = nc.createVariable('lat', 'd', ('lat',) )
    lat.units = "degrees_north"
    lat.long_name = "latitude"
    lat.standard_name = "latitude"
    lat.axis = "Y"
    lat[:] = numpy.arange(-25.0,10.1,0.5)

    lon = nc.createVariable('lon', 'd', ('lon',) )
    lon.units = "degrees_east"
    lon.long_name = "longitude"
    lon.standard_name = "longitude"
    lon.axis = "X"
    lon[:71] = numpy.arange(145.0,180.1,0.5)
    lon[-20:] = numpy.arange(-179.5,-169.9,0.5)

    # Generate singletons
    if varname in ['huss','tas','tasmax', 'tasmin','uas','vas']:
        height = nc.createVariable('height', 'd')
        height.long_name = "height"
        height.standard_name = "height"
        height.units = "m"
        height.positive = "up"
        height.axis = "Z"
        if varname in ['huss','tas','tasmax','tasmin']:
            height[:] = 2.
        elif varname in ['uas','vas']:
            height[:] = 10.

    if varname in ['zg850','zg500','zg200','mpuhusa','mpvhusa']:
        plev = nc.createVariable('plev', 'd')
        plev.long_name = "pressure"
        plev.standard_name = "air_pressure"
        plev.units = "Pa"
        plev.positive = "down"
        plev.axis = "Z"
        if varname in ['zg850','mpuhusa','mpvhusa']:
            plev[:] = 85000.
        elif varname in ['zg500',]:
            plev[:] = 50000.
        elif varname in ['zg200',]:
            plev[:] = 20000.


def convert_to_netcdf(datadir):
    """
    Convert any files we find datadir to netCDF
    """
    # Change directory
    os.chdir( datadir )
    # Look for any MMOUT and NCOUT files
    files = glob.glob('NCOUT_DOMAIN1_[0-9][0-9][0-9]')
    files = files + glob.glob('MMOUTP_DOMAIN1_[0-9][0-9][0-9]')
    files.sort()
    # Loop over the files
    for file in files:
        # Skip the initial output files, we don't care about these
        if file == "NCOUT_DOMAIN1_000" or file == "MMOUTP_DOMAIN1_000":
            continue
        if os.path.isfile( file +".nc"):
            continue
        # Figure out how many timesteps there are.
        mm5 = mm5_class.mm5(file)
        cmd = "archiver %s 0 %s" % (file, mm5.tsteps)
        print "Converting %s to NetCDF %s tsteps" % (file, mm5.tsteps)
        si,so = os.popen4( cmd )
        a = so.read() # Necessary to keep things blocking?
        if not os.path.isfile( file+".nc" ):
            print "FAIL!", file
            print a
            sys.exit()
        # Now we corrupt the grid, shift 30 degrees west
        nc = netCDF3.Dataset( file+".nc", 'a')
        nc.variables['coarse_cenlon'][:] = 138.
        nc.variables['stdlon'][:] = 138.
        nc.close()


    

def convert_to_ll( datadir ):
    """
    Convert the netCDF files to regular Lat/Lon Grids
    """
    # Change directory
    os.chdir( datadir )
    # Look for any MMOUTP and NCOUT NC files
    files = glob.glob("NCOUT_DOMAIN1_*.nc")
    files = files + glob.glob("MMOUTP_DOMAIN1_*.nc")
    files.sort()
    # Loop over the files
    for file in files:
        cmd = "proj2ll %s 10.0 -25.0 0.5 160. 115. 0.5" % (file,)
        print "Convert %s to LatLon Coords" % (file,)
        si,so = os.popen4( cmd )
        a = so.read() # Necessary to keep things blocking?
        if not os.path.isfile( file.replace(".nc", "_interp.nc") ):
            print "FAIL!", file
            print a
            sys.exit()
        # Remove intermediate netcdf file
        os.remove( file )



if __name__ == '__main__':
    datadir = sys.argv[2]
    print 'Step 0: Rename any two digit named files'
    rename_files( datadir )
    print 'Step 1: interpb'
    interpb_step( datadir )
    print 'Step 2: Convert NCOUT* MMOUT* files to netCDF (archiver)'
    convert_to_netcdf(datadir)
    print 'Step 3: Converting netCDF files into Lat/Lon'
    convert_to_ll(datadir)
    print 'Step 4: Collect lat/lon data into uber netcdf file!'
    finalize_step( datadir )
    special_spechumidity( datadir )
    special_precip( datadir )
    