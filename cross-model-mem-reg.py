import scipy.stats as stats
import os
import pandas as pd

def tabluar_regression_of_cross_model_memorization(model1, model2):
    '''
    Script to regress the memorization proportion of the index values of model 1 on the memorization proportion 
    of index values in model 2.
    `model1`: filepath to the dependent variable model
    `model2`: filepath to the independent variable model
    
    Outputs regression results to a list in directory defined by the `filepath` global variable called 'cross-model-
    regression-results.csv'. Note, if a file with this name already exists, this method will append to that file 
    without overwriting.
    
    The output list is formatted:
        [`model1`, `model2`, OLS coefficent, p-value]
        [`modelA`, `modelB`, OLS coefficent, p-value]
        ...
    
    If more output variables of the scipy.stats.linregress function are required, these can be added by altering line 
    40.
    '''
    
    if model1 is not model2:
        outfile = os.path.join(filepath, 'cross-model-regression-results.csv')
    
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        outfilewriter = open(outfile, "a", encoding="utf-8")
    
        importer = pd.read_csv(model1)
        df1 = pd.DataFrame(data=importer)
        
        importer = pd.read_csv(model2)
        df2 = pd.DataFrame(data=importer)

        reg = stats.linregress(df1['accuracy'], df2['accuracy'])
        name1 = os.path.split(model1)
        name2 = os.path.split(model2)
        outfilewriter.write(f'[{name1[1]}, {name2[1]}, {reg.slope}, {reg.pvalue}]\n')
        
        outfilewriter.close()
        
    else:
        print("Warning: input models are identical. No output written.")