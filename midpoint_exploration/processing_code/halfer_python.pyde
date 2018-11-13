#import processing.pdf.*

arrayy=[]
addd=[]
varrayy=[]
c=["#A7226E","#EC2049","#F26B38","#2F9599"]#,"#F7DB4F"]
x1=int(random(0,len(c)-1))
#x2=int(random(0,len(c)-1))
#global wait
#wait=1000
#global c
#c=0
global d
d=0



def setup():
    bord=15
    background("#F7DB4F")
    #global t
    #t= millis()
    colorMode(HSB, 100)
    #noLoop()
    loadPixels()
    size(500, 500)
    '''
    dd=3
    cc=[ [random(width),random(height)]]
    for i in range(0,dd):
        q=random(width)
        q2=random(height)
        if abs(q-cc[-1][-2])>10 and abs(q2-cc[-1][-1])>10:
            cc.append([q,q2])
    '''
    n=4
    #print(midpoint([[bord,height/2],[width-bord,height/2],[width/2,bord],[width/2,height-bord],[width/2,height/2]]) )
    arrayy.append(midpoint([[bord,height/2],[width-bord,height/2],[width/2,bord],[width/2,height-bord],[width/2,height/2]],n)) #,[random(0,width),random(0,height)] ],n ))

def draw():
    #global t
    #print t
  #  global t
   # t=millis()
    #background(50)
    #println(arrayy)
    #println(arrayy)
    #
   # x2=int(random(0,len(c)-1))
    strokeWeight(random(1,2))
    
    noFill()
    #addd=[]
    #rect(50,50,50,50)
    #println(c)
    #println(d)
    global d
   # global c
    
   #arrayy=varrayy
    #println(d)
   # println("yes")
    #println(arrayy[0])
    #println(len(arrayy[c]))
    while d<(len(arrayy[0])-1):
        #println("a")
        #println(d)
        #println("no")
        #addd=[]
        e=d+1
        while e<len(arrayy[0]):
            x1=arrayy[0][d][0]
            y1=arrayy[0][d][1]
            x2=arrayy[0][e][0]
            y2=arrayy[0][e][1]
            #stroke(random(100),random(75,100),random(60,100))
            stroke(c[int(random(0,len(c)))])
            #while (millis() - t < 100):
                #print "a"
            line(x1,y1,x2,y2)
               # t=millis()
            #x2=int(random(0,len(c)-1))
            #fill(x2)
            #ellipse(x1,y1,10,10)
                #print addd
            #stroke(0)
            #point(arrayy[c][d][0],arrayy[c][d][1])
            #point(arrayy[c][e][0],arrayy[c][e][1])
            #ellipse()
            e+=1
        d+=1
    #println(addd)

def midpoint(entry,n):
    a=0
    new=entry
    totals=[]
    while a<n:
        d=0
        while d<(len(new)-1):
            e=d+1
            while e<len(new):
                x1=new[d][0]
                y1=new[d][1]
                x2=new[e][0]
                y2=new[e][1]
                midpoints=[]
                midpoints.append( (x1+ x2 )/2)
                midpoints.append( (y1+ y2 )/2 )
                if (midpoints not in totals): #and (midpoint not in arrayy[-1]:
                    totals.append(midpoints)
                e+=1
            d+=1
        new=totals
       # print (new)
        totals=[]
        #print (totals)
        a+=1
    #println( totals)
    return new
    

def mousePressed():
    #println(addd)
    #global arrayy
    #arrayy=[addd]
    #println(addd)
    global x2
    x2=int(random(0,len(c)-1))
    fill(c[x2])
    #println(type(arrayy))
    ##global c
    #global d
    #d=0
    #arrayy=[]
#println (c)
        
     #   addd=[]
     #   addd
     #   arrayy.append 