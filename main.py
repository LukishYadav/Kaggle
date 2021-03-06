import pandas as pd
import numpy as np

data=pd.read_csv('train.csv')


x=['Age','Pclass','Sex','Fare']
y=['Survived']

X=data[x]
Y=data[y]


X['Age'].isnull().sum()
X['Sex'].isnull().sum()
X['Fare'].isnull().sum()
X['Pclass'].isnull().sum()




#Replacing nulls with medians


X['Age']=X['Age'].fillna(X['Age'].median())
d={'male':0,'female':1}
X['Sex']=X['Sex'].apply(lambda x:d[x])
X['Sex'].head()


from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42)


from sklearn import svm
clf=svm.LinearSVC()

clf.fit(X_train,Y_train)


print clf.predict(X_test[0:10])

y_pred=clf.predict(X_test)
Y_pred=pd.DataFrame(y_pred,columns=['Survived2'])

#Just to get a replica of y_pred
Y_test1=pd.DataFrame(y_pred,columns=['Survived'])


    

print clf.score(X_test,Y_test)

"""
Ar=Y_test.index.get_values()
length=len(Ar)
list=[]
for i in range(0,length):
    list.append(Ar[i])
x=0    
for i in list:
    if x!=len(Y_test):
     Y_test1['Survived'][x]=Y_test['Survived'][i]
     x=x+1

d2=range(0,len(Y_test))

from prettytable import PrettyTable
t = PrettyTable(['Actual','Prediction'])
for x in d2:
 t.add_row([Y_test1['Survived'][x],Y_pred['Survived2'][x]])
 
 

#Main=pd.concat([X_test,Y_test.reset_index(drop=True),Y_pred.reset_index(drop=True)],axis=1)
print t

"""
#Main=pd.concat([X_test,Y_test.reset_index(drop=True),Y_pred.reset_index(drop=True)])

#******VIMP***********
# Arrangement for concating three dataframes columnwise


X_test2=X_test.reset_index(drop=True)
Y_test2=Y_test.reset_index(drop=True)
Y_pred2=Y_pred.reset_index(drop=True)
Main=pd.concat([X_test2,Y_test2,Y_pred2],axis=1)


#Condition based indexing
#print Main[(Main['Survived']==Main['Survived2'])] #Correct Prediction
#print Main[(Main['Survived']!=Main['Survived2'])] #Wrong Prediction
#print((X_test[(Y_test.reset_index(drop=True) != Y_pred.reset_index(drop=True))]).reset_index(drop=True)).sum()


print (Main['Survived']==Main['Survived2']).sum()
print (Main['Survived']!=Main['Survived2']).sum()

     

