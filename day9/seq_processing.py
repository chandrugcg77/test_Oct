from Bio import SeqIO
path=r"E:\github\test_Oct\day9\sequence.fasta"

records=SeqIO.parse(path,"fasta")
file=open("transcribed_seq.fatsa","w")
for seq in records:
    file.write(">"+str(seq.id)+"\n")
    file.write(str(seq.seq.transcribe())+"\n")
file.close()