#!/usr/bin/perl
       
print "Enter a filename: ";
open(NAME,<STDIN>);
print "File contents are:\n";
print "------------------\n";
while(<NAME>) {
  chomp $NAME;
  print $_;
 }

