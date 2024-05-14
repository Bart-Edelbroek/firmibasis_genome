options(scipen = 999)
dfir_samtools_index <- read.table("../genomes/dfir_genome.fa.fai", sep = "\t")
firmibasis <- data.frame(name = dfir_samtools_index[,1],
                         start = rep(0,nrow(dfir_samtools_index)),
                         end = dfir_samtools_index[,2])
firmibasis$name <- factor(firmibasis$name, levels = firmibasis$name)
firmibasis$alias <- c(paste0("Dfir_chr",1:6),"","","Dfir_mtDNA",rep("",3))
dfir_regions <- data.frame()
for (i in 1:nrow(dfir_samtools_index)) {
  sequence_region <- seq(1,dfir_samtools_index[i,2], 2500)
  dfir_regions <- rbind(dfir_regions,
                        data.frame(chr = dfir_samtools_index[i,1],
                                   V2 = ".",
                                   V3 = "region",
                                   start = sequence_region,
                                   end = sequence_region+2499,
                                   V6 = ".",
                                   V7 = "+",
                                   V8 = ".",
                                   name = paste0("ID=",dfir_samtools_index[i,1],":",sequence_region,"..",sequence_region+2499)
                        ))
}
write.table(dfir_regions, "dfir_regions.gff", quote = FALSE, sep = "\t", col.names = F, row.names = F)

ddis_samtools_index <- read.table("../genomes/ddis_genome.fasta.fai", sep = "\t")[c(5:11,1:4),]
discoideum <- data.frame(name = ddis_samtools_index[,1],
                         start = rep(0,nrow(ddis_samtools_index)),
                         end = ddis_samtools_index[,2])
discoideum$name <- factor(discoideum$name, levels = discoideum$name)
ddis_regions <- data.frame()
for (i in 1:nrow(ddis_samtools_index)) {
  sequence_region <- seq(1,ddis_samtools_index[i,2], 2500)
  ddis_regions <- rbind(ddis_regions,
                        data.frame(chr = ddis_samtools_index[i,1],
                                   V2 = ".",
                                   V3 = "region",
                                   start = sequence_region,
                                   end = sequence_region+2499,
                                   V6 = ".",
                                   V7 = "+",
                                   V8 = ".",
                                   name = paste0("ID=",ddis_samtools_index[i,1],":",sequence_region,"..",sequence_region+2499)
                        ))
}
write.table(ddis_regions, "ddis_regions.gff", quote = FALSE, sep = "\t", col.names = F, row.names = F)
