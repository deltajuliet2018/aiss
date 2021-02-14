#! /bin/bash
#################
##Created for AISS####
##08 Feb 2020#######


clear

PERSON=$(whoami)

if ! [ $PERSON == "oracle" ] 
then
	echo " "
	echo "  $PERSON user is not allowed to run"
	echo "  this command. Try being oracle."
	echo " "
	exit 1
fi


if  [  "$1" == "revert"  ] 

then
	cd /opt/EAD/SDO/current/config/
	sed s/DEBUG/WARN/g  sdo_app_log4j.properties  > anewtemp
	cp -f anewtemp sdo_app_log4j.properties
	rm -f anewtemp
	
else
	cd /opt/EAD/SDO/current/config/
	sed s/WARN/DEBUG/g  sdo_app_log4j.properties  > anewtemp
	cp -f anewtemp sdo_app_log4j.properties
	rm -f anewtemp
	

fi





