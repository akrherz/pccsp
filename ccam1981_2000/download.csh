#!/bin/csh

# topo land
foreach typ (air hgt mslp pres rhum skt tsea uwnd vwnd) 
  foreach year (1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000)
    foreach month (01 02 03 04 05 06 07 08 09 10 11 12)
     if (! -e ${typ}-C160b_gfdlcm21_A2-ct-uf-2.${year}${month}.grb) then
       echo "MISS ${typ}-C160b_gfdlcm21_A2-ct-uf-2.${year}${month}.grb"
       wget -q http://www.hpsc.csiro.au/users/kat024/pccsp/grb/1981to2000/${typ}/${typ}-C160b_gfdlcm21_A2-ct-uf-2.${year}${month}.grb
     endif
    end
  end
end   
