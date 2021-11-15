def distance(strand_a, strand_b):
    """Calculate the Hamming Distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    differences = [v for i, v in enumerate(strand_a) if v != strand_b[i]]
    return len(differences)
