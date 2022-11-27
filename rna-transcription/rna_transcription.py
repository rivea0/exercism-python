def to_rna(dna_strand):
    TRANSLATION = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    return ''.join([TRANSLATION[nucleotide] for nucleotide in dna_strand])
