# Bayes Demo

Tool for calculating the posterior probability distribution and marginal likelihood of a parameter from a binomial distribution using a beta prior probability distribution.

Used to compute Figure 1 in
"Jamie R. Oaks, Kerry A. Cobb, Vladimir N. Minin, and Adam D. Leaché. 2018. Marginal likelihoods in phylogenetics: a review of methods and applications."

An interactive Javascript implementation is available at [https://kerrycobb.github.io/beta-binomial-web-demo/](https://kerrycobb.github.io/beta-binomial-web-demo/)

## Installation
```bash
pip install git+https://github.com/phyletica/bayes-demo
```

## Usage
### Command Line
```bash
bayes-demo --help

```

### Python Modules
#### Examples
##### Compute and plot single model
Compute probability distributions and marginal likelihood of a single model and plot the probability distributions
```python
import bayes_demo as bd

M = bd.BetaBinomial()

MM = bd.BetaBinomial(a=0.5, b=0.5, n=100, p=0.5)

bd.plot_model(MM)
```
Output:

![](/img/plot.png)

##### Compute and plot multiple models
Compute probability distributions and marginal likelihood of a multiple models and plot the probability distributions and marginal likelihoods of each model
```python
import bayes_demo as bd

inputs = [(1, 1), (0.6, 0.6), (5, 5), (1, 5)]

models = bd.get_models(inputs, n=100, p=0.5)

bd.plot_models(models)
```
Output:

![](/img/grid-plot.png)

#### Documentation
```
BetaBinomial(a=1, b=1, n=100, p=0.5, params=1000)
```
Binomial model with a beta prior distribution

Arguments:
- a: alpha parameter for beta prior distribution, defaults to 1
- b: beta parameter for beta prior distribution, defaults to 1
- n: sample size of simulated, defaults to 100
- p: proportion of successes, defaults to 0.5
- params: number of parameters to draw from probability density functions

Class attributes:
- a: alpha shape parameter of model
- b: beta shape parameter of model
- n: sample size of model
- p: proportion success of model
- x: array between 0 and 1 with length given by params argument
- like_df: likelihood density function of array x
- prior_df: prior probability density function of array x
- post_df: posterior probability density function of array x
- like: likelihood of model
- prior: prior probability of model
- post: posterior probability of model
- marginal: marginal likelihood of model


```
get_models(shape_params, n=100, p=0.5, params=1000)
```
Compute multiple binomial models

Arguments:
- shape_params: List of tuples containing alpha and beta shape parameters.  
    - Example: [(a1, b1), (a2, b2), (a3, b3)]
- a: alpha parameter for beta prior distribution, defaults to 1
- b: beta parameter for beta prior distribution, defaults to 1
- n: sample size of simulated, defaults to 100
- p: proportion of successes, defaults to 0.5
- params: number of parameters to draw from probability density functions

```
plot_model(M, show=True, save=False, format='png')
```
Plot probability density functions of a binomial model instance

Arguments:
- M: BetaBinomial class instance
- show: boolean, show plot, defaults to True
- save: boolean, save plot to plot.pdf, defaults to False
- format: output file format, defaults to 'png'

```
plot_models(models, show=True, save=False, format='png')
```
Plot probability density functions and marginal likelihoods of multiple models

Arguments:
- models: list of 4 BetaBinomial model instances
- show: boolean, show graph, defaults to True
- save: boolean, save plot to grid-plot.pdf, defaults to False
- format: output file format, defaults to 'png'
