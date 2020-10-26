                                                                                    
#!/usr/bin/perl

#asks user  for input       
print "Enter a filename: ";
open(NAME,<STDIN>);
#Prints contents of that file to console
print "File contents are:\n";
print "------------------\n";
while(<NAME>) {
  chomp $NAME;
  print $_;
 }

