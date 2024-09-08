# window dimension
import random

WIDTH = 600
HEIGHT = 600

#variables
fox = Actor ("foxright.png")
fox.x = 300
fox.y = 300
ghost_list = []

for i in range(1):
    ghost = Actor ("ghost2.png")
    ghost.x = random.randint (0, 600)
    ghost.y = random.randint (0, 600)
    ghost_list.append(ghost)

score = 0

fox_costumes = ["foxright.png", "foxleft.png"]
i = 0

heart = Actor ("heart.png")
heart.x = random.randint (0, 600)
heart.y = random.randint (0, 600)
wait = 0
#drawloop
def draw():
    screen.fill("Light Pink")
    fox.draw()
    heart.draw()
    for ghost in ghost_list:
        ghost.draw()
    screen.draw.text("score: "+ str(score), (20, 20), color = "ivory")

#update loop
def update ():
    global score, i, wait
    fox.image = fox_costumes [i%2]
    if keyboard.right and fox.x<WIDTH:
        fox.x = fox.x +5
        i=0
    if keyboard.left and fox.x>0:
        fox.x = fox.x-5
        i=1
    if keyboard.down and fox.y<HEIGHT:
        fox.y = fox.y+5

    if keyboard.up and fox.y>0:
        fox.y = fox.y-5

    if fox.colliderect(heart):
        heart.x = random.randint(0,600)
        heart.y = random.randint(0,600)
        score = score + 1
        for ghost in ghost_list:
            ghost.x = random.randint (0, 600)
            ghost.y = random.randint (0, 600)

    for ghost in ghost_list:
        if fox.colliderect(ghost):
            score = 0
            ghost.x = random.randint (0, 600)
            ghost.y = random.randint (0, 600)

    if wait > 0:
        wait = wait -1
    if score%3 == 0 :
        if wait == 0:
            ghost = Actor ("ghost2.png")
            ghost.x = random.randint (0, 600)
            ghost.y = random.randint (0, 600)
            ghost_list.append(ghost)
            wait = 300





