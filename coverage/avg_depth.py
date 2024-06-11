import pandas as pd

def size_depth(samdepth):
    contigs = {}
    depths = {}
    with open(samdepth) as fin:
        for line in fin:
            c, p, d = line.strip("\n").split("\t")
            if c not in contigs:
                contigs[c] = 0
                depths[c]   = 0
            contigs[c] = int(p) # last pos per contig equals contig size
            depths[c]  += float(d) # Sum depth per contig
    size  = sum(contigs.values()) # Total assembly size
    depth = sum(depths.values()) # Sum of depth at all positions
    return str(size), str(depth), str(depth/size)

#gDNA data
ill_size, ill_depth, ill_avg_cov = size_depth("samtools_output/illumina_depthPerPos.txt")
nan_size, nan_depth, nan_avg_cov = size_depth("samtools_output/nanopore_depthPerPos.txt")
#mRNA data
mRNA = pd.read_csv("samtools_output/mRNA_samtoolsDepth.txt", 
                  sep="\t", header=None)
#sum coverage over replicates
mRNA_sum = mRNA[[0,1]]
mRNA_sum[2] = mRNA[[2,3,4,5,6,7,8,9,10]].sum(axis=1)
mRNA_sum.to_csv("samtools_output/mRNA_samtoolsDepth_repSum.txt", sep="\t",
                header=None, index=None)
#Calculate mRNA cov
mRNA_size, mRNA_depth, mRNA_avg_cov = size_depth("samtools_output/mRNA_samtoolsDepth_repSum.txt")

#Write avg cov table 
with open("avg_depth.txt", "w") as fout:
    fout.write("\t".join(["Data", "AssemblySize", "SumDepth", "AvgCov", "\n"]))
    fout.write("\t".join(["Illum", ill_size, ill_depth, ill_avg_cov, "\n"]))
    fout.write("\t".join(["Nano", nan_size, nan_depth, nan_avg_cov, "\n"]))
    fout.write("\t".join(["mRNA", mRNA_size, mRNA_depth, mRNA_avg_cov, "\n"]))

