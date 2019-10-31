###Altenative script for generating k-mer with consecutive numbers in range format and median number as k-mer index
from Bio import SeqIO
import statistics
import sys

inputFile=str(sys.argv[1])
outputFile=str(sys.argv[2])

fastaFile = []
result = {}
K = 9
#f = open(r"/Users/User pc/Desktop/MyKmers.txt", "w") # Requiried to creat a file to write out put if step 4-5 is ignored
f = open(outputFile, "w")
with open(inputFile, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
                fastaFile.append(record)

for fasta in fastaFile:
        i=0
        j=9						#Required for the k-mer (k) window size (Default is set at 9)
        seq=str(fasta.seq)
        lenOfSeq=len(seq)
        kmersDic={}
        while j <= lenOfSeq:
                kmers=seq[i:j]
                index=statistics.median(range(i,j))+1
                if kmers in kmersDic:
                        kmersList=kmersDic[kmers]
                        kmersList.append(index)
                else:
                        kmersDic[kmers]=[index]	
                i=i+1
                j=j+1
        result[fasta.id] = kmersDic
  
firstvar = 0
nextvar = 0
lastvar = 0

for fastaID in result:
    for kmers in result[fastaID]:
            kmersDic=result[fastaID]
            f.write(kmers+";"+str(fastaID)+"; ")
            for index in kmersDic[kmers]:		#For creating range if the position numbers are consecutive
                    if (firstvar > 0):
                            nextvar = index
                            gap = (nextvar - lastvar)
                            if (gap > 1):
                                if ((nextvar > lastvar) and (lastvar == firstvar)):
                                    f.write (" " + str(nextvar).zfill(7))
                                    firstvar = nextvar
                                    lastvar = nextvar
                                elif ((nextvar > lastvar) and (lastvar > firstvar)):
                                    f.write("-" + str(lastvar).zfill(7))
                                    firstvar = nextvar
                                    lastvar = nextvar
                                    f.write(" " + str(firstvar).zfill(7))
                            if(gap == 1):
                                lastvar = nextvar
                    if(firstvar == 0):
                        firstvar = index
                        lastvar = index
                        nextvar = index
                        f.write(str(firstvar).zfill(7))
            if(lastvar !=0 ):
                if(nextvar > firstvar):
                    f.write("-"+str(nextvar).zfill(7))
                    firstvar = 0
                    nextvar = 0
                    lastvar = 0
                elif(nextvar == firstvar):
                    firstvar = 0
                    nextvar = 0
                    lastvar = 0
            f.write("\n")
            firstvar = 0
            lastvar = 0
            nextvar =0
            
    f.write("\n\n")			





