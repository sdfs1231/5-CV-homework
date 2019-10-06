import cv2
from matplotlib import pyplot as plt
import numpy as np
import random
# print(cv2.__version__)
#
# # cv2.imshow('kobe',img)
# # key=cv2.waitKey(0)
# # if key==27:
# #     cv2.destroyAllWindows()
# # elif key==ord('s'):
# #     a=input('what filename you want to save?')
# #     cv2.imwrite(a+'.jpg',img)
# #     cv2.destroyAllWindows()

class creat_img():
    def __init__(self,img,name):
        self.img=img
        self.name=name
        b,g,r=cv2.split(self.img)
        self.img=cv2.merge((r,g,b))


    def crop(self):
        height,width=self.img.shape[:2]
        w1=random.randint(100,width+1-100)
        w2=random.randint(w1+100,width+1)
        h1=random.randint(100,height+1-100)
        h2=random.randint(h1+100,height+1)
        self.img = self.img[w1:w2, h1:h2]

    def color_shift(self):
        r,g,b=cv2.split(self.img)
        changeR=random.randint(0,256)
        changeG=random.randint(0,256)
        changeB=random.randint(0,256)
        def f(org,change):
            org[org>255-change]=255
            org[org<=255-change]=org[org<=255-change]+change
            return org

        r=f(r,changeR)
        g=f(g,changeG)
        b=f(b,changeB)
        self.img=cv2.merge((r,g,b))

    def rotation(self):
        angle=random.randint(0,360)
        M=cv2.getRotationMatrix2D((self.img.shape[1]/2,self.img.shape[0]/2),angle,1)
        self.img=cv2.warpAffine(self.img,M,(self.img.shape[1],self.img.shape[0]))

    def perspective_transform(self):
        height, width = self.img.shape[:2]
        print(height, width)
        pst1 = []
        pst2 = []
        for i in range(4):
            x = random.randint(0, width + 1)
            y = random.randint(0, height + 1)
            pst1.append([x, y])
        for i in range(4):
            x = random.randint(0, width + 1)
            y = random.randint(0, height + 1)
            pst2.append([x, y])
        pst1 = np.float32(pst1)
        pst2 = np.float32(pst2)
        M = cv2.getPerspectiveTransform(pst1, pst2)
        self.img = cv2.warpPerspective(img, M, (self.img.shape[1], self.img.shape[0]))


    def gamma_trans(self, gamma=1):
        gamma_tabe = [np.power(x / 255, gamma) * 255.0 for x in range(256)]
        gamma_tabe = np.round(np.array(gamma_tabe)).astype(np.uint8)
        self.img=cv2.LUT(self.img, gamma_tabe)

    def write_img(self):
        cv2.imwrite(self.name,self.img)
img=cv2.imread('kobe.jpg',1)
j=random.randint(1,100)
print(j)
for i in range(100):
    name='kobe'+str(i)+'.jpg'
    a=random.choice([0,1])
    b=random.choice([0,1])
    c=random.choice([0,1])
    d=random.choice([0,1])
    work=creat_img(img=img,name=name)
    if a:
        work.crop()
    if b:
        work.color_shift()
    if c:
        work.rotation()
    if d:
        work.perspective_transform()
    work.write_img()




