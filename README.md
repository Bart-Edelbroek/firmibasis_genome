# Analysis of Dictyostelium firmibasis genome
Repository to accompany the analysis of the sequenced, assembled and annotated <i>Dictyostelium firmibasis</i> JAVFKY000000000 assembly (http://identifiers.org/ncbi/insdc:JAVFKY000000000). 

The main analysis and generation of the plots is in <b>firmibasis_analysis.Rmd</b>. All generated plots are also available in the plots folder. To enable the calculation of the gDNA and mRNA coverage over the genome, the mapped reads are counted over regular intervals and the counts are available in the <b>count_regions</b> folder. For example, the number of illumina short read gDNA sequences are counted in count_regions/regions_gDNA_illumina.txt. Other files needed for the analysis are located in the different folders.
