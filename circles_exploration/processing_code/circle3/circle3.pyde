#circle3

#quars=[]
from math import *

#c=[ [96.972,98.9,62.9],[.5,94.2,79.6],[7.027,86.4,82.7],[.17,22,77.4],[42.417,21.6,60] ]
'''
c=[]
e=2
for i in range(0,e):
    c.append([random(100)])
'''
c=[[46],[2]]

def setup():
    size(3000, 3000)
    colorMode(HSB, 100)
    cc=int(random(0,len(c)))
    background(c[cc][0],random(0,100),random(0,100),random(50,75))
    loadPixels()
    noLoop()
    noStroke()
    #bord=15
    global radius
    radius=0.9*width/2
    rectMode(CENTER);
    #print quars

def draw():
    quars=[ [width/2,height/2,radius] ]
    n=6
    d=80
    f=1
    #ellipse(quars[0][0],quars[0][1],2*quars[0][2],2*quars[0][2])
    print quars
    for i in quars:
        f=int(random(1,3))
        cc=int(random(0,len(c)))
        #fill(c[cc][0],c[cc][1],c[cc][2],random(20,50))
        #stroke( c[cc][0],c[cc][1],c[cc][2],random(50,100) )
        #noStroke()
        fill(c[cc][0],random(0,100),random(0,100),d)#random(25,75))
        #if f==1:
        ellipse(i[0],i[1],2*i[2],2*i[2])
       # else:
        #    rect(i[0],i[1],2*i[2],2*i[2])
       # print "a"
        
    while n>=1:
        quars2=[]
        a=0
        for a in quars:
            for b in isec(a):
                quars2.append(b)
        quars=quars2
        for i in quars:
            f=int(random(1,3))
            strokeWeight(1)#random(1,3))
            cc=int(random(0,len(c)))
            #stroke( c[cc][0],c[cc][1],c[cc][2],random(50,100) )
            #cc=int(random(0,len(c)))
            #fill(c[cc][0],c[cc][1],c[cc][2],random(20,50))
            fill(c[cc][0],random(0,100),random(0,100),d)#random(25,75))
            #if f==1:
            ellipse(i[0],i[1],2*i[2],2*i[2])#2*random(i[2],i[2]*1.5),2*random(i[2],i[2]*1.5))
            #else:
              #  rect(i[0],i[1],2*random(i[2],i[2]*1.2),2*random(i[2],i[2]*1.2))
        d=d*.8#random(.5,1.23)
        n-=1


def isec(array):
    r=array[2]
    xx=array[0]
    yy=array[1]
    d=r/float(2*sqrt(2))
    #print d
    return [[xx+d,yy+d,r/2],[xx-d,yy+d,r/2],[xx-d,yy-d,r/2],[xx+d,yy-d,r/2]]