import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp

row = []
col = []
with open('/Users/zx/Desktop/roc_data.txt', 'r') as file:
    
    for y in file.readlines():
        y = y.replace('\n','')
        y = y.split()
        if float(y[0]) == 2:
            row.append(1)
            col.append(float(y[1]))
        elif float(y[0]) == 1:
            row.append(0)
            prob = 10 - float(y[1])
            #print (prob)
            col.append(prob)
        elif float(y[0]) == 0:
            row.append(0)
            prob = 10 - float(y[1])
            #print (prob)
            col.append(prob)
            
    row = np.array(row)
    col = np.array(col)
    
    print(row)
    print(col)
    
fpr, tpr, thresholds = metrics.roc_curve(row, col)

print(fpr)
print(tpr)
print(auc(fpr, tpr))

roc_auc = auc(fpr,tpr)

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()  
