# DNA Sequence Analyzer

dna = input("Enter DNA Sequence: ").upper()

a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

length = len(dna)

gc_content = ((g_count + c_count) / length) * 100

print("\nDNA Analysis")
print("Length:", length)
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
print("GC Content: {:.2f}%".format(gc_content))