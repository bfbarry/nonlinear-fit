from sklearn.preprocessing import StandardScaler, MinMaxScaler, KBinsDiscretizer
import numpy as np

def rescale(d, scalers=['zscore', 'minmax']):
    if len(d.shape) < 2: # for 1d labels
        d = np.array(d).reshape(-1, 1) # leads to DataConversionWarning?
    if 'zscore' in scalers:
        d = StandardScaler().fit_transform(d)
    if 'minmax' in scalers:
        d = MinMaxScaler().fit_transform(d)

    return d

def discretize_target(pos, neg, nbins):
    """
    Bins continuous target variables into bins using KBinsDiscretizer
        pos: dataframe where target values are > 0
        neg: " " are False
        nbins: number of bins for positive samples. Total # bins in final df will be nbins+1
    """
    kbd = KBinsDiscretizer(n_bins=nbins-1, encode='ordinal', strategy='quantile') #subtract 1 from nbins as these are the # bins for positive targets
    
    y1 = np.array(pos.weeks_to_prepayment).reshape(-1, 1) # needs to be 2d for transformer
    y1 = kbd.fit_transform(y1).T.ravel()
    y0 = neg.weeks_to_prepayment.apply(lambda x: 3).to_numpy() # f(-1) -> 9, a safe score
    y = np.append(y1,y0).astype(int)
    X = pos.append(neg).drop(['weeks_to_prepayment'],axis=1) 
    
    return X,y