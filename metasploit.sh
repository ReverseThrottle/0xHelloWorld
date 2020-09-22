#!/bin/bash

##################################################################
# Zachary Hopping                                                #
# Project_1.5 Simple Script Challenge                            #
#                                                                #
# This script will run an nmap scan an export to an xml document #
#   which will then be uploaded to metasploit                    #
#  where the user can further analyze the results                #
##################################################################

#Requires user to enter IP address or range of addresses
echo "Enter ip address/es"
echo "Ex: 10.10.10.192"
echo "Ex: 10.10.10.1-100"

#Saves input in variable ip
read ip

#shows user what nmap scan is being run against ip
echo "nmap -v -sC -sV -oX output $ip"
nmap -v -sC -sV -oX output $ip

#Starts mehtasploit and imports nmap xml file to metasploit for futher analysis
msfdb init
msfconsole -q -x "db_import output"
