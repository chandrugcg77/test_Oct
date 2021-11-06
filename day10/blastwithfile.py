from Bio.Blast import NCBIWWW
fasta_file=open(r"E:\github\test_Oct\day10\sample_seq.fasta","r").read()
#qblast using fasta file
handler=NCBIWWW.qblast("blastp","nr",fasta_file)
#handler=NCBIWWW.qblast("blastp","swissprot",fasta_file)
print(handler.read())