import matplotlib as mpl
import matplotlib.pyplot as plt

def dark_mpl():
    mpl.rcParams['figure.figsize'] = [8, 6]
    plt.style.use(['dark_background'])
    plt.rcParams['axes.spines.top']=False
    plt.rcParams['axes.spines.right']=False
    
    # font = {'family' : 'Arial',
#        'weight' : 'regular',
#        'size'   : font_size}
    
#     plt.rc('font', **font)