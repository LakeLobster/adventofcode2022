#!/usr/bin/perl
#1658 for part 1
#2260 for part 2

$x=<STDIN>;
$length = 14;
for my $i (0..length($x)-$length-1) {
   my %ss; $ss{$_}++ for split //, substr($x,$i,$length);
   if((scalar keys %ss) == $length)
   {
      print($i+$length,"\n");
      exit;
   }
}
