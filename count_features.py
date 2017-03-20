#!/usr/bin/env python

import click

def count_features(inputfile, feature_type):
    count = 0
    for line in inputfile:
        if line.startswith('#'):
            continue
        stripped_line = line.rstrip('\n')
        fields = stripped_line.split('\t')
        feature_type_field = fields[2]
        if feature_type_field == feature_type:
            count += 1
    return(count)

@click.command()
@click.argument('filename')
def count_genes(filename):
    with open(filename) as input:
        gene_count = count_features(input, 'gene')
        # cds_count = count_features(input, 'CDS')
        print('gene_count:', gene_count)
        # print('cds_count:', cds_count)

count_genes()
