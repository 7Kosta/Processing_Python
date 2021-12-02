x=1
siz=1
fil=0
filll=0
mode="RGB"
def setup():
    size(600,600)
    frameRate(5)
def draw():
    global x,siz,mode,fil,filll
    fill(245,0,0)
    if mouseX>0 and mouseX<40 and mouseY>0 and mouseY<40 and mousePressed==True:
        stroke(255,0,0)
    if mouseX>60 and mouseX<80 and mouseY>0 and mouseY<40 and mousePressed == True:
        stroke(0,255,0)
    if mouseX>80 and mouseX<120 and mouseY>0 and mouseY<40 and mousePressed == True:
        if mouseButton == RIGHT:
            siz-=1
        if mouseButton == LEFT:
            siz+=1
    if mouseX>560 and mouseX<600 and mouseY>560 and mouseY<600 and mousePressed == True:
        background(200)
    if siz == 0:
        siz=1
    if mouseX>120 and mouseX<160 and mouseY>0 and mouseY<40 and mousePressed==True and mouseButton == LEFT:
        mode="HSB"
        colorMode(HSB,255)
    if mouseX>120 and mouseX<160 and mouseY>0 and mouseY<40 and mousePressed==True and mouseButton == RIGHT:
        mode="RGB"
        colorMode(RGB,255)
    if mouseX>160 and mouseX<200 and mouseY>0 and mouseY<40 and mousePressed==True and mouseButton == LEFT:
        background(random(0,255),random(0,255),random(0,255))
    if mouseX>160 and mouseX<200 and mouseY>0 and mouseY<40 and mousePressed==True and mouseButton == RIGHT:
        background(200)
    if mode=="RGB":
        strokeWeight(1)
        rect(0,0,40,40)#красная кнопка
        fill(0,255,0)
        rect(40,0,40,40)#зелёная кнопка
        fill(0)
        rect(560,580,40,20)#кнопка стереть
        fill(random(0,255),random(0,255),random(0,255))
        rect(160,0,40,40)#кнопка разноцветного фона
        textSize(10)
        fill(random(0,255),random(0,255),random(0,255))
        rect(120,0,40,40)#кнопка радуги
        fill(255)
        text("RED",5,20)
        text("GREEN",40,20)
        textSize(15)
        text(siz,100,20)
        textSize(10)
        text(u"СТЕРЕТЬ",560,600)
        text("RAINBOW",120,20)
        textSize(5)
        text("BACKGROUND",160,20)
    if mode=="HSB":
        fil+=1
        strokeWeight(1)
        fill(fil,255,255)
        stroke(fil,255,255)
        rect(120,0,40,40)
        fill(255)
        textSize(10)
        text("RAINBOW",120,20)
        if fil==255:
            fil=0
        fill(0)
        rect(560,580,40,20)#кнопка стереть
        fill(255)
        text(u"СТЕРЕТЬ",560,600)
        textSize(15)
        text(siz,100,20)
    if mousePressed == True and mouseButton == RIGHT:
        filll=200
        stroke(filll)
        strokeWeight(siz)
        line(mouseX,mouseY,pmouseX,pmouseY)
    if mousePressed == True and mouseButton == LEFT:
        strokeWeight(siz)
        line(mouseX,mouseY,pmouseX,pmouseY)
def mouseClicked():
    saveFrame('risunok.jpg')
