def distance(seq1, seq2):
    '''This function will calculate the Hamming difference between two sequences of DNA.'''
    pass

    step = 0

    for s, q in zip(seq1, seq2):
    	if s != q:
    		step += 1
    	elif len(seq1) != len(seq2):
    		raise ValueError('The strings are of uneven length.')
    return step
    
strand1 = str(input("Enter the first DNA strand: "))
strand2 = str(input("Enter the second DNA strand: "))

print("The Hamming difference between the two sequences is %s." % distance(strand1, strand2))





