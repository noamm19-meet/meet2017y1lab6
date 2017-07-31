UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
SPACEBAR='space'
UP=0
LEFT=1
DOWN=2
RIGHT=3
direction=UP
def up():
    global direction
    direction=0
    print('you pressed up')
def down():
    global direction
    direction=1
    print('you pressed down')
    
    
