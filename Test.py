import pygame as py

w = py.display.set_mode((600, 600))
py.display.set_caption("Hello World !!!")

screen = py.Surface((600,600))

x = 40
y = 0
Done = True
S_G_R = True
S_G_D = True

def Intersect(x1, x2, y1, y2):
    if (x1 > x2 - 40) and (x1 < x2 + 40):
        if (y1 > y2 - 40) and (y1 < y2 + 40):
            return 1
        else:
            return 0
class Object:
    def __init__(self,x,y,file_name):
        self.x = x
        self.y = y
        self.bitmap = py.image.load(file_name)
        self.bitmap.set_colorkey((25,245,18))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
    def turn(self,angle):
        self.bitmap = py.transform.rotate(self.bitmap, angle)
    def image(self,file_name):
        self.bitmap = py.image.load(file_name)
    def remove(self):
        self.bitmap.fill((0,0,0))
    def move(self):
            self.y += 1
            py.time.delay(5)
            



panzer_one = Object(300,560,'Tank1.png')
panzer_one.up = False
panzer_one.turn(180)
panzer_two = Object(300,10,'Tank1.png')
panzer_two.up = True
panzer_two.turn(180)
panzer_one.turn(-180)
puly = Object(-20,560,'puly.png')
puly.push = False
direction = py.K_UP
py.key.set_repeat(1,1)
puly.direction = py.K_UP
while Done:
    for e in py.event.get():
        if e.type == py.QUIT:
            Done = False
        if e.type == py.KEYDOWN:
            
            if e.key == py.K_UP:
                if panzer_one.y > 0:
                    if direction != py.K_UP:
                        panzer_one.image('Tank1.png')
                    panzer_one.y-=1
                    direction = py.K_UP
                
                    
            if e.key == py.K_DOWN:
                    
                if panzer_one.y < 560:
                    if direction != py.K_DOWN:
                        panzer_one.image('Tank_d.png')
                    panzer_one.y+=1
                    direction = py.K_DOWN
                    
            if e.key == py.K_RIGHT:
                if panzer_one.x < 560:
                    if direction != py.K_RIGHT:
                        panzer_one.image('Tank_r.png')
                    panzer_one.x+=1
                    direction = py.K_RIGHT
                    
            if e.key == py.K_LEFT:
                if panzer_one.x > 0:
                    if direction != py.K_LEFT:
                        panzer_one.image('Tank_l.png')
                    panzer_one.x-=1
                    direction = py.K_LEFT
                
                    
           
            
            if e.key == py.K_SPACE:
                    if puly.push == False:
                        puly = Object(-20,560,'puly.png')
                        puly.x = panzer_one.x+10
                        puly.y = panzer_one.y+10
                        puly.push = True
                        if  direction == py.K_UP:
                            puly.direction = py.K_UP
                        if  direction == py.K_DOWN:
                            puly.direction = py.K_DOWN
                        if  direction == py.K_LEFT:
                            puly.direction = py.K_LEFT
                        if  direction == py.K_RIGHT:
                            puly.direction = py.K_RIGHT
    
      
    
    if puly.y < 0 or puly.x < 0 or puly.y > 580 or puly.x > 580 :
                puly.push = False
    
    
    if puly.push == False:
                puly.x = -20  
                puly.y = 560
    elif puly.direction ==py.K_UP:
                puly.y -= 2
    elif puly.direction ==py.K_DOWN:
                puly.y += 2
    elif puly.direction ==py.K_LEFT:
                puly.x -= 2
    elif puly.direction == py.K_RIGHT:
                puly.x += 2
    
    screen.fill((0,0,0))
    panzer_two.move()
    puly.render()
        
    if Intersect(puly.x, panzer_two.x, puly.y, panzer_two.y):
        puly.push = False
        panzer_two.remove()
        print('ok')   
        
   
    
    panzer_two.render()
    panzer_one.render()
 
    w.blit(screen,(0,0)) 
   
    
    py.display.flip()
    py.time.delay(5)
    
    

