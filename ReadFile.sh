#By: Zachary Hopping
#Project_1.2 Due September 20th 
#Parse /etc/paswd file and look for username, dir, shell
#Put into text file in alphabetical order

#!/bash/sh

#using awk command to search for field 1,6 and 7 those are the usernames, directory, and shells
#sorts the text file in alphabetical order

awk -F: '{print $1, $6, $7}' /etc/passwd | sort > user.txt
