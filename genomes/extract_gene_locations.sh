awk '$3 == "gene" { print $1,$4,$5,substr($9,4,12) }' ../05_reference_genomes/ddis_combined_annotation.gff > ddis_genes_location.txt
awk '$3 == "gene" { print $1,$4,$5,substr($9,4,9) }' ../05_reference_genomes/dfir_combined_annotation.gff > dfir_genes_location.txt
awk -F'\t|product=' '$3 == "tRNA" { print $1,$4,$5,substr($10,6,3) }' ../05_reference_genomes/ddis_combined_annotation.gff > ddis_tRNAs_location.txt
awk -F'\t|isotype=' '$3 == "tRNA" { print $1,$4,$5,substr($10,1,3) }' ../05_reference_genomes/dfir_combined_annotation.gff > dfir_tRNAs_location.txt
grep "_rRNA" ../05_reference_genomes/dfir_combined_annotation.gff | awk -F'\t|Name=' '{ print $1,$4,$5,substr($10,1,9) }' > dfir_rRNA_location.txt
