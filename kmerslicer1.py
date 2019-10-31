## Generating kmers overalp of specific window size (k) 

	from Bio import SeqIO
	import statistics


	fastaFile = []
	result = {}
	K = 11
	f = open(r"/Users/User pc/Desktop/pythonEx/2k_mers.txt", "w") #Path for output library containing dictionaries of k-mers 
	with open(r"/Users/User pc/Desktop/pythonEx/viralNinput.txt", "r") as handle:  #Required to path of input FASTA sequences
    		for record in SeqIO.parse(handle, "fasta"):
        			fastaFile.append(record)

	for fasta in fastaFile:
		i=0
		j=9		#Required for the k-mer (k) window size (Default is set at 9)
		seq=str(fasta.seq)
		lenOfSeq=len(seq)
		kmersDic={}
		while j <= lenOfSeq:
			kmers=seq[i:j]
			#index=statistics.median(range(i,j))+1
			index=i+1
			if kmers in kmersDic:
				kmersList=kmersDic[kmers]
				kmersList.append(index)
			else:
				kmersDic[kmers]=[index]	
				i=i+1
				j=j+1
				result[fasta.id] = kmersDic

	for fastaID in result:
		for kmers in result[fastaID]:
			kmersDic=result[fastaID]
			f.write(kmers+";"+str(fastaID)+"; ")
			for index in kmersDic[kmers]:
				f.write(str(index).zfill(7)+" ")
			f.write("\n")
		f.write("\n\n")		