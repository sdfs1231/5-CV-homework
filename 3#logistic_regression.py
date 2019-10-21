import numpy as np
import random
import matplotlib.pyplot as plt
import time
import math

def generate_sampple():
    w=random.randint(0,10)+random.random()
    b=random.randint(0,5)+random.random()
    generate_time=100
    i=0
    j=0
    generate_time=100
    for i in range(generate_time):
        x1_list=[random.randint(0,50) for i in range(generate_time)]
        x2_list=[random.randint(50,100)+random.randrange(-10,10) for i in range(generate_time)]
        label_list=[random.ra]
    return x_list,y_list
# x,y=generate_sampple()
# plt.scatter(x,y)
# plt.show()

def sigmoid(x):
    return 1/(math.exp(-x))

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
        aver_loss+=-label_list[i]*math.log(predict_pro(w,data_list[i],b))+(1-label_list[i])*math.log(predict_pro(w,data_list[i],b))
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
    return w,b


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
x_list,y_list=generate_sampple()
train(x_list,y_list,100,0.0001)



