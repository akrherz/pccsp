#!/bin/csh

foreach year (`seq 1997 2000`)
  foreach month (`seq 1 12`)
    set mo=`printf "%02d" $month`
    wget -q http://nomad3.ncep.noaa.gov/pub/reanalysis-2/6hr/flx/flx.ft06.${year}${mo}
  end
end
