from Bio.Blast import NCBIWWW
print("Blast program started.....")
handler=NCBIWWW.qblast("blastn","nt","8332116",format_type="Text")
print("Blast program completed.....")
file=open("blast_result.txt","w")
file.write(handler.read())
file.close()