# Write your code here :-)
character = Actor('character_before.png')
character.topright= 100,56

WIDTH = 500
HEIGHT = character.height + 50

def draw():
    screen.clear()
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

def on_mouse_down():
    print("You clicked!")
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.mixkit-martial-arts-fast-punch-2047.wav()
        character.image = 'character_after.png.png'

def on_mouse_down(pos):
    if character.collidepoint(pos):
        sounds.eep.play()
        character.image = 'character_after.png.png'
        time.sleep(1)
        character.image = 'character_after.png.png'


