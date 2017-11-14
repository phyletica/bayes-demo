import matplotlib.pyplot as plt

def matplotlib(m):
    plt.plot(
        m.x, m.like_df,
        color='#1F77B4', linestyle=':', linewidth=1.0,
        label=r'$Likelihood\/\/p(D|\theta$)')
    plt.plot(
        m.x, m.prior_df, color='#1F77B4', linestyle='--',
        linewidth=1.0, label=r'$Prior\/\/p(\theta)$'
    )
    plt.plot(
        m.x, m.post_df, color='#1F77B4', linestyle='-',
        linewidth=1.0, label=r'$Posterior\/\/p(\theta|D)$'
    )
    plt.title(r'$\alpha={},\/\/\beta={}$'.format(m.a, m.b))
    plt.xlabel(r'$\theta$', fontsize=10)
    plt.xticks([0,1], )
    plt.tick_params(labelsize=6)
    plt.ylabel(r'Density', fontsize=10)
    plt.xlim(left=0, right=1)
    plt.xlim(left=0, right=1)
    plt.ylim(bottom=0)
    plt.legend()
    plt.show()
