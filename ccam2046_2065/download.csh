#!/bin/csh

cd grib/

# topo land
foreach typ (air hgt mslp pres rhum skt tsea uwnd vwnd)
  foreach year (`seq 2046 2065`)
    foreach month (01 02 03 04 05 06 07 08 09 10 11 12)
     if (! -e ${typ}-C160b_gfdlcm21_A2-ct-uf-2.${year}${month}.grb) then
       echo "MISS ${typ}-C160b_gfdlcm21_A2-ct-uf-2.${year}${month}.grb"
       wget -q http://www.hpsc.csiro.au/users/kat024/pccsp/grb/2046to2065/${typ}/${typ}-C160b_gfdlcm21_A2-ct-uf-2.${year}${month}.grb
     endif
    end
  end
end