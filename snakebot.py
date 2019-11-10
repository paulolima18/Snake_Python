'Game1'
'''
x.type são os seguintes
(Tudo em Capslock)
quit
atctiveevent
keydown
keyup
mousemotion
mousebuttonup
mousebuttondown
videioresize
'''
#40pygame
import pygame_textinput
import pygame
import random

width=800
height=600
bsize=20
thick=20
fps=60
direction = 270
wall = 10

pygame.init()
gdisplay=pygame.display.set_mode((width,height))
pygame.display.update()

pygame.display.set_caption('SNAKE PL')
colors={'red':(128,0,0),'black':(0,0,0),'white':(255,255,255),'green':(0,155,0),'blue':(0,0,155),'yellow':(255,170,0),'darkblue':(51,102,204),'darkgreen':(51,102,0),
'violet':(102,0,102),'brown':(77,38,0),'pink':(255,204,255)}

'music = pygame.mixer.Sound('')'
def music1():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Reloaded Installer 9.mp3')
    pygame.mixer.music.play(-1)

def music2():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Lionel Richie - Hello.mp3')
    pygame.mixer.music.play(-1)

def music3():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Lana Del Rey - Video Games.mp3')
    pygame.mixer.music.play()

def music4():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('George Michael - Careless Whisper.mp3')
    pygame.mixer.music.play()

icon = pygame.image.load('s32.png')
snakepng = pygame.image.load('snakehead20.png')
applepng = pygame.image.load('apple20.png')
pygame.display.set_icon(icon)

textinput = pygame_textinput.TextInput()

clock=pygame.time.Clock()

smallfont = pygame.font.SysFont('impact', 30)
medfont = pygame.font.SysFont('impact', 60)
largefont = pygame.font.SysFont('impact', 90)
introfont = pygame.font.SysFont('Impact', 150)
def snake(bsize,snakelist,x):

    head = pygame.transform.rotate(snakepng,direction)
    gdisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for xy in snakelist[:-1]:
        pygame.draw.rect(gdisplay,colors['green'],[xy[0],xy[1],bsize,bsize])

def text_objetcts(text,color,size):
    textsurface = size.render(text, True,color)
    return textsurface, textsurface.get_rect()

def msm(msg,color,change=0,size=medfont):
    text1,text2 = text_objetcts(msg,color,size)
    text2.center = (width/2),((height/2)+change)
    gdisplay.blit(text1,text2)

def score(score):
    text = smallfont.render('Score: ' + str(score), True, colors['black'])
    gdisplay.blit(text,(bsize,bsize))

def pause():

    pause = True
    pygame.mixer.music.pause()
    gdisplay.fill(colors['darkblue'])
    msm('PAUSE',colors['black'],-100,largefont)
    msm('(C) to Continue (Q) to Quit',colors['black'],0,smallfont)
    msm('New music press from (1 to 4)',colors['black'],50,smallfont)


    pygame.display.update()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    pygame.mixer.music.unpause()
                    pause = False
                if event.key == pygame.K_1:
                    music1()
                if event.key == pygame.K_2:
                    music2()
                if event.key == pygame.K_3:
                    music3()
                if event.key == pygame.K_4:
                    music4()
    clock.tick(5)

def introg():
    music1()
    pygame.display.update()
    intro = True
    while intro:
        gdisplay.fill(colors['darkgreen'])
        msm("SNAKE PL",colors['violet'],-100,introfont)
        msm('Simple Snake Game', colors['black'],0,smallfont)
        msm('Press (S) to Start (P) to Pause (Q) to Quit',colors['blue'],height/2-100,smallfont)
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
                    gameloop()
                if event.key == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def inputed():
    inpute = True

    while inpute:
        gdisplay.fill(colors['darkblue'])
        msm('|Place Player Name|',colors['yellow'],0,largefont)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return textinput.get_text()
                    inpute = False
        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        gdisplay.blit(textinput.get_surface(), (10, 10))
        pygame.display.update()
        clock.tick(30)

