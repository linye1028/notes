import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time, threading
import serial
def serialRec():
	global t
	global x
	global y,y2
	global recRD

	if ser.inWaiting()>0:
		recRD+=ser.read().decode()
		if(recRD[-1]=='\n'):
			t=t+1
			x=np.append(x,t)
			y=np.append(y,float(recRD.split('m')[0]))
			y2=np.append(y2,float(recRD.split('m')[1]))
			recRD=""
			if len(x)>50 :
				x=x[-50:]
				y=y[-50:]
				y2=y2[-50:]
			drawPic()
			drawPic2()
	time.sleep(0.01)
	t1 = threading.Thread(target=serialRec)
	t1.start()	
def drawPic():
	global x
	global y
       
    #清空图像，以使得前后两次绘制的图像不会重叠
	drawPic.f.clf()
	drawPic.a=drawPic.f.add_subplot(111)
      
    #在[0,100]范围内随机生成sampleCount个数据点
    #x=np.random.randint(0,100,size=sampleCount)
    #y=np.random.randint(0,100,size=sampleCount)
	#color=['b','r','y','g']

    #绘制这些随机点的散点图，颜色随机选取
	drawPic.a.plot(x,y,color='b')
	drawPic.a.set_title('Demo: Draw sin')
	drawPic.canvas.show()
 
 
def drawPic2():
	global x
	global y2
       
    #清空图像，以使得前后两次绘制的图像不会重叠
	drawPic2.f.clf()
	drawPic2.a=drawPic2.f.add_subplot(111)
      
    #在[0,100]范围内随机生成sampleCount个数据点
    #x=np.random.randint(0,100,size=sampleCount)
    #y=np.random.randint(0,100,size=sampleCount)
	#color=['b','r','y','g']

    #绘制这些随机点的散点图，颜色随机选取
	drawPic2.a.plot(x,y2,color='b')
	drawPic2.a.set_title('Demo: Draw cos')
	drawPic2.canvas.show() 
 
if __name__ == '__main__':   
	ser=serial.Serial("COM2",9600)
	
	t=0
	recRD=""
	x=np.array([0])
	y=np.array([0])
	y2=np.array([0])
	
	matplotlib.use('TkAgg')
	root = Tk()  
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
	drawPic.f = Figure(figsize=(5,4), dpi=100)
	drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root) 
	drawPic.canvas.show() 
	drawPic.canvas.get_tk_widget().grid(row=0, column=0)    

	drawPic2.f = Figure(figsize=(5,4), dpi=100)
	drawPic2.canvas = FigureCanvasTkAgg(drawPic2.f, master=root) 
	drawPic2.canvas.show() 
	drawPic2.canvas.get_tk_widget().grid(row=0, column=1)    
    
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
	t_serialRec = threading.Thread(target=serialRec)
	t_serialRec.start()    	
    #启动事件循环
	root.mainloop()