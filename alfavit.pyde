#leters - список всех букв алфавита
#x_letters - список иксовых компонент координат, где будем размещать буквы
#y_letters - список игриковых компонент координат, где будем размещать буквы
#x - иксовая компонента координаты центра эллипса
#y - игриковая компонента координаты центра

letters=[u"а",u"б",u"в",u"г",u"д",u"е",u"ё",u"ж",u"з",u"и",u"й",u"к",u"л",u"м",u"н",u"о",u"п",u"р",u"с",u"т",u"у",u"ф",u"х",u"ц",u"ч",u"ш",u"щ",u"ъ",u"ь",u"ы",u"э",u"ю",u"я"]
x_letters=[] #400,60 - первая координата; 180,50 - вторая координата; ... ; 100,360 - последняя координата
y_letters=[] #то есть,пока всего будет первые 6 букв алфавита, расположенных в вышеперечисленных координатах (так как всего завели 6 координт)
x=5
y=5
mode=[]
x_finish=180
def setup():
    size(600,600)
    textSize(20)
def draw():
    global letters,x_letters,y_letters,x,y,mode,x_finish
    background(25,1,7)
    for q in range(33):
        x_letters.append(floor(random(0,580)))
        y_letters.append(floor(random(0,580)))
        mode.append("n")
    ellipse(x,y,10,10)
    if keyPressed==True:
        if key=='w':
            y-=1
        if key=='s':
            y+=1
        if key=='a':
            x-=1
        if key=='d':
            x+=1
            
    #отображаем len(x_letters) рандомных букв из алфавита (то есть из нашего списка letters)
    for i in range(len(letters)):#можно было и y_letters, длины всегда одинаковы у них будут
        #проверяем равенство координаты центра эллипса с координатой буквы. 
        if abs(x-x_letters[i])<10 and abs(y-y_letters[i])<10:
            mode[i]='c'
            x_letters[i]=x_finish
            y_letters[i]=420
            x_finish+=35
        if mode[i]=='c':
            fill(0,255,0)
        else:
            fill(255)
        text(letters[i], x_letters[i],y_letters[i])
    # терперь буквы перерисовываются в координатах x_lett перерисовывается в том же месте. Ведь списки с координатами не меняются
    # то есть i-тая буква рисуется в координате x_letters[i],y_letters[i]. И так для каждого i равного от 0 до 5.
    # нулевая буква рисуется в координате x_letters[0],y_letters[0]
    # первая буква рисуется в координате x_letters[1],y_letters[1] и так далее до пяти. Итого 6 букв
