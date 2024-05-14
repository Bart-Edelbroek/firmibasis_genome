featureCounts -T 4 -O --fraction -M --fraction -p -t 'region' -g 'ID' -a ddis_regions.gff -o regions_ddis.txt star_map_ddis/*.bam
featureCounts -T 4 -O --fraction -M --fraction -p -t 'region' -g 'ID' -a dfir_regions.gff -o regions_dfir.txt star_map_dfir/*.bam
