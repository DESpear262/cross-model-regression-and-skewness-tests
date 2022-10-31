mods = []
for model, checkpoints in models.items():
    for checkpoint in checkpoints:
        filename = os.path.join(filepath, f'memorization_results_{model}-{checkpoint}.csv')
        mods.append(filename)
        
for mod1 in mods:
    for mod2 in mods:
        tabluar_regression_of_cross_model_memorization(mod1, mod2)

###########################################################################################

for model, checkpoints in models.items():
    for checkpoint in checkpoints:
        filename = os.path.join(filepath, f'memorization_results_{model}-{checkpoint}.csv')
        tabluar_skewness_test(filename)