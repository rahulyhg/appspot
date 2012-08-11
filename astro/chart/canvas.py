# -*- coding:utf-8 -*-
from struct import *
import math
import sys

def readBits(bmp,x1,y1,x2,y2):
    x1,y1,x2,y2=map(int,[x1,y1,x2,y2])
    w,h,p,bc=unpack("<llhh", bmp[18:30])
    line=4*int(math.ceil(w*bc/32.0))
    d={}
    for y in range(y1,y2):
        ln=x2/2-x1/2
        bits=unpack("<"+"B"*ln, bmp[118+y*line+x1/2:118+y*line+x1/2+ln])
        for i,b in enumerate(bits):
            if b!=0xff:
                for j,bx in enumerate([(b>>4) & 0xf,b & 0xf]):
                    if bx!=0xf:
                        d[i*2+j+1j*y]=bx
    p=sum(d.keys())/len(d) if d else 0
    r={}
    for v in d:
        r[v-p]=d[v]
    return r
    
class Canvas():
    def __init__(self,response):
        self.response=response
        self.rot=1
        self.trns=0
        self.points={}
        self.colors=[(i+1,0,0,0) for i in range(15)]+[(0xff,0xff,0xff,0)]
        self.color_cnt=3
        self.pens={1:[0],1.5:[0.25,-0.25,0.25j,-0.25j],2:[0.5,-0.5,0.5j,-0.5j],3:[-1.0,0j,1.0,1j,-1j]}
        self.pen=self.pens[1]

    def addPoints(self,ps):
        for p in ps:
            p=p*self.rot+self.trns
            self.points[(int(p.real),int(p.imag))]=self.color
#            self.points[int(p.real)+1j*int(p.imag)]=self.color
            
    def addPoint(self,pnt):
        for pd in self.pen:
            p=(pnt+pd)*self.rot+self.trns
            self.points[(int(p.real),int(p.imag))]=self.color
#            self.points[int(p.real)+1j*int(p.imag)]=self.color

    def circle(self,x,y,r):
        dth=5.0/r
        th=0
        lst=[]
        while th<=2*math.pi:
            th+=dth
            p=x+int(r*math.cos(th))+1j*int(y+r*math.sin(th))
            lst.append(p)
        self.polygon(lst)
            
    def save(self):
        bmp=open('astro/chart/bmp.bmp','rb').read()
        w,h,p,bc=unpack("<llhh", bmp[18:30])
        line=4*int(math.ceil(w*bc/32.0))
        self.response.write(bmp[:54])#118
        bits=""
        for c in self.colors:
            bits+=pack("<BBBB",*c)
        bs=[0xff for y in range(h) for i in range(line)]
        for p in self.points:
            x,i,y=p[0],p[0]/2,p[1]
            v=self.points[p]
            if x%2:
                v=0xf0+v
            else:
                v=(v<<4)+0xf
            bs[i+y*line]&=v
        bits+=pack("<"+"B"*line*h,*bs)
        self.response.write(bits)
                
    def line(self,x1,y1,x2,y2):
        p1,p2=map(lambda x,y:x+1j*y,[x1,x2],[y1,y2])
        self.lineI(p1,p2)
    
    def lineI(self,p1,p2):
        d=p2-p1
        d=max(abs(d.imag),abs(d.real))
        for i in range(int(d)+1):
            p=(p1*i+p2*(d-i))/d if d else p1          
            self.addPoint(p)  
    
    def polygon(self,lst):
        for p1,p2 in zip(lst,lst[1:]+lst[:1]):
            self.lineI(p1,p2)
            
    def setStrokeColorRGB(self,*args):
        args=list(args)
        args.reverse()
        args=tuple(map(lambda x:int(255*x),args)+[0])
        if not args in self.colors:
            self.colors[self.color_cnt]=args
            self.color_cnt+=1
        self.color=self.colors.index(args)
        
    def translate(self,x,y):
        self.trns+=self.rot*(x+1j*y)
    
    def rotate(self,d):
        a=math.radians(d)
        self.rot*=math.cos(a)+1j*math.sin(a)
    