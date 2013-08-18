&record0
  input_file     = '/mnt/tera11/pccsp/REGRID/regridder/REGRID_DOMAIN1' /

&record1
 start_year                      =    %(syear)s
 start_month                     =    %(smonth)s
 start_day                       =    %(sday)s
 start_hour                      =    %(shour)s
 end_year                        =    %(eyear)s
 end_month                       =    %(emonth)s
 end_day                         =    %(eday)s
 end_hour                        =    00
 interval                        = 21600/
 less_than_24h                   = .FALSE. /

&record2
 sigma_f_bu     = 1.00,0.99,0.98,0.96,0.93,0.89,     ! full sigma, bottom-up,
                  0.85,0.80,0.75,0.70,0.65,0.60,     ! start with 1.0, end
                  0.55,0.50,0.45,0.40,0.35,0.30,     ! with 0.0
                  0.25,0.20,0.15,0.10,0.05,0.00       
 ptop           = 10000                              ! top pressure if need to be redefined
 isfc           = 0 /                                ! # sigma levels to spread
                                                     ! surface information

&record3
 p0             = 1.e5                               ! base state sea-level pres (Pa)
 tlp            = 50.                                ! base state lapse rate d(T)/d(ln P)
 ts0            = 275.                               ! base state sea-level temp (K)
 tiso           = 0./                                ! base state isothermal stratospheric temp (K)

&record4
 removediv      = .TRUE.                             ! T/F remove integrated mean divergence
 usesfc         = .TRUE.                             ! T/F use surface data
 wrth2o         = .TRUE. /                           ! T/F specific humidity wrt H2O

&record5
 ifdatim        =  1 /                               ! # of IC time periods to output
