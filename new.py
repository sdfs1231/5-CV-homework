import numpy as np
import random
import matplotlib.pyplot as plt
import time
import math

def generate_sampple():
    x_list=[]
    y_list=[]
    generate_time=100
    for i in range(generate_time):
        if i < 50:
            x_list.append(random.randint(0,50)+random.randint(-5,5))
            y_list.append(random.uniform(0,0.5))
        else:
            x_list.append(random.randint(50,100)+random.randint(-5,5))
            y_list.append(random.uniform(0.5,1))
    return x_list,y_list


def sigmoid(x):
    y=1/(1+math.exp(-x))
    return y

def predict_pro(w,x,b):
    temp=w*x+b
    prob=sigmoid(temp)
    return prob

def zero_or_one(pro):
    if pro>0.5:
        return 1
    else:
        return 0



def cal_loss(data_list,label_list,w,b):
    size=len(label_list)
    aver_loss=0
    for i in range(size):
        aver_loss+=-(label_list[i]*math.log(predict_pro(w,data_list[i],b))+(1-label_list[i])*math.log(predict_pro(w,data_list[i],b)))
    return aver_loss

def update_parameters(data_list,label_list,w,b,lr):
    dw=0
    db=0
    size=len(data_list)
    for i in range(size):
        dw+=-(label_list[i]-predict_pro(w,data_list[i],b))*data_list[i]
        db+=-label_list[i]-predict_pro(w,data_list[i],b)
    w=w-lr*dw
    b=b-lr*db
    return w,b

def train(data_list,label_list,maxiter,lr):
    w=0
    b=0
    for i in range(maxiter):
        w,b=update_parameters(data_list,label_list,w,b,lr)
        
        print('w:{},b:{}'.format(w,b))
        print('loss is :{}'.format(cal_loss(data_list,label_list,w,b)))
        time.sleep(1)
    return w,b
label_list=[]
x,y=generate_sampple()
plt.scatter(x,y)
plt.show()
for label in y:
    if label>0.5:
        label_list.append(1)
    else:
        label_list.append(0)
train(x,label_list,500,0.00001)

# def cal_loss(x_list,y_list,w,b,):
#     average_loss=0
#     batch_size=len(x_list)
#     for i in range(batch_size):
#         average_loss+=0.5*(prec_y(w,x_list[i],b)-y_list[i])**2
#     average_loss/=len(y_list)
#     return average_loss
#
# def update_parameters(x_list,gt_y_list,w,b,lr):
#     dw=0
#     db=0
#     batch_size=len(x_list)
#     for i in range(batch_size):
#         dw+=(prec_y(w,x_list[i],b)-gt_y_list[i])*x_list[i]
#         db+=prec_y(w,x_list[i],b)-gt_y_list[i]
#     dw/=len(x_list)
#     db/=len(gt_y_list)
#     w=w-lr*dw
#     b=b-lr*db
#     return w,b
#
# def train(x_list,gt_y_list,batchsize,lr,maxiter):
#     w=0
#     b=0
#     for i in range(maxiter):
#         batch_idx=np.random.choice(len(x_list),batchsize)
#         batch_x=[x_list[j] for j in batch_idx]
#         batch_y=[gt_y_list[j] for j in batch_idx]
#         w,b=update_parameters(batch_x,batch_y,w,b,lr)
#         print('w:{},b:{}'.format(w,b))
#         print('loss is :{}'.format(cal_loss(batch_x,batch_y,w,b)))
#         time.sleep(1)
#     return w,b
