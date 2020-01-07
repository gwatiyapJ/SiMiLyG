#!/usr/bin/python

import re 

accession1 = ''
seq1 = ''
no1 = ''
accession2 = '' 
seq2 = ''
no2 = ''
printline1 = ''
printline2 = ''
flag = 0
data = ''

fh1 = open('sortedSWAviral-IDsKmers','r')

while fh1:
 line = fh1.readline()
 line = line.rstrip()
 line = re.sub('\r', '', line )
 if accession1:
  accession2 = accession1
 if seq1:
  seq2 = seq1
 if no1:
  no2 = no1

 #print(len(line))
 data = line.split("\t") 

 if len(data)>=3:
  #print(data)
  accession1 = data[0]
  seq1 = data[1]
  no1 = int(data[2], base=10)

 if (accession1 == accession2):
 
  if no1 == '':
   break
  diff = int(no1) - int(no2) 
  if diff<8:
  #if (int(no1) - int(no2))<2:
   if flag == 1:
    print (printline1, end='')
    printline1 = "\t" + str(accession1) + "\t" + str(seq1) + "\t" + str(no1).zfill(7)
   if flag == 0:
    printline1 = str(accession2) + "\t" + str(seq2) + "\t" + str(no2).zfill(7) + "\t" + str(accession1) + "\t" + str(seq1) + "\t" + str(no1).zfill(7)
    flag = 1
   #print(newline)
   accession2 = accession1
   accession1 = ""
   seq2 = seq1
   seq1 = ""
   no2 = no1
   no1 = ""

  #if (int(no1) - int(no2))>=2:
  if diff>=8:
   if(printline1):
    print (printline1)
    printline1 = ""
    flag = 0

 else:
  print(printline1)
  printline1 = ""
  flag = 0
  accession2 = accession1
  seq2 = seq1
  no2 = no1
  accession1 = ""
  seq1 = ""
  no2 = ""

