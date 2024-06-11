import pandas as pd
import polars as pl
import json
from tqdm import tqdm

def contig_sizes(depth_file):
    sizes = {}
    for c in set(depth_file[0].values):
        sizes[c] = depth_file[depth_file[0] == c][1].max()
    return sizes

def get_region_indices(parsed_contigs, interval):
    ri = {}
    for c in parsed_contigs:
        ri[c] = [x for x in range(1, parsed_contigs[c], interval)]
        ri[c].append(parsed_contigs[c])
    return ri

def generate_regions(r_indices):
    r = {x: {} for x in r_indices}
    for c in r_indices:
        for i in range(len(r_indices[c])-1):
            region = "region_" + str(i+1)
            start  = r_indices[c][i]
            stop   = r_indices[c][i+1]
            r[c][region] = {"start": start, "stop": stop, "cov": 0}
    return r

def get_coverage(covs, regs, csv):
    tmp_regs = regs
    for c in tqdm(regs):
        for r in tqdm(tmp_regs[c]):
            start = regs[c][r]["start"]
            stop  = regs[c][r]["stop"]
            size  = stop - start # 2500 except for last region per contig
            #only read in current region with polars
            
            q = (pl.scan_csv(csv, sep="\t", has_header=False)
                .filter((pl.col("column_1") == c)     &
                        (pl.col("column_2") >= start) &
                        (pl.col("column_2")  < stop)))
            filt = q.collect()
            
            # Sum coverage in region and divide by region size
            avg_cov = str(filt["column_3"].sum()/size)
            #cov   = covs[covs[0] == c][covs[1] >= start][covs[1]<stop][2].sum()
            #avg_cov = cov/size
            tmp_regs[c][r]["cov"] = avg_cov
    return tmp_regs


# Input files generated with samtools depth -aa *bam
illuDepth = "samtools_output/illumina_depthPerPos.txt"
nanoDepth = "samtools_output/nanopore_depthPerPos.txt"
mRNADepth = "samtools_output/mRNA_samtoolsDepth_repSum.txt"

illu = pd.read_csv(illuDepth, 
                    sep="\t", header=None)
nano = pd.read_csv(nanoDepth, 
                    sep="\t", header=None)
mRNA = pd.read_csv(mRNADepth,
                   sep="\t", header=None)

# Generate regions for coverage calculations
c_sizes          = contig_sizes(illu)
regions_indices  = get_region_indices(c_sizes, 2500) 
regions          = generate_regions(regions_indices)

# Get average coverage per region and save output as dicts

illu_cov_regions = get_coverage(illu, regions, illuDepth)
with open("illu_cov_regions.py", "w") as fout:
    fout.write("illu_cov_regions = " + str(illu_cov_regions))
nano_cov_regions = get_coverage(nano, regions, nanoDepth)
with open("nano_cov_regions.py", "w") as fout:
    fout.write("nano_cov_regions = " + str(nano_cov_regions))
mRNA_cov_regions = get_coverage(mRNA, regions, mRNADepth)
with open("mRNA_cov_regions.py", "w") as fout:
    fout.write("mRNA_cov_regions = " + str(mRNA_cov_regions))

# make summary table from cov outputs
from illu_cov_regions import illu_cov_regions
from nano_cov_regions import nano_cov_regions
from mRNA_cov_regions import mRNA_cov_regions
header = ["Contig", "Start", "Stop", "Illumina", "Nanopore", "mRNA"]

with open("regions_cov.txt", "w") as fout:
    fout.write("\t".join(header)+"\n")
    for c in illu_cov_regions:
        for r in illu_cov_regions[c]:
            fout.write("\t".join([c, str(illu_cov_regions[c][r]["start"]),
                                     str(illu_cov_regions[c][r]["stop"]-1),
                                     str(illu_cov_regions[c][r]["cov"]),
                                     str(nano_cov_regions[c][r]["cov"]),
                                     str(mRNA_cov_regions[c][r]["cov"]),
                                     "\n"]))