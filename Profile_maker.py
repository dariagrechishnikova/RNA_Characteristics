import numpy as np

def get_nucleotide_pairs():
    # all possible nucleotides
    nucleotides = ['A', 'C', 'G', 'T']

    # all possible ordered nucleotide pairs
    nucl_pairs = []
    for first in nucleotides:
        for second in nucleotides:
            nucl_pairs.append(first + second)

    return nucl_pairs

#print get_nucleotide_pairs()

def get_dinucl_dict ():
    path = "C:\Users\Daria\Documents\PHD\RNA_characterisation\diprodb2.txt"
    tab = np.loadtxt(path, delimiter = '\t', skiprows = 1)
    tab_reshaped = zip(*tab)
    dinucl = get_nucleotide_pairs()
    dinucl_dict = {k: v for k, v in zip(dinucl, tab_reshaped)}
    return dinucl_dict

#def parse_sequence():
 #   path = "C:\Users\Daria\Documents\PHD\RNA_characterisation\test_rna_seq.txt"
    #

#print get_dinucl_dict()

class Sequence:
    seq_id_ = -1
    sequence_ = ""

    def __init__(self, seq_id, sequence):
        self.seq_id_ = seq_id
        self.sequence_ = sequence

    def print_seq(self):
        print "id =", self.seq_id_
        print self.sequence_

class Parser:
    path_ = 'C:\\Users\\Daria\\Documents\\PHD\\RNA_characterisation\\test_rna_seq.txt'
    mark_ = '>'

    def is_id_line(self, line):
        return line[0] == self.mark_

    def extract_id(self, line):
        return line[1:].strip()

    def parse(self):

        sequences = []

        seq_file = open(self.path_, 'r')

        cur_id = ''
        for line in seq_file:
            if self.is_id_line(line):
                cur_id = self.extract_id(line)
                #print "found id", cur_id
                continue

            if cur_id:
                sequences.append(Sequence(cur_id, line.split()))
                #print "found string", line
                cur_id = ''

        return sequences

parser = Parser()

parser.mark_ = '+'

for seq in parser.parse():
    seq.print_seq()