def topscore(score,name):
    eva = True
    pre = ["?","meh"]
    pos = ["crazy","veryStack"]
    listz = []
    while eva:
        with open('topscore.txt','r') as fd:
            lines = [x.split() for x in fd.readlines()]
            check = False
            for line in lines:
                if (score > int(line[1]) ) and (not check):
                    #Save current value
                    pre[0] = line[0]
                    pre[1] = line[1]
                    #Insert New score
                    line[1] = score
                    line[0] = name
                    listz.append(line)
                    check = True
                elif check:
                    #Position Value
                    pos[0] = line[0]
                    pos[1] = line[1]
                    #Player that got downgraded
                    line[1] = pre[1]
                    line[0] = pre[0]
                    #Player that will get downgraded
                    pre[0] = pos[0]
                    pre[1] = pos[1]
                    listz.append(line)
                else:
                    listz.append(line)
            x = [x for x in listz]

        with open('topscore.txt','w') as fd:
                for i in range(len(x)):
                    if i == 0:
                        fd.write('%s %s\n'%(x[i][0],x[i][1]))
                    elif 0<i<9:
                        fd.write('%s %s\n'%(x[i][0],x[i][1]))
                    elif i == 9:
                        fd.write('%s %s'%(x[i][0],x[i][1]))
                eva = False

        '''fd = open('top10.txt',a)
        'Nome de Jogador | score '
        fd.close()
        '''
def final():
    fin = True
    while fin:
        with open('topscore.txt','r') as fd:
            lines = [line.split() for line in fd.readlines()]
            gdisplay.fill(colors['darkblue'])
            msm('TOP SCORES',colors['yellow'],-250,medfont)
            msm(str('%s:%s'%(lines[0][0],lines[0][1])),colors['black'],-200,smallfont)
            msm(str('%s:%s'%(lines[1][0],lines[1][1])),colors['black'],-150,smallfont)
            msm(str('%s:%s'%(lines[2][0],lines[2][1])),colors['black'],-100,smallfont)
            msm(str('%s:%s'%(lines[3][0],lines[3][1])),colors['black'],-50,smallfont)
            msm(str('%s:%s'%(lines[4][0],lines[4][1])),colors['black'],0,smallfont)
            msm(str('%s:%s'%(lines[5][0],lines[5][1])),colors['black'],50,smallfont)
            msm(str('%s:%s'%(lines[6][0],lines[6][1])),colors['black'],100,smallfont)
            msm(str('%s:%s'%(lines[7][0],lines[7][1])),colors['black'],150,smallfont)
            msm(str('%s:%s'%(lines[8][0],lines[8][1])),colors['black'],200,smallfont)
            msm(str('%s:%s'%(lines[9][0],lines[9][1])),colors['black'],250,smallfont)
            text = smallfont.render('Q (Quit) B (Start Screen)', True, colors['black'])
            gdisplay.blit(text,(width-300,height-50))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                        fin == False
                    if event.key == pygame.K_b:
                        introg()
def walls():
    left = pygame.draw.rect(gdisplay,colors['pink'],[0,0,wall,height])
    right = pygame.draw.rect(gdisplay,colors['pink'],[width-wall,0,wall,height])
    up = pygame.draw.rect(gdisplay,colors['pink'],[0,0,width,wall])
    down = pygame.draw.rect(gdisplay,colors['pink'],[0,height-wall,width,wall])

def butt(snakelist,snakehead,direction):
    for i in snakelist[:-1]:
        if direction == 270:
            if [snakehead[0]+10.0,snakehead[1]] == i:
                return True
        if direction == 90:
            if [snakehead[0]-10.0,snakehead[1]] == i:
                return True
        if direction == 0:
            if [snakehead[0],snakehead[1]-10.0] == i:
                return True
        if direction == 180:
            if [snakehead[0],snakehead[1]+10.0] == i:
                return True
    return False

