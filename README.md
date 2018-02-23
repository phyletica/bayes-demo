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
##### BetaBinomial()
Binomial model with from a beta prior distribution

Arguments:
<ul style="list-style: none;">
    <li>a: alpha parameter for beta prior distribution, defaults to 1</li>
    <li>b: beta parameter for beta prior distribution, defaults to 1</li>
    <li>n: sample size of simulated, defaults to 100</li>
    <li>p: proportion of successes, defaults to 0.5</li>
    <li>params: number of parameters to draw from probability density functions</li>
</ul>

Class attributes:
<ul style="list-style: none;">
    <li>a: alpha shape parameter of model</li>
    <li>b: beta shape parameter of model</li>
    <li>n: sample size of model</li>
    <li>p: proportion success of model</li>
    <li>x: array between 0 and 1 with length given by params argument</li>
    <li>like_df: likelihood density function of array x</li>
    <li>prior_df: prior probability density function of array x</li>
    <li>post_df: posterior probability density function of array x</li>
    <li>like: likelihood of model</li>
    <li>prior: prior probability of model</li>
    <li>post: posterior probability of model</li>
    <li>marginal: marginal likelihood of model</li>
</ul>

##### get_models()
Compute multiple binomial models

Arguments:
<ul style="list-style: none;">
    <li>shape_params: List of tuples containing alpha and beta shape parameters.</li>
        <ul style="list-style:none;">
            <li>Example: [(a1, b1), (a2, b2), (a3, b3)]</li>
        </ul>
    <li>a: alpha parameter for beta prior distribution, defaults to 1</li>
    <li>b: beta parameter for beta prior distribution, defaults to 1</li>
    <li>n: sample size of simulated, defaults to 100</li>
    <li>p: proportion of successes, defaults to 0.5</li>
    <li>params: number of parameters to draw from probability density functions</li>
</ul>

##### plot_model()
Plot probability densities functions of a binomial model instance

Arguments:
<ul style="list-style: none;">
    <li>M: BetaBinomial class instance</li>
    <li>show: boolean, show plot, defaults to True</li>
    <li>save: boolean, save plot to plot.pdf, defaults to False</li>
    <li>format: output file format, defaults to 'png'</li>
</ul>

##### plot_models()
Plot probability density functions and marginal likelihoods of multiple models

Arguments:
<ul style="list-style: none;">
    <li>models: list of 4 betabinomial model class instances</li>
    <li>show: boolean, show graph, defaults to True</li>
    <li>save: boolean, save plot to grid-plot.pdf, defaults to False</li>
    <li>format: output file format, defaults to 'png'</li>
</ul>
