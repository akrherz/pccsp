#!/bin/csh

set year=2000

cd processed/${year}02
rm *${year}030100* *${year}022918* *${year}022912* *${year}022906*
mv SST.${year}02290000.grib SST.${year}03010000.grib
mv SKINT.${year}02290000.grib SKINT.${year}03010000.grib
mv 3D.${year}02290000.grib 3D.${year}03010000.grib
cp 3D.${year}03010000.grib ../${year}03/
cp SKINT.${year}03010000.grib ../${year}03/
cp SST.${year}03010000.grib ../${year}03/
