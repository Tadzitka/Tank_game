import pgzrun
import random

class Bullet(Actor):
    def __init__(self,x,y):
        super(Bullet, self).__init__('bullet', (x,y))
        self.pos=x,y
        self.angle=90
        self.shot=0

    def fly(self):
        self.y-=4
    def draw(self):
        if self.shot==1:
            super(Bullet,self).draw()
            self.fly()
        if self.y<=-50:
            self.shot=0

class Tank():
    def __init__(self,x,y,WIDTH,HEIGHT):
        self.Zycie = Zycie(810, 675)
        self.track=Actor('tank_track')
        self.body=Actor('tank_body')
        self.turret=Actor('tanks_turret')
        self.game_size=(WIDTH,HEIGHT)
        self.track.pos=x,y-15
        self.body.pos=x+3,y-35
        self.turret.angle=90
        self.turret.pos=x+10,y-65
        self.MyBullet = Bullet(200, 200)

    def left(self,x):
        if self.track.x-40>=0:
            self.track.x-=x
            self.body.x-=x
            self.turret.x-=x

    def right(self,x):
        if self.track.x<=WIDTH-50:
            self.track.x +=x
            self.body.x +=x
            self.turret.x +=x
    def collidepoint(self,other):
        if self.body.collidepoint(other.pos):
            return True
        else:
            return False

    def shot(self):
        if self.MyBullet.shot==0:
            self.MyBullet.pos=self.turret.x,self.turret.y
            self.MyBullet.shot=1

    def draw(self):
        self.track.draw()
        self.turret.draw()
        self.body.draw()
        self.MyBullet.draw()
        self.Zycie.draw()
class Zycie():
    def __init__(self,x,y):
        self.s1 = Actor("heart")
        self.s2 = Actor("heart")
        self.s3 = Actor("heart")
        self.s1.pos = x,y
        self.s2.pos = x + 35,y
        self.s3.pos = x + 70,y
        self.licznik = 3
        self.zmiana = 0

    def zmniejsz(self):
        if self.zmiana == 0:
            self.licznik -= 1
            self.zmiana = 1
            clock.schedule_unique(Z, 1.0)
    def draw(self):
        if self.licznik == 1:
            self.s1.draw()
        elif self.licznik == 2:
            self.s1.draw()
            self.s2.draw()
        elif self.licznik == 3:
            self.s1.draw()
            self.s2.draw()
            self.s3.draw()

class Bullet_enemy(Actor):
    def __init__(self,x,y):
        super(Bullet_enemy, self).__init__('bullet', (x,y))
        self.pos=x,y
        self.angle=-90
        self.shot=0

    def fly(self):
        self.y+=4
    def draw(self):
        if self.shot==1:
            super(Bullet_enemy,self).draw()
            self.fly()
        if self.y>=HEIGHT:
            self.shot=0

class Przeciwnik():
    def __init__(self,x,y,WIDTH,HEIGHT):
        self.track=Actor('tank_track')
        self.body=Actor('tankbody')
        self.turret=Actor('tanks_turret')
        self.game_size=(WIDTH,HEIGHT)
        self.Zycie_p = Zycie_p(20, 20)
        self.track.pos=x,y
        self.body.pos=x-2,y+21
        self.turret.angle=-90
        self.body.angle=180
        self.turret.pos=x-10,y+50
        self.MyBullet = Bullet_enemy(200, 200)
        self.ruch=0

    def left(self,x):
        if self.track.x-40>=0:
            self.track.x-=x
            self.body.x-=x
            self.turret.x-=x

    def right(self,x):
        if self.track.x<=WIDTH-50:
            self.track.x +=x
            self.body.x +=x
            self.turret.x +=x
    def shot(self):
        if self.MyBullet.shot==0:
            self.MyBullet.pos=self.turret.x,self.turret.y+10
            self.MyBullet.shot=1
    def fly(self):
        self.y+=4

    def draw(self):
        self.Zycie_p.draw()
        self.track.draw()
        self.turret.draw()
        self.body.draw()
        self.MyBullet.draw()
    def collidepoint(self,other):
        if self.body.collidepoint(other.pos):
            return True
        else:
            return False
    def update(self):
        if self.ruch == 0:
            los = random.randint(0,11)
            czas = random.random()
            clock.schedule_unique(ruch, czas)
            self.shot()
            if los %2 == 0:
                self.ruch = 1
            else:
                self.ruch= -1
        elif self.ruch == 1:
            self.right(3)
        elif self.ruch == -1:
            self.left(3)
