import re

samples = []

with open(r"/home/james.student/Analysis/VIRAL_recordsFORdiff", "r") as f:
   for line in f.readlines():
       if re.search(r'VERSION*|/organism=*', line):                
           samples.append(line)		
print(samples)
print("\n")
print("\n\n")
