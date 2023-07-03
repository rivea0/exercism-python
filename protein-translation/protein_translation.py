PROTEIN_TRANSLATIONS = {
	'AUG': 'Methionine',
	'UUU': 'Phenylalanine', 
	'UUC': 'Phenylalanine',
	'UUA': 'Leucine',
	'UUG': 'Leucine',
	'UCU': 'Serine', 
	'UCC': 'Serine', 
	'UCA': 'Serine', 
	'UCG': 'Serine',
	'UAU': 'Tyrosine', 
	'UAC': 'Tyrosine',
	'UGU': 'Cysteine', 
	'UGC': 'Cysteine',
	'UGG': 'Tryptophan',
	'UAA': 'STOP', 
	'UAG': 'STOP', 
	'UGA': 'STOP'
}


def proteins(strand):
    codons = ''
    for i, v in enumerate(strand, start=1):
        codons += v
        if i % 3 == 0:
            codons += ' '
    result = [PROTEIN_TRANSLATIONS[i] for i in codons.split() if i in PROTEIN_TRANSLATIONS]
    if 'STOP' in result:
        return result[:result.index('STOP')]
    return result
