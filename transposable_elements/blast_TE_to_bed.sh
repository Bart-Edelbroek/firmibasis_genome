tblastx -query TE_amoebozoa_500_ddis.fa -db ../../genome.nextpolish.modHeaders.fasta -outfmt "6 sseqid sstart send qseqid length evalue bitscore" -evalue 10E-15 > out.txt
Rscript output_to_gff.R out.txt annot_TEmerged.gff