def gameloop():
    global direction
    exitg = False
    overg = False
    x_lead=width/2 #incio
    y_lead=height/2
    xclead,yclead=bsize,0

    snakehead = []
    snakelist = []
    snakelen = 1
    xapple = int(random.randrange(bsize,width-thick,bsize))
    yapple = int(random.randrange(bsize,height-thick,bsize))

    while not exitg:
        while overg == True:
            gdisplay.fill(colors['darkblue'])
            msm('GAME OVER',colors['red'],-100,largefont)
            msm('Press C (Repeat) Q (Quit) B (Music Selection) T (Scores)',colors['yellow'],height/2-100,smallfont)
            msm('Your score is %d'%(snakelen-1), colors['black'], 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitg = True
                    overg = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    if event.key == pygame.K_q:
                        exitg = True
                        overg = False
                    if event.key == pygame.K_b:
                        introg()
                    if event.key == pygame.K_t:
                        playername = inputed()
                        topscore(snakelen-1,playername)
                        final()
                    '''if event.key == pygame.K_t:
                        topscore(snakelen-1,playername)
                        '''

        if (x_lead > xapple):
            if direction == 270 and (not butt(snakelist,snakehead,270)):#(right)
                if (y_lead < yapple) and (not butt(snakelist,snakehead,180)):
                    direction = 180
                    yclead = bsize
                    xclead = 0
                    #faker
                if (y_lead < yapple) and (not butt(snakelist,snakehead,0)):
                    direction = 0
                    yclead = -bsize
                    xclead = 0
                if (y_lead > yapple) and (not butt(snakelist,snakehead,0)):
                    direction = 0
                    yclead = -bsize
                    xclead = 0
                    #faker
                if (y_lead > yapple)and (not butt(snakelist,snakehead,180)):
                    direction = 180
                    yclead = bsize
                    xclead = 0
            elif (not butt(snakelist,snakehead,90)):
                direction = 90
                xclead = -bsize
                yclead = 0

        print(not butt(snakelist,snakehead,90))
        if (x_lead < xapple):
            if direction == 90 and (not butt(snakelist,snakehead,90)):#(left)
                if (y_lead < yapple) and (not butt(snakelist,snakehead,180)):
                    direction = 180
                    yclead = bsize
                    xclead = 0
                    #faker
                if (y_lead < yapple) and (not butt(snakelist,snakehead,0)):
                    direction = 0
                    yclead = -bsize
                    xclead = 0
                if (y_lead > yapple)and (not butt(snakelist,snakehead,0)):
                    direction = 0
                    yclead = -bsize
                    xclead = 0
                    #faker
                if (y_lead > yapple)and (not butt(snakelist,snakehead,180)):
                    direction = 180
                    yclead = bsize
                    xclead = 0
            elif (not butt(snakelist,snakehead,270)):
                direction = 270
                xclead = bsize
                yclead = 0

        if (x_lead == xapple):
            if (not butt(snakelist,snakehead,180)) and (y_lead < yapple):#(left)
                direction = 180
                yclead = bsize
                xclead = 0
            elif (not butt(snakelist,snakehead,0)) and (y_lead > yapple):
                direction = 0
                yclead = -bsize
                xclead = 0
            elif (not butt(snakelist,snakehead,90)):
                direction = 90
                yclead = 0
                xclead = -bsize
            elif (not butt(snakelist,snakehead,270)):
                direction = 270
                yclead = 0
                xclead = bsize

            if x_lead > width-wall-bsize or x_lead < wall or y_lead < wall or y_lead > height-wall-bsize:
                overg = True
            '''if event.type == pygame.KEYUP:   #só move quando pressionado o butão
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    xclead = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yclear=0
            '''

        dt = clock.tick(fps)
        x_lead+=xclead /2
        y_lead+=yclead /2

        if x_lead+bsize > xapple and x_lead < xapple+thick:
            if y_lead+bsize > yapple and y_lead < yapple+thick:
                xapple = int(random.randrange(bsize,width-bsize,bsize))
                yapple = int(random.randrange(bsize,height-bsize,bsize))
                snakelen+=1
        '''for i in colors:
            gdisplay.fill(colors[i])
            pygame.display.update()
        '''

        gdisplay.fill(colors['brown'])

        gdisplay.blit(applepng,(xapple,yapple))
        snakehead = []
        snakehead.append(x_lead)
        snakehead.append(y_lead)
        snakelist.append(snakehead)

        if len(snakelist) > snakelen:
            del snakelist[0]
        for i in snakelist[:-1]:
            if snakehead == i:
                overg = True

        snake(bsize,snakelist,direction)
        walls()
        #gdisplay.fill(colors[''], rect=[x,y,w,h])
        score(snakelen-1)
        pygame.display.update()
        #pygame.draw.rect(local,cor,[x,y,w,h])
        clock.tick(fps)
    pygame.quit()
    quit()

introg()
gameloop()
