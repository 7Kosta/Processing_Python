w=275
a=275
xc=a+25
yc=w+25
p=255
def setup():
    size(600,600)
def draw():
    global w,a,xc,yc, rasst,p
    if mouseX>0 and mouseX<40 and mouseY>0 and mouseY<40 and mousePressed == True:
        a=300
        w=300
        background(200)
    fill(255)
    if keyPressed== True:
        if key=='w':
            w-=1
        if key=='s':
            w+=1
        if key=='a':
            a-=1
        if key=='d':
            a+=1
    fill(255,0,0)
    fill(p)
    ellipse(70,70,25,25)
    fill(255)
    rect(a,w,50,50)
    xc=a+25
    yc=w+25
    rasst=sqrt((xc-70)*2 + (yc-70)*2)
    if rasst <5:
        p=0
    rect(0,0,40,40)
    
