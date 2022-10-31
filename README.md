# Cross-model regression and skewness tests

cross-model-mem-reg is a method which takes in two datasets from the provided models (as in the memorization Jupyter Notebook) and regresses the accuracy of one on the other. This method will throw a non-fatal warning if the input files have identical names, but will not check if the underlying data is identical.
skewness-test.py is a method which takes in a model and runs a skewness test on the accuracy of that model.
test-code.py is the code I used to test these methods with the sample model provided. They should be fully compatible with the existing Jupyter notebook, but they are poorly optimized. In particular, the test code for cross-model-mem-reg runs redundant regressions of model x on model y as well as regressions of y on x. 
