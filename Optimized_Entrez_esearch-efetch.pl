#!/opt/perl-5.8.8/bin/perl

use LWP::Simple;

my $utils = "https://www.ncbi.nlm.nih.gov/entrez/eutils";
open (LIST, "/home/james.student/SHARED_PROTEOME/xac-diff") || die "couldn't open the file (/home/huisan/Desktop/attachments/Test2.txt)!";
   	$db     = "protein";
   	$report = "gp";


while(<LIST>){
	my $query  = $_;
	my $esearch = "$utils/esearch.fcgi?" . "db=$db&retmax=1&usehistory=y&term=";
	my $esearch_result = get($esearch.$query);
	$esearch_result =~ m|<Count>(\d+)</Count>.*<QueryKey>(\d+)</QueryKey>.*<WebEnv>(\S+)</WebEnv>|s;
	$Count    = $1;
	$QueryKey = $2;
	$WebEnv   = $3;
	$retmax=200;
	for(my $retstart = 0; $retstart < $Count; $retstart += $retmax) {
		my $efetch = "$utils/efetch.fcgi?" . "rettype=$report&retmode=text&retstart=$retstart&retmax=$retmax&" . "db=$db&query_key=$QueryKey&WebEnv=$WebEnv";    
		my $efetch_result = get($efetch);
  		print "\n$efetch_result\n\n";
  	}
}
close(LIST);

##Reference:
#Li, W., Jaroszewski, L. and Godzik, A. (2002) ‘Tolerating some redundancy significantly speeds up clustering of large protein databases’, 
#Bioinformatics, 18(1), pp. 77–82. doi: 10.1093/bioinformatics/18.1.77.
