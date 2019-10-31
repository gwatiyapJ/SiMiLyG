from Bio import Entrez
from urllib.error import HTTPError

w= open(r"/Users/User pc/Desktop/records.txt", "w")
Entrez.email = "james@perdanauniversity.edu.my"     # Always tell NCBI who you are (by providing you email address)
with open(r"/Users/User pc/Desktop/Vid.txt", "r") as f:
	for record in f:
		#f.readlines()
		handle = Entrez.efetch(db="protein", id=record, rettype="gb", retmode="text")
		#print(handle.read())
		w.write(handle.read())
	w.write("\n")					 