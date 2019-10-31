#/usr/bin/perl

use strict;
use warnings;
 
my $filename1 = 'sortedHUMAN-IDsKmers';
#my $filename2 = 'uniqidx.list';


open(my $fh1, '<:encoding(UTF-8)', $filename1) or die "Could not open file '$filename1' $!";
#open(my $fh2, '<:encoding(UTF-8)', $filename2) or die "Could not open file '$filename2' $!";
 
#while (my $row = <$fh2>) {
#	chomp $row;
#	print "row:$row\n";
	my $accession1 ="";
	my $seq1="";
	my $no1 ="";
	my $accession2="";
	my $seq2="";
	my $no2="";
	my $printline1 ="";
	my $printline2 ="";
	my $flag = 0;

	while(my $line = <$fh1>)
	{
		chomp $line;
		$line =~ s/\r//g;
		if($accession1) {$accession2=$accession1;}
		if($seq1) {$seq2=$seq1;}
		if($no1) {$no2=$no1;}

		#print "line:$line\n";
		($accession1, $seq1, $no1) = split("\t", $line);
		#print "$accession1\n";
		#print "$seq1\n";
		#print "$no1\n";

		if($accession1 eq $accession2)
		{
			#print "$no2\t$no1\t";
			my $diff = $no1 - $no2;
			#print "$diff\n";
			if($diff<8)
			{
				if($flag == 1)
				{
					print "$printline1";
					$printline1=" $accession1 $seq1 $no1";	
				}
				if($flag == 0)
				{
					$printline1="$accession2 $seq2 $no2 $accession1 $seq1 $no1 ";
					$flag = 1;
				}
				#print "$accession2\t$seq2\t$no2\t$accession1\t$seq1\t$no1\n";
				$accession2=$accession1;
				$accession1="";
				$seq2=$seq1;
				$seq1="";
				$no2=$no1;
				$no1="";
			}
			if($diff>=8)
			{
				if($printline1)
				{
					print "$printline1\t\t\n";
				}
				$printline1 = "";
				$flag = 0;
			}
		}
		else
		{
			print "\n$printline1";
			$printline1 = "";
			$flag = 0;
			#print "not same\n";
			$accession2 = $accession1;
			$seq2 = $seq1;
			$no2 = $no1;
			$accession1="";
			$seq1="";
			$no1="";
		}

		#if($seq1) {$seq2=$seq1;}
		
		#if($no1) {$no2=$no1;}
	}
#}
