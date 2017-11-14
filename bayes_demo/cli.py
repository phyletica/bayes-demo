#!/usr/bin/env python3

import click
import bayes_demo as bd

@click.command()
@click.option('--alpha', '-a', default=1, type=float, help='Alpha shape parameter for beta prior probability distribution')
@click.option('--beta', '-b', default=1, type=float, help='Beta shape parameter for beta prior probability distribution')
@click.option('--sample_size', '-n', default=100, type=int, help='Size of binomial sample')
@click.option('--proportion', '-p', default=0.5, type=float, help='Proportion of binomial sample success')

def cli(alpha, beta, sample_size, proportion):
    '''
    Description:
    '''
    m = bd.BetaBinomial(a=alpha, b=beta, n=sample_size, p=proportion)

    print(
        '''
        Likelihood Density = {}
        Prior Density = {}
        Posterior Density = {}
        Marginal Likelihood = {}
        '''.format(m.like, m.prior, m.post, m.marginal)
    )

    bd.matplotlib(m)

if __name__=='__main__':
    cli()
