#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 13:11:15 2018

@author: miguelrebelo
"""

# Pandas for managing datasets
import pandas as pd

# set pandas max rows    
pd.options.display.max_rows = 10000
pd.options.display.max_columns = 10000
pd.options.display.width = 10000

# read positions file
pos = pd.read_csv('/Users/miguelrebelo/Desktop/positionsE_W_99.txt', sep="\t")

# Read gff file
file = pd.read_csv('/Users/miguelrebelo/Desktop/cribi_V1_on_assembly_12X_V2.gff', sep="	")

# only genes
genes_only = file['gene']=='gene'
genes = file[genes_only]

with open('/Users/miguelrebelo/Desktop/myGenes.txt', 'w') as f:
    
    # start a loop through the target positions
    for index, row in pos.iterrows():
        # identify the chr 
        cut=genes.loc[genes['chr']==str(row['chr'])]
        # compute interval
        position_end=row['midpos']+50000
        position_start=row['midpos']-50000
        # cut withi the interval
        gen_end=cut.loc[cut['end']<=position_end]
        gen=gen_end.loc[gen_end['start']>=position_start]
        # print selected rows of the gff file
        print(gen['id'], file=f)

myGenes=pd.read_csv('/Users/miguelrebelo/Desktop/myGenes.txt', sep="\t")
with open('/Users/miguelrebelo/Desktop/UniqueGenes.txt', 'w') as g:
    unique=myGenes.drop_duplicates()
    print(unique,file=g)