# Bayes Demo

Tool for calculating the posterior probability distribution and marginal likelihood of a parameter from a binomial distribution using a beta prior probability distribution.

Used to compute Figure 1 in:
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

### Python Module


#### Examples
##### Compute and plot single model
Compute probability distributions and marginal likelihood of a single model and plot the probability distributions
```python
import bayes_demo as bd

M = bd.BetaBinomial()

MM = bd.BetaBinomial(a=0.5, b=0.5, n=100, p=0.5)

bd.plot_model(MM)
```
![](/img/plot.png)


##### Compute and plot multiple models
Compute probability distributions and marginal likelihood of a multiple models and plot the probability distributions and marginal likelihoods of each model
```python
import bayes_demo as bd

inputs = [(1, 1), (0.6, 0.6), (5, 5), (1, 5)]

models = bd.get_models(inputs, n=100, p=0.5)

bd.plot_models(models)
```
![](/img/grid-plot.png)
