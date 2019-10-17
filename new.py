import numpy as np
import cv2
#find median number
def findmedian(begin,median,end):
	if begin<end:
		if median<begin:
			median=begin
		elif median>=end:
			median=end
	else:
		temp=begin
		begin=end
		end=temp
		if median<begin:
			median=begin
		elif median>=end:
			median=end
	return median 


def findMatrixMedian(a):
	m=len(a)#rows
	n=len(a[0])#columns
	if m%2==0 or n%2==0:
		return Exception('kernel size is odd!')
	#initial the median
	M=a[(m-1)//2][(n-1)//2]

	#initial the first and last
	i=[0,0]
	j=[m-1,n-1]

	#use enmerate number tell when to stop
	enume=0
	#O(n)
	while enume<(m*n)//2:
		M=findmedian(a[i[0]][i[1]],M,a[j[0]][j[1]])
		# print(a[i[0]][i[1]],M,a[j[0]][j[1]])
		enume+=1
		# print([i[0],i[1]],[j[0],j[1]])
		i[1]+=1
		j[1]-=1
		if i[1]>n-1 and j[1]<0:
			i[1]=0
			i[0]+=1
			j[0]-=1
			j[1]=n-1
	return M
print(findMatrixMedian([[1,2,3],[4,9,6],[8,6,7]]))

def BlurTunel(T,ksize):#ksize is heigh x width int or tuple or list are supported
	#keep the original bound
	if isinstance(ksize,int):#judge the type of ksize 
		paddingh=(ksize-1)//2
		paddingw=paddingh
	elif isinstance(ksize,tuple) or isinstance(ksize,list):
		paddingw=(ksize[1]-1)//2
		paddingh=(ksize[0]-1)//2
	
	height=len(T)
	width=len(T[0])
	for i in range(paddingh,height-paddingh):
		for j in range(paddingw,width-paddingw):
			T[i][j]=findMatrixMedian(T[i-paddingh:i+paddingh+1,j-paddingw:j+paddingw+1])
	return T
			
	#to do (maybe black bound,or no bound optional)

	
def MedianBlur(img,ksize):
	if len(img.shape)<3:
		img=BlurTunel(img,ksize)
	else:
		R,G,B=cv2.split(img)
		R=BlurTunel(R,ksize)
		G=BlurTunel(G,ksize)
		B=BlurTunel(B,ksize)
		img=cv2.merge([R,G,B])
	return img

img=cv2.imread('lenna.jpg',1)
m_img=MedianBlur(img,(3,5))
cv2.imshow('medin_img',m_img)
cv2.imshow('original_img',img)
key=cv2.waitKey()
if key==27:
	cv2.destroyAllWindows()

