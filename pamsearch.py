import argparse
import regex
import re
parser = argparse.ArgumentParser()
parser.add_argument( '-i' ,'--input',help= 'fasta file required.')
parser.add_argument( '-p' ,'--pattern',help= 'string pattern to be searched in the given fasta sequences.')
#parser.add_argument( '-v','--variable', help = 'string variable required.')
args = parser.parse_args()


input=args.input
pattern=args.pattern
#variable=args.variable
print("variable file:")
#print(variable)
print("input file :")
print(input)
out=input.replace('.fasta','') + "_" +pattern + "RECENT1.txt"
f2=open(out,'w')
seqdic={}
pam=pattern.replace('N','[ACGT]').replace('R','[AG]').replace('Y','[CT]').replace('V','[ACG]')
print(pam)
pam1 ='[ACGT]{20}'  +  pam 
 
with open(input) as sequences:
    for line in sequences:
            if line.startswith(">"):
                name = line[1:-1]
                #print(name)
                seqdic[name] = []
            else:
                seqdic[name].append(line[:-1])
                # seqdic[laast].append(line)
            
    for name in seqdic:
        print(name)
        seqdic[name] = ''.join(seqdic[name])
        long_seq_record = seqdic[name]
        #print(long_seq_record[1:20])
        #NGG1 = re.finditer(r"[ACGT]{21}GG", long_seq_record)
        #NGG = re.finditer(pam1, long_seq_record)
        NGG = regex.finditer(pam1, long_seq_record,overlapped=True )
        for match in NGG:
             
        #print(match.start(),match.end(),match.group())

            laast=  name +"\t" +str(match.start())+ "\t" + str(match.end()) + "\t" +str(match.group()) + "\n"
        
            f2.write(laast)



