"""
random k-fold cross-validation is a simple way to dividing data into a few parts. 
We will train the model on some of these parts and test on the remaining parts. 
So k-fold mean that we will divided data into k different sets which are exclusive
of each other. 

"""


import pandas as pd 
from sklearn import model_selection
def kfold_cross_validation(input, output):
    df = df.read_csv(input)
    
    df['kfold'] = -1 
    
    df = df.sample(frac=1).reset_index(drop=True)
    
    kf = model_selection.KFold(n_splits=5)
    
    for fold, (trn_, val_) in enumerate(kf.split(X=df)):
        df.loc[val_, 'kfold'] = fold
        
    df.to_csv(output , index=False)
