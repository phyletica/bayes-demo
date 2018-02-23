"""
Module for plotting the probability density functions of a binomial model
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

def plot_model(M, show=True, save=False, format='png'):
    """Plot probability densities functions of a binomial model instance

        Parameters:
            M: betabinomial class instance
            show: boolean, show plot, defaults to True
            save: boolean, save plot to plot.pdf, defaults to False
            format: output file format, defaults to 'png'


        Examples:
            M = bd.BetaBinomial()
            bd.plot_model(M, show=False)
    """

    plt.plot(
        M.x, M.like_df,
        color='#1F77B4', linestyle=':', linewidth=1.0,
        label=r'$Likelihood\/\/p(D|\theta$)')
    plt.plot(
        M.x, M.prior_df, color='#1F77B4', linestyle='--',
        linewidth=1.0, label=r'$Prior\/\/p(\theta)$'
    )
    plt.plot(
        M.x, M.post_df, color='#1F77B4', linestyle='-',
        linewidth=1.0, label=r'$Posterior\/\/p(\theta|D)$'
    )
    plt.title(r'$\alpha={},\/\/\beta={}$'.format(M.a, M.b))
    plt.xlabel(r'$\theta$', fontsize=10)
    plt.xticks([0,1], )
    plt.tick_params(labelsize=6)
    plt.ylabel(r'Density', fontsize=10)
    plt.xlim(left=0, right=1)
    plt.xlim(left=0, right=1)
    plt.ylim(bottom=0)
    plt.legend()
    if save:
        plt.savefig('plot.{}'.format(format), dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=format,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None)
    if show:
        plt.show()

def plot_models(models, show=True, save=False, format='png'):
    """Plot probability density functions of multiple models

    Parameters:
        models: list of 4 betabinomial model class instances
        show: boolean, show graph, defaults to True
        save: boolean, save plot to grid-plot.pdf, defaults to False
        format: output file format, defaults to 'png'

    Examples:
        import bayes_demo as bd
        inputs = [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75), (5, 5)]
        models = bd.get_models(inputs, n=1000, p=0.25)
        bd.plot_models(models)

    """
    if len(models) != 4:
        sys.exit('<br>Error in plot_models!<br><br>Input must be a list of 4 betabinomial class instances<br>')
    fig, ax = plt.subplots(nrows=2, ncols=3, figsize=None, frameon=True)
    a1 = ax[0, 0]
    a2 = ax[0, 1]
    a3 = ax[0, 2]
    a4 = ax[1, 0]
    a5 = ax[1, 1]
    a6 = ax[1, 2]
    model_axes = [[a1, models[0]], [a2, models[1]], [a4, models[2]], [a5, models[3]]]
    for ax, m in model_axes:
        ax.plot(
            m.x, m.like_df, color='#1F77B4', linestyle=':',
            linewidth=1.0, label=r'$Likelihood\/\/p(D|\theta$)'
        )
        ax.plot(
            m.x, m.prior_df, color='#1F77B4', linestyle='--',
            linewidth=1.0, label=r'$Prior\/\/p(\theta)$'
        )
        ax.plot(
            m.x, m.post_df, color='#1F77B4', linestyle='-',
            linewidth=1.0, label=r'$Posterior\/\/p(\theta|D)$'
        )
        ax.set_title(r'$M_{}$'.format(m.name), fontsize=12, loc='left')
        ax.set_xlabel(r'$\theta$', fontsize=10)
        ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
        ax.tick_params(labelsize=6)
        ax.set_ylabel(r'Density', fontsize=10)
        ax.set_xlim(left=-.01, right=1.01)
        ax.set_ylim(bottom=-.1)
        ax.text(
        .76, .95,
        r'$\alpha={},\/\/\beta={}$'.format(m.a, m.b),
        ha='center',
        va='center',
        transform = ax.transAxes,
        fontsize=6
        )
        a2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        a3.axis('off')

    a6.bar(np.arange(1, len(models)+1), [m.marginal for m in models])
    a6.set_xticks([1,2,3,4])
    a6.set_title(r'Marginal Likelihoods', fontsize=10)
    a6.set_xticklabels([r'$M_{}$'.format(m.name) for m in models], fontsize=10)
    a6.set_ylabel(r'P(D)', fontsize=10)
    a6.tick_params(labelsize=6)

    plt.tight_layout(pad=1, w_pad=0, h_pad=0)
    if save:
        plt.savefig('grid-plot.{}'.format(format), dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=format,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None)
    if show:
        plt.show()
