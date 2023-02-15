from random import randint
WIDTH = 600
HEIGHT = 400
score = 0
game_over = False
hedgehog = Actor("hedgehog")
hedgehog.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.blit('background', (0, 0))
    hedgehog.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        hedgehog.x = hedgehog.x - 7
    elif keyboard.right:
        hedgehog.x = hedgehog.x + 7
    elif keyboard.up:
        hedgehog.y = hedgehog.y - 7
    elif keyboard.down:
        hedgehog.y = hedgehog.y +


    coin_collected = hedgehog.colliderect(coin)


    if coin_collected:
        score = score + 10
        place_coin()


clock.schedule(time_up, 45.0)
place_coin()
