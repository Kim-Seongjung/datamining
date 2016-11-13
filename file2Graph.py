
# coding: utf-8

# In[59]:

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


        
def showLines(path , limit ):
    fo = open(path)
    lines=fo.readlines()
    for i in range(limit):
        print lines[i]
    
        
def stringInWords(str_): #
    words_list=str_.split()
    for i , ele in enumerate(words_list):
        print i , ele 

def file2Graph(x_list , y_list , graph_size , save_path ,x_label , y_label):    
    assert len(x_list)==len(y_list)
    
    fig1 = plt.figure(figsize =graph_size)
    save_name='x: step , y : loss'
    ax=fig1.add_subplot(1,1,1)
    
    plt.scatter(x_list , y_list )
    plt.savefig(save_path+save_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
"""
    step 223600 , training  accuracy 0.851508
step 223600 , loss : 2.30553
step 223700 , training  accuracy 0.851508
step 223700 , loss : 2.26034
step 223800 , training  accuracy 0.849188
step 223800 , loss : 2.29881
step 223900 , training  accuracy 0.846868
step 223900 , loss : 2.31931
step 224000 , training  accuracy 0.846868
step 224000 , loss : 2.27104
step 224100 , training  accuracy 0.846868
step 224100 , loss : 2.29065
step 224200 , training  accuracy 0.846868
step 224200 , loss : 2.31258
step 224300 , training  accuracy 0.846868
"""
    


# In[60]:

def showLines(source_path , limit ):
    fo = open(path)
    lines=fo.readlines()
    for i in range(limit):
        print i, lines[i]
source_path= '/media/ncc/새 볼륨/mammo_acuuracy_91/log.txt'
limit=6
showLines(source_path , limit)


# In[62]:

def extractStr(source_path , pattern1 , pattern2=None): # \n을 무시하고 모든 라인을 읽는다
    fo=open(path)
    lines=fo.readlines()
    lines_=[]
    if pattern2 is not None:
        for line in lines:
            if line !='\n' and pattern1 in line and pattern2 in line:
                lines_.append(line)
    else:
        for line in lines:
            if line !='\n' and pattern1 in line:
                lines_.append(line)
    return lines_
source_path= '/media/ncc/새 볼륨/mammo_acuuracy_91/log.txt/'

pattern1='training'

list_1 = list_str=extractStr(source_path , pattern1)

pattern1='step'
pattern2='loss'
list_2 = extractStr(source_path , pattern1 , pattern2)


def extractValue(list_str):
    x=[]
    y=[]
    sample_str=list_str[0].split()
    for i, ele in enumerate(sample_str):
            print i , ele , 
    print "x축으로 선택할 추출하고 싶은 번호를 입력하세요" 
    pattern1 = raw_input()
    print "y축으로 선택할 추출하고 싶은 번호를 입력하세요" 
    pattern2 = raw_input()
    
    for i , ele in enumerate(list_str):
        ele=ele.split()
        x.append(float(ele[int(pattern1)]))
        y.append(float(ele[int(pattern2)]))
    return x , y 

    


x,y=extractValue(list_1)
graph_size=(10,8)
save_path='/home/ncc/Desktop/delete_result'
file2Graph(x , y , graph_size , save_path ,'step' , 'accuracy')



# In[14]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
step=[0,4,2,3,4]
loss=[0,1,2,3,4]

fig1 = plt.figure(figsize =graph_size)
save_name='x: step , y : loss'
ax=fig1.add_subplot(1,1,1)
plt.scatter(step[0:5] , loss[0:5])
plt.savefig(save_path+save_name)


# In[12]:

file_path='/media/ncc/새 볼륨/mammo_acuuracy_91/log.txt'
save_path='/home/ncc/Desktop/delete_result'
graph_size=(20,8)
file2Graph(file_path , save_path , graph_size)


# In[63]:

import site; 
print site.getsitepackages()


# In[ ]:



