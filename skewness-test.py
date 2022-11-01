import scipy.stats as stats
import os
import pandas as pd
import statistics

def tabluar_skewness_test(model):
    '''
    Script to perform a Person median skewness test on the input model.
    `model`: filepath to the input model
    
    Outputs skewness test results to a list in directory defined by the `filepath` global variable called 'skewness-
    results.csv'. Note, if a file with this name already exists, this method will append to that file without 
    overwriting.
    
    The output list is formatted:
    [`model`, skewness value]  
    If more output variables of the scipy.stats.linregress function are required, these can be added by altering line 
    33.
    '''
    
    outfile = os.path.join(filepath, 'skewness-results.csv')
    
    importer = pd.read_csv(model)
    df = pd.DataFrame(data=importer)
    
    skew = stats.skew(df['accuracy'], axis=0)
    
    name = os.path.split(model)
    
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    outfilewriter = open(outfile, "a", encoding="utf-8")
    
    outfilewriter.write(f'[{name[1]}, {skew}]\n')
    
    outfilewriter.close()
