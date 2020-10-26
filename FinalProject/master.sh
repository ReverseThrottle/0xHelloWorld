#!/bin/bash

#Final Project
#Zachary Hopping
#Will use multiple scripts to create final 
#User can pick between what they want to do 

clear
cat << EOF
Please Select:
#Creates menu for user to pick what they want to do 
1. Compress,Encrypt,Decrypt Directory
2. Dump File Contents
3. Scan IP and import to Metasploit
4. Modified /etc/passwd
0. Quit

EOF

echo -n 'Enter Selection [0-4]: '
read -r sel
#Case statement that will run script dependiing on user input
case $sel in
        0) echo 'Program Terminated.';;
        1) /bin/bash ~/Scripts/Final/FinalProject.sh;;
        2) /usr/bin/perl ~/Scripts/Final/FileDump.pl;;
        3) /bin/bash ~/Scripts/Final/metasploit.sh;;
        4) /bin/bash ~/Scripts/Final/passwd.sh;;

        *)
           echo 'Invalid Entry.'>&2
           exit 1
esac
