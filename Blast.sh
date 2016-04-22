#!/bin/bash

#export blast path
export PATH="$PATH:$HOME/blast_2.231/ncbi-blast-2.2.31+/bin"

#export blast database path
export BLASTDB="$HOME/blast_2.231/ncbi-blast-2.2.31+/db"

#assign variable to raw sequence input
MY_FA="/home/alexandra/SeqAnalysis/RawSeqRepeat/208p16.txt"

#assign variable to repeat masker out directory
OUT_DIR="/home/alexandra/SeqAnalysis/RawSeqRepeat"

#assign variable to out file
BLAST_OUT="/home/alexandra/blast_2.231/blast_output/blast_out_EST_2.txt"

#assign variable to out file
BLAST_OUT2="/home/alexandra/blast_2.231/blast_output/blast_out_SwissProt_2.txt"

#use repeat masker 
#to mask repeats

perl /usr/local/RepeatMasker/RepeatMasker $MY_FA

#run blast

blastn -query $OUT_DIR/208p16.txt.masked -db est_all -outfmt "6 stitle sseq qstart qend sstart send" > $BLAST_OUT

#run blast

blastx -query $OUT_DIR/208p16.txt.masked -db swissprot.00 -outfmt "6 stitle sseq qstart qend sstart send" > $BLAST_OUT2

