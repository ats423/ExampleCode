#!/usr/bin/perl
use strict;
use warnings;
use Bio::DB::GenBank;
use Bio::DB::Query::GenBank;
use Bio::Ontology::GOterm;

#################################################### 
#Main Program
####################################################

my $in = "F:/Perl2015/CCDS_IN2.txt"; #in file for reading
my %GENES=(); #declare an empty hash

%GENES = &GetUnique($in); #call Get Unique subroutine and pass the in file to it, assign returned data to the empty hash


FastaSeq(%GENES); #call FastaSeq subroutine and pass the %GENES hash to it



####################################################
#Subroutine
####################################################



sub FastaSeq{
	my %gene_hash = $_[0]; 
	my $out_file = ">F:/Perl2015/CCDS_out.txt"; #out file for writing
	open (OUT, $out_file); #open out file
	
	while (my ($key, $value) = each(%GENES)){ #use the while loop to go through the key value pairs of the hash 
	while (my ($k, $v) = each($GENES{$key})){  #use the while loop to go through the key value pairs of the hash 
		my $id = sprintf '%07s', $key; #take only genes that have seven digits
		next if $id =~ /\d{8,}/;#remove genes that have  more than seven digits
		my $go_obj = Bio::Ontology::GOterm -> new (-go_id => $id,       #create new object for GO ID and gene ID
													 -name => "GeneID:$key",
													 );
												
		my $genbankobj = Bio::DB::GenBank->new(-retrievaltype => 'tempfile' ,  #create new object for getting fasta sequence based on gene ID's
                                             -format => 'Fasta');
   		my $seq = $genbankobj->get_Stream_by_id(["$key"] ); #pass gene ID to the get_stream_by_id method
    		while( my $seqid =  $seq->next_seq ) { #use the while loop to go through each ID and print to the out file the GO ID, gene ID, chromosome number and fasta sequence
      			print OUT   $go_obj ->name() , "\t" , $go_obj -> GO_id() , "\n",
      				"Chromosome Number:", $k, "\n",
            		 "FastaSequence:", $seqid->seq, "\n\n",
            		 ;
    									}
		
 		
									} }
										}



####################################################
#Subroutine
####################################################

sub GetUnique{
	my $in_file = $_[0];
	open(IN, $in_file);  #open in file for reading 
	my %Uniq=(); #declare empty hash
	my %genes=(); #declare empty hash
	my %chr=(); #declare empty hash
	while(<IN>){ #use while loop to read the in file line by line	
		chomp($_);
		if($_ =~ /^#/){next;} #use regex to skip over the header
		my @fields=split("\t", $_); #create array and split the columns of in file on the tab delimeter
		next if $fields[5] =~ /withdrawn/i; #pass over genes with withdrawn status
		$Uniq{$fields[0]}{$fields[3]}++; #populate  %Uniq hash with chromosome number column and gene id column
		if($Uniq{$fields[0]}{$fields[3]}==1){ #check if chromosome and gene id pairs are duplicated, else move to next entry
			$chr{$fields[0]}++; #populate %chr with unique values 
			if($chr{$fields[0]}>5){  #skip over any elements past the first five genes from each chromosome
				next;
			}else{
				$genes{$fields[3]}{$fields[0]}++; #else add the first five genes from each chromosome into %genes hash
			}
			
		}else{
			next;
		}
	
	}
	return %genes; #return the unique first five genes from each column and their chromsome number

}

close (OUT); #close the out file
close (IN); #close the in file