class Zycie_p():
    def __init__(self,x,y):
        self.sp1 = Actor("heart_prze")
        self.sp2 = Actor("heart_prze")
        self.sp3 = Actor("heart_prze")
        self.sp1.pos = x,y
        self.sp2.pos = x + 35,y
        self.sp3.pos = x + 70,y
        self.licznik = 3
        self.zmiana = 0
    def zmniejsz(self):
        if self.zmiana == 0:
            self.licznik -= 1
            self.zmiana = 1
            clock.schedule_unique(Z_p, 1.0)
    def draw(self):
        if self.licznik == 1:
            self.sp1.draw()
        elif self.licznik == 2:
            self.sp1.draw()
            self.sp2.draw()
        elif self.licznik == 3:
            self.sp1.draw()
            self.sp2.draw()
            self.sp3.draw()
class Ekslpozja():
    def __init__(self, x, y):
        self.eks = Actor("eksplozja1",(x,y))
    

WIDTH = 900
HEIGHT = 700


tank = None
enemy = None

def ruch():
    global enemy
    enemy.ruch = 0
def Z():
    global tank
    tank.Zycie.zmiana = 0
def Z_p():
    global enemy
    enemy.Zycie_p.zmiana = 0

stan_gry = 0 #początek-0, gra-1, koniec_p - 2, koniec_w - 3

def draw():
    screen.fill((26, 43, 173))
    for i in range(13):
        screen.blit("grass", (70 * i, 630))
    for i in range(13):
        screen.blit("grass2", (70 * i, 0))
    if stan_gry == 0:
        screen.draw.text("Kliknij SPACJA aby rozpocząć gre", (100, 350), color="red",fontsize=60)
    elif stan_gry == 1:
        tank.draw()
        enemy.draw()
    elif stan_gry == 2:
        screen.draw.text("Przegrałeś :(", (300, 350), color="red", fontsize=60)
        screen.draw.text("Kliknij SPACJA aby rozpocząć gre", (100, 420), color="red", fontsize=60)
    elif stan_gry == 3:
        screen.draw.text("Wygrałeś :)", (300, 350), color="red", fontsize=60)
        screen.draw.text("Kliknij SPACJA aby rozpocząć gre", (100, 420), color="red", fontsize=60)


def update():
    global stan_gry
    sprawdz_klawisze()
    if stan_gry == 1:
        enemy.update()
        if tank.collidepoint(enemy.MyBullet):
            tank.Zycie.zmniejsz()
        if enemy.collidepoint(tank.MyBullet):
            enemy.Zycie_p.zmniejsz()
        if enemy.Zycie_p.licznik <= 0:
            stan_gry = 3
        if tank.Zycie.licznik <= 0:
            stan_gry = 2

def sprawdz_klawisze():
    global stan_gry
    global enemy
    global tank
    if stan_gry == 1 and keyboard.left:
        tank.left(3)
    if stan_gry == 1 and keyboard.right:
        tank.right(3)
    if stan_gry == 1 and keyboard.up:
        tank.shot()
    if keyboard.space:
        if stan_gry != 1:
            stan_gry = 1
            tank=Tank(350,629,WIDTH,HEIGHT)
            enemy=Przeciwnik(350,87,WIDTH,HEIGHT)

pgzrun.go()