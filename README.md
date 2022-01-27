# SiMiLyG
Mapping shared sequences (Share-ome)
#Python code for generating k-mers of any defined length from an input biological sequence
kmerslicer is a source code, for constructing/generating generate k-mer (either peptides or nucleotide) sequences of any desired length, based on the sliding window method across given FASTA sequences from an input file.
Written by Stephen A. James at School of Data Sciences, Perdana University, Malaysia 
Email: james@perdanauniversity.edu.my

Description of Code:
This is a Python code(s) designed to generate k-mers and write the output (in "AMONG format") by either appending 
k-mer; Accession number and index number e.g.
A)
MSDTGQMEE; AAK77753.1; 0000001
.
.
.
AAAAAAAAA; AAK77753.1; 0000341 0000342 0000343 0000344 0000369 0000370 0000371 0000372 0000397 0000398 0000399
OR
B)
MSDTGQMEE; AAK77753.1; 0000005
.
.
.
AAAAAAAAA; AAK77753.1; 0000345-0000348 0000373-0000376 0000401-0000403
The code incorporates modules such as Biopython, Statistics, and in addition System-specific parameters and functions in the case of kmerslicer2 source code. The source code in “kmerslicer1” generates the output as shown in ‘A’  (i.e. append  k-mer; IDs;  serial-index number (refere to as "AMONG format"); while the source code in kmerslicer2 generates an output as in ‘B’ but with index number appended based the median residue in the k-mer length. In addition, in kmerslicer2 the occurrence of consecutive index number for a k-mer, it is presented in the form of range value.   For the basic implementation of the code see below: 

Input Format:
A FASTA sequences with a description line (i.e. “> accessions number and sequences detail”) as start of each sequence

Code Execution:
#For code with define input and output file variable 
python sourceCode.py InputFile OutputFile

#For code with define PATH for (input and output) files
python sourceCode.py

Installation:
kmerslicer supports Python 3.x version

For the source code implementation installation of Biopython is required.

Usage: 
kmerslicer is capable of slicing large datasets of biological sequences to any desire length that can be used for and structural/functional characterization.

