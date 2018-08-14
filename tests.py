import bayes_demo as bd

M = bd.BetaBinomial()
MM = bd.BetaBinomial(a=1, b=1, n=100, p=0.5)

bd.plot_model(MM, show=False, save=False)

inputs = [(1, 1), (0.6, 0.6), (5, 5), (1, 5)]
models = bd.get_models(inputs, n=100, p=0.5)

bd.plot_models(models, show=False, save=False)

print('Tests Successful')
