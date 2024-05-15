#!/usr/bin/env python
import argparse
from Bio import SeqIO
import re
import numpy as np
import pandas as pd

def get_ngaps(fasta_seq, gapsize):
    matches = re.findall(r'(N)\1{'+str(gapsize)+',}', fasta_seq, re.IGNORECASE)
    return len(matches)


parser = argparse.ArgumentParser()
parser.add_argument("-f","--fasta", nargs='+',  required=True, help="Input fasta files to be analyzed")
parser.add_argument("-o","--out", required=True, help="Output file name")
args = parser.parse_args()

fasta_files = args.fasta 
out_file = args.out

out_dict = {}
for fasta in fasta_files:
    combined_fasta = ""
    nGaps_count = 0
    contig_count = 0
    lengths = []
    fasta_sequences = SeqIO.parse(open(fasta),'fasta')
    for single_fasta in fasta_sequences:
        fasta_seq = str(single_fasta.seq)
        lengths.append(len(fasta_seq))
        combined_fasta += fasta_seq
        nGaps_count += get_ngaps(fasta_seq, 10)
        contig_count += 1
    A = combined_fasta.upper().count('A')
    T = combined_fasta.upper().count('T')
    C = combined_fasta.upper().count('C')
    G = combined_fasta.upper().count('G')
    N = combined_fasta.upper().count('N')
    total = A + T + C + G

    sorted_lengths = sorted(lengths, reverse=True)
    middle_point = sum(lengths)/2
    summed = 0
    index = 0
    while (summed < middle_point):
        summed += sorted_lengths[index]
        index += 1

    out_dict[fasta] = {"size": total+N, "det_bases": total, "contigs": contig_count, "ATp": (A + T)/total*100, "nN": N, "nGaps": nGaps_count, "N50": sorted_lengths[index]}
pd.DataFrame(out_dict).to_csv(out_file, index=True)


