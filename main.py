# Fill me in!
import random
from cmu_graphics import *

app.background = 'papayaWhip'
Rect(0,0,400,130, fill = 'moccasin', border = "black")
pop = Sound("cmu://1131798/4548338/dragon-studio-pop-402324.mp3")
music = Sound("cmu://1131798/4564686/nojisuma-street-at-night-167545.mp3")

music.play()

#create the paints
##def paintsCans(x,y, color):
##     Circle(x,y,20, fill = color, border = "black")

app.starColorList = ['lightYellow', 'pink', 'lavender', 'lightCyan', 'lemonChiffon']

red = Circle(40,40,20, fill = "red", border = "black")
orange = Circle(90,40,20, fill = "orange", border = "black")
yellow = Circle(140,40,20, fill = "gold", border = "black")
green = Circle(190,40,20, fill = "green", border = "black")
blue = Circle(240,40,20, fill = "blue", border = "black")
navy = Circle(290,40,20, fill = "navy", border = "black")
purple = Circle(340,40,20, fill = "black", border = "black")

darkRed = Circle(40,90,20, fill = "darkRed", border = "black")
darkOrange = Circle(110,90,20, fill = "saddleBrown", border = "black")
khaki = Circle(160,90,20, fill = "khaki", border = "black")
darkGreen = Circle(210,90,20, fill = "darkGreen", border = "black")
midnightBlue = Circle(260,90,20, fill = "lightBlue", border = "black")
indigo = Circle(310,90,20, fill = "black", border = "black")
white = Circle(360,90,20, fill = "white", border = "black")

#window Light
app.LightOn = Group(Circle(110,340, 20, fill = gradient( "lightYellow","darkOrange", start = 'center')),
                     Rect(90,320, 40,40, fill = None, border = 'saddleBrown', borderWidth = 5),
                     Line(110, 320, 110, 360, fill = 'saddleBrown', lineWidth = 5),
                     Line(90,340, 130,340, fill = 'saddleBrown', lineWidth = 5))

app.LightOn.visible = False

#person
app.person1 = Group(Circle(225,310, 10), Polygon(225,310,215,350,235,350),
                     Line(225, 350, 225, 380, lineWidth = 8))

app.person2 = Group(Circle(270,310, 10), Polygon(270,365,260,320,280,320),
                     Line(270, 350, 270, 380, lineWidth = 8))

app.person1.visible = False
app.person2.visible = False

#color index
app.i=0

#star
app.star = Star(200,200,50,5, fill = "white")
app.star.visible = False

def onMouseMove(mouseX, mouseY):
    brush.rotateAngle = 30
    brush.centerX = mouseX
    brush.centerY = mouseY
    if(mouseY < 130):
        brush.visible = False
    
    elif(darkRed.hits(mouseX, mouseY)):
        Polygon(0,250, 0,400, 160,400, 160,300, 130,250, 30,250, fill = "red", border = "black")
        brush.toFront()
    
    if(darkRed.hits(mouseX, mouseY)):
        Polygon(30,250, 60,300, 160,300, 160,400, 0,400, 0,250, fill = "darkRed", border = "black", opacity = 60)
        Rect(60,300, 100,100, fill = "darkRed", border = "black")
        brush.toFront()
    
    if(orange.hits(mouseX, mouseY)):
        Rect(90,320, 40,40, fill = None, border = 'darkOrange')
        brush.toFront()
    
    if(darkOrange.hits(mouseX, mouseY)):
        Rect(90,320, 40,40, fill = None, border = 'saddleBrown', borderWidth = 5)
        Line(110, 320, 110, 360, fill = 'saddleBrown', lineWidth = 5)
        Line(90,340, 130,340, fill = 'saddleBrown', lineWidth = 5)
        brush.toFront()
    
    if(yellow.hits(mouseX, mouseY)):
        if(app.isLightOn == False):
            app.LightOn.visible = True
            app.isLightOn = True
            app.LightOn.toFront()
            brush.toFront()
        else:
            app.LightOn.visible = False
            app.isLightOn = False
            brush.toFront()
    
    if(khaki.hits(mouseX, mouseY)):
        Polygon(30,250, 60,300, 160,300, 160,400, 0,400, 0,250, fill = "khaki", border = 'black', opacity = 50)
        brush.toFront()
    
    if(green.hits(mouseX, mouseY)):
        Rect(0,380, 400,20, fill = "green")
        brush.toFront()
    
    if(darkGreen.hits(mouseX, mouseY)):
        Rect(0,380, 400,20, fill = gradient("green", "darkGreen", start = "top"))
        brush.toFront()
    
    if(blue.hits(mouseX, mouseY)):
        Rect(0,130, 400,250, fill = "blue")
        brush.toFront()
    
    if(midnightBlue.hits(mouseX, mouseY)):
        Rect(0,130, 400,250, fill = gradient("Blue","Blue","Blue", "lightBlue", start = "top"))
        app.house.toFront()
        brush.toFront()
        Rect(0,380, 400,20, fill = gradient("green", "darkGreen", start = "top"))
        brush.toFront()
    
    if(navy.hits(mouseX, mouseY)):
        night = Rect(0,130, 400,300, fill = gradient("navy","Blue","Blue", "lightBlue", start = "top"))
        brush.toFront()
        app.house.toFront()
        brush.toFront()
        Rect(0,380, 400,20, fill = gradient("green", "darkGreen", start = "top"))
        brush.toFront()
    
    if(indigo.hits(mouseX, mouseY)):
        app.person1.visible = True
        app.person1.toFront()
        brush.toFront()
    
    if(white.hits(mouseX, mouseY)):
        app.star.visible = True
        onStar()
        brush.toFront()


