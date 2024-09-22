#window dimensions
import random

WIDTH = 600
HEIGHT = 600

# Variables
fox = Actor("foxright.png")
fox.pos = (WIDTH // 2, HEIGHT // 2)

ghost_list = []

def spawn_actor_randomly(actor):
    actor.x = random.randint(0, WIDTH - 50)  
    actor.y = random.randint(0, HEIGHT - 50)  

for _ in range(1):
    ghost = Actor("ghost2.png")
    spawn_actor_randomly(ghost)
    ghost_list.append(ghost)

score = 0
lives = 3
game_over = False
fox_costumes = ["foxright.png", "foxleft.png"]
costume_index = 0

heart = Actor("heart.png")
spawn_actor_randomly(heart)

shield = Actor("shield.png")
spawn_actor_randomly(shield)

shield_active = False
shield_timer = 0
shield_visible = True
wait = 0

# Draw loop
def draw():
    if not game_over:
        screen.fill("Light Pink")
        fox.draw()
        heart.draw()

        if shield_visible:
            shield.draw()

        for ghost in ghost_list:
            ghost.draw()

        screen.draw.text("Score: " + str(score), (20, 20), color="ivory")
        screen.draw.text("Lives: " + str(lives), (20, 50), color="ivory")

        if shield_active:
            screen.draw.text("Shield Active!", (WIDTH - 150, 20), color="yellow")
    else:
        screen.fill("black")
        screen.draw.text("Game Over!", center=(WIDTH / 2, HEIGHT / 2), color="red", fontsize=50)
        screen.draw.text("Press R to Restart", center=(WIDTH / 2, HEIGHT / 2 + 50), color="blue", fontsize=30)

# Update loop
def update():
    global score, costume_index, wait, shield_active, shield_timer, shield_visible, lives, game_over

    if game_over:
        if keyboard.r:
            reset_game()
        return

    fox.image = fox_costumes[costume_index]
    if keyboard.right and fox.x < WIDTH:
        fox.x += 5
        costume_index = 0
    if keyboard.left and fox.x > 0:
        fox.x -= 5
        costume_index = 1
    if keyboard.down and fox.y < HEIGHT:
        fox.y += 5
    if keyboard.up and fox.y > 0:
        fox.y -= 5

    if fox.colliderect(heart):
        spawn_actor_randomly(heart)
        score += 1
        for ghost in ghost_list:
            spawn_actor_randomly(ghost)

    for ghost in ghost_list:
        if shield_active:
            continue

        if ghost.x < fox.x:
            ghost.x += 2  
        if ghost.x > fox.x:
            ghost.x -= 2  
        if ghost.y < fox.y:
            ghost.y += 2  
        if ghost.y > fox.y:
            ghost.y -= 2  

        if fox.colliderect(ghost):
            lives -= 1
            if lives <= 0:
                game_over = True
            spawn_actor_randomly(ghost)

    if shield_visible and fox.colliderect(shield):
        shield_active = True
        shield_timer = 300
        shield_visible = False

    if shield_active:
        shield_timer -= 1
        if shield_timer <= 0:
            shield_active = False

    if not shield_visible and random.randint(0, 1000) < 5:
        shield_visible = True
        spawn_actor_randomly(shield)


    if score % 3 == 0 and score != 0 and wait == 0:
        new_ghost = Actor("ghost2.png")
        spawn_actor_randomly(new_ghost)
        ghost_list.append(new_ghost)
        wait = 300  
    if wait > 0:
        wait -= 1

def reset_game():
    global score, lives, game_over, ghost_list, shield_visible, shield_active, shield_timer
    score = 0
    lives = 3
    game_over = False
    ghost_list = []
    for _ in range(1):
        ghost = Actor("ghost2.png")
        spawn_actor_randomly(ghost)
        ghost_list.append(ghost)
    spawn_actor_randomly(heart)
    fox.pos = (WIDTH // 2, HEIGHT // 2)
    shield_visible = True
    shield_active = False
    shield_timer = 0
    spawn_actor_randomly(shield)
