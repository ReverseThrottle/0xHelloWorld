#!/bin/bash

#Makes a copy of /etc/passwd file
cp /etc/passwd ~/Scripts/Final/passwd.txt
#Checks to see if copy was created
if test -f ~/Scripts/Final/passwd.txt; then
        echo "File exists"
fi

#removes the nologin accounts and just has accounts that can be used
sed -i '/nologin/d' ~/Scripts/Final/passwd.txt
sed -i '/false/d' ~/Scripts/Final/passwd.txt
echo "Done!"