def creatStarBurst(centerX, centerY):
    if(centerY > 130):
        for i in range(len(app.starColorList)):
            offsetX = random.randint(-50,50)
            offsetY = random.randint(-50,50)
            Star(centerX-28 + offsetX ,centerY+48 + offsetSetY,7, 5, fill = app.starColorList[i])

def onStar():
    if(app.star.opacity >= 10):
        app.star.visible = True
        app.star.radius += 5
        app.star.opacity -= 7
    
    else:
        app.star.opacity = 0
        app.star.visible = False

def onMousePress(mouseX, mouseY):
    pop.play()
    brush.toFront()
    if(mouseY < 130):
        if(red.hits(mouseX, mouseY)):
            Polygon(0,300, 0,400, 160,400, 160,300, 130,250, 30,250, fill = "red", border = "black")
            brush.toFront()
    
    if(darkRed.hits(mouseX, mouseY)):
        Polygon(30,250, 60,300, 160,300, 160,400, 0,400, 0,250, fill = "red", border = "black")
        brush.toFront()
    
    if(orange.hits(mouseX, mouseY)):
        Rect(90,320, 40,40, fill = None, border = 'darkOrange')
        brush.toFront()
    
    if(darkOrange.hits(mouseX, mouseY)):
        Rect(90,320, 40,40, fill = None, border = 'saddleBrown', borderWidth = 5)
        Line(110, 320, 110, 360, fill = 'saddleBrown', lineWidth = 5)
        Line(90,340, 130,340, fill = 'saddleBrown', lineWidth = 5)
        brush.toFront()
    
    if(yellow.hits(mouseX, mouseY)):
        if(app.isLightOn == False):
            app.LightOn.visible = True
            app.isLightOn = True
            app.LightOn.toFront()
            brush.toFront()
        else:
            app.LightOn.visible = False
            app.isLightOn = False
            brush.toFront()
    
    if(khaki.hits(mouseX, mouseY)):
        Polygon(30,250, 60,300, 160,300, 160,400, 0,400, 0,250, fill = "khaki", border = 'black', opacity = 50)
        brush.toFront()
    
    if(green.hits(mouseX, mouseY)):
        Rect(0,380, 400,20, fill = "green")
        brush.toFront()
    
    if(darkGreen.hits(mouseX, mouseY)):
        Rect(0,380, 400,20, fill = gradient("green", "darkGreen", start = "top"))
        brush.toFront()
    
    if(blue.hits(mouseX, mouseY)):
        Rect(0,130, 400,250, fill = "blue")
        brush.toFront()
    
    if(purple.hits(mouseX, mouseY)):
        app.person1.visible = True
        app.person1.toFront()
        brush.toFront()
    
    if(indigo.hits(mouseX, mouseY)):
        app.person2.visible = True
        app.person2.toFront()
        brush.toFront()
    
    if(white.hits(mouseX, mouseY)):
        app.star.visible = True
        onStar()
        brush.toFront()
    
    else:
        creatStarBurst(mouseX, mouseY)
        brush.toFront()


brush.toFront()
