#! /bin/csh -f
#
# c-shell script to download selected files from dss.ucar.edu using wget
# NOTE: if you want to run under a different shell, make sure you change
#       the 'set' commands according to your shell's syntax
# after you save the file, don't forget to make it executable
#   i.e. - "chmod 755 <name_of_script>"
#
# Experienced Wget Users: add additional command-line flags here
#   Use the -r (--recursive) option with care
#   Do NOT use the -b (--background) option - simultaneous file downloads
#       can cause your data access to be blocked
set opts = "-N"
#
# Replace "xxxxxx" with your password
# IMPORTANT NOTE:  If your password uses a special character that has special meaning
#                  to csh, you should escape it with a backslash
#                  Example:  set passwd = "my\!password"
set passwd = "hello"
#
set cert_opt = ""
# If you get a certificate verification error (version 1.10 or higher), uncomment the following line
set cert_opt = "--no-check-certificate"
#
# authenticate
wget $cert_opt -O /dev/null --save-cookies auth.dss_ucar_edu --post-data="email=akrherz@iastate.edu&passwd=$passwd&action=login" https://dss.ucar.edu/cgi-bin/login
#
# download the file(s)
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}01.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}02.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}03.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}04.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}05.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}06.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}07.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}08.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}09.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}10.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}11.tar
wget $cert_opt $opts --load-cookies auth.dss_ucar_edu http://dss.ucar.edu/datazone/tigwork/ds091.0/${1}/${2}.${3}.${1}12.tar
#
# clean up
rm auth.dss_ucar_edu
