# Analysis of *Dictyostelium firmibasis* genome assembly
Repository to accompany the analysis of the sequenced, assembled and annotated *Dictyostelium firmibasis* JAVFKY000000000 assembly (http://identifiers.org/ncbi/insdc:JAVFKY000000000). 
   
### Analysis and plots
The main analysis and generation of the plots is in **firmibasis_analysis.Rmd**. All generated plots are also available in the plots folder. Other files needed for the analysis are located in the different folders.

### Calculate coverage over genome
The gDNA and mRNA coverage over the genome was calculated using *samtools depth -aa* on the mapped .bam files. The average depth over the genome was calculated with **coverage/avg_depth.py**. To enable visualisation of the coverage over the genome, the mean coverage was calculated over 2.5 kbp regular intervals with the **coverage/cov_per_region.py** python script, resulting in the **coverage/regions_cov.txt** table. For the sRNA reads, the number of mapped reads was calculated with featureCounts over regular intervals.


### Genome metrics python script
Genome metrics were calculated using **analyze_genomes.py**, which outputs the genome size, number of determined and undetermined bases, number of contigs, AT%, number of gaps (consecutive stretches of N's of a given size), and N50 contiguity. Use **-f** for the input genomes (multi-line fasta files) and **-o** for the output file (comma separated). Prerequisites are biopython, numpy and pandas.

Example usage for the two *D. firmibasis* genome assemblies:  
$python analyze_genomes.py -f [ASM27748v1.fna](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000277485.1/) [ASM3616959v1.fna](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_036169595.1/) -o out.csv  
The example output is included in the repository. 

