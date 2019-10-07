import matplotlib.pyplot as plt
import seaborn as sns
from .utils import features_target_split
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro, normaltest

def get_class_counts(df, target, display='all', subtitle=None):
   '''
   Plots a countplot of column.
   display options are number, percent or all
   '''
   fig = plt.figure(figsize=(7,7))
   g = sns.countplot(df[target])
   for p in g.patches:
       if display == 'all':
           g.annotate ('{}\n\n{:.2f}%\n'.format (p.get_height(), 100*p.get_height()/len(df)), (p.get_x(), p.get_height()+10), bbox=dict(boxstyle='round', alpha=0.1, color='grey'))
       elif display == 'number':
           g.annotate('{}'.format(p.get_height()),(p.get_x(), p.get_height()+10), bbox=dict(boxstyle='round', alpha=0.1, color='grey'))
       elif display == 'percent':
           g.annotate('{:.2f}%'.format(100*p.get_height()/len(df)),(p.get_x(), p.get_x(), p.get_height()+10),bbox = dict(boxstyle='round', alpha=0.1, color='grey') )
       else:
           raise ValueError('Display must be either of number, percent or all')
   g.set_ylim(0, max([p.get_height()*1.15 for p in g.patches]))
   g.text (x=0.5, y=1.07, s=f'Count plot of {target}', fontsize=16, weight='bold', ha='center', va='bottom', transform=g.transAxes, color='navy')
   if subtitle:
       g.text(x=0.5, y=1.03, s=f'{subtitle}', fontsize=12, alpha=0.75, ha='center', va ='bottom', transform=g.transAxes, color='darkblue')
   if any ([p.get_height()/len(df)<0.2 for p in g.patches]):
       fig.text(x=1, y=0.5, s='Imbalanced dataset', bbox=dict(boxstyle='round', color='red', alpha=0.7), color='white', fontsize=14)
   else:
       fig.text(x=1, y=0.5, s='Balanced dataset', bbox = dict(boxstyle='round', color='green', alpha=0.7), color='white', fontsize=14)
   plt.show()



def normality_plots(df, col):
    """
    Plots distplot, QQ-plot and runs Shapiro test for verifying Gaussian distribution
    """

    fig = plt.figure(figsize=(15, 5))
    shapiro_p = round(shapiro(df[col])[1], 2)
    normaltest_p = round(normaltest(df[col])[1], 2)
    plt.subplot(1, 3, 1)
    plt.title('Histogram for '+col, color='navy', fontsize=12)
    plt.hist(df[col])
    plt.subplot(1, 3, 2)
    plt.title('Q-Q Plot for '+col, color='brown', fontsize=12)
    qqplot(df[col], line='s', ax=plt.subplot(1, 3, 2))
    plt.subplot(1, 3, 3)
    plt.title('Normality Test Results for '+col, color='olive', fontsize=12)
    plt.plot([shapiro_p, normaltest_p], linestyle=' ', marker='x')
    plt.text(x=0.2, y=0.5, s='Shapiro\np value\n'+str(shapiro_p))
    plt.text(x=0.6, y=0.5, s='Normaltest\np value\n'+str(normaltest_p))
    plt.ylim((0, 1))
    plt.hlines(y=0.05, color='r', xmin=0, xmax=1)
    fig.text(x=0.5, y=1.07, s=f'Normality Test for {col}', fontsize=16, weight='bold',
             ha='center', va='bottom', color='navy')

    if all(st > 0.05 for st in [shapiro_p, normaltest_p]):
        fig.text(x=0.5, y=1.03, s=f'Distribution is Gaussian', fontsize=14,
             ha='center', va='bottom', color='darkblue')
    else:
        fig.text(x=0.5, y=1.03, s=f'Distribution is Skewed', fontsize=14,
             ha='center', va='bottom', color='darkblue')

    #plt.suptitle('Normality Test for '+col, fontsize=16, color='b')
    plt.show()
