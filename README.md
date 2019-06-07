# FindMyGenes
Helpfull Python Script for finding genes in each genomic window.

With the detection of selection signatures, it was necessary to convert positional windows in the genome into actual genes.

This script was made specifically to work with '.gff' files. The ‘.gff’ file format contains condensed information about the genomic regions, genes, CDS, RNA, and their positions within the chromosomes.

This workes by feeding a file with a column for chromosomes (chr), another for mid-positions (midpos) (that locate the window), and the ‘.gff’ file.

The script dumpes a text file with the lines found on the ‘.gff’ file for each window searched. Then, it removes the duplicate genes for subsequent gene analysis, creating a new file.
