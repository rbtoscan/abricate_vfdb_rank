

'''
### conda install and activate
conda install -c conda-forge -c bioconda -c defaults abricate
conda activate abricate

# run abricate with virulent database
abricate --db vfdb <fasta> > <abricate_output.tsv>

# process output, sorting abricate contigs by number of virulent genes, coverage, identiy
python proc_abricate.py <abricate_output.tsv> <rank_contigs_virulence.tsv>
'''

