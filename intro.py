import pgzrun

obj = Actor('object.png')
obj.left = 10
obj.y = 400

obj2 = Actor('object.png')
obj2.left = 10
obj2.y = 200 

cxk = Actor('cxk2.png')
cxk.top=10
cxk.x = 300

WIDTH = 600
HEIGHT = 600
pressed = False
counter = 0 
def draw():
    screen.fill((255,255,255))
    cxk.draw()
    obj.draw()
    obj2.draw()
    screen.draw.text("score:  "+str(counter),(90,30),color = (40,40,10),fontsize = 50)
def update():
    global pressed
    global counter
    obj.left += 3
    obj2.left += 2

    if obj.right > WIDTH:
        obj.left = 10
    if obj2.right > WIDTH:
        obj2.left = 10
    if pressed == True:
        cxk.bottom += 5
    if keyboard.down:
        pressed = True
    if cxk.bottom >HEIGHT:
        cxk.top = 10
        counter = counter + 1
        pressed = False
    if cxk.colliderect(obj):
        sounds.err.play()
        cxk.top=10
        counter = 0
        pressed = False
    if cxk.colliderect(obj2):
        sounds.err.play()
        cxk.top=10
        counter = 0
        pressed = False
        print('你没有只因只因')
        
        
        
        
pgzrun.go()
