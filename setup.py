import setuptools as st

st.setup(
    name='bayes-demo',
    version='1.0',
    description='A package for calculating and plotting the posterior and marginal likelihood for a binomial likelihood density function weighted by a beta prior density function',
    url='https://github.com/phyletica/bayes-demo',
    author='Kerry A. Cobb and Jamie R. Oaks',
    author_email='cobbkerry@gmail.com',
    license='MIT',
    packages=st.find_packages(),
    install_requires=[
        'click',
        'numpy',
        'scipy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts':[
            'beta-binomial=bayes_demo.cli:cli'
        ]
    },
)
