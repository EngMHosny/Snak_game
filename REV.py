#import LIB
import curses
import random

#initialize curses lib
screen = curses.initscr()

#hide mouse curses
curses.curs_set(0)

#get size of screen
screen_hight,screen_width = screen.getmaxyx()

# create window
window = curses.newwin(screen_hight, screen_width, 0, 0)

#allow keybad
window.keypad(1)

#delay to update screen
window.timeout(125)

#snak head
snk_x = screen_width // 4
snk_y = screen_hight // 2

#snak Body Initialization position
snak = [
    [snk_y, snk_x],     #0 head
    [snk_y,snk_x-1],    #1 body
    [snk_y,snk_x-2]     #2 tail
]

#create snak's food ==> position
food = [screen_hight//2, screen_width//2]

#add food as PI letter
window.addch(food[0], food[1],curses.ACS_PI)

#initialization Movement
key = curses.KEY_RIGHT

#looping
while True :
    next_key = window.getch() ## defualt value is -1

#Accebt new direction from user
    key = key  if next_key == -1 else next_key

    #if snak crached walls or its self
    if snak[0][0] in [0,screen_hight] or snak[0][1] in [0,screen_width] or snak[0] in snak[1:] :
        curses.endwin() #close window
        quit()#quit screen

    #set head position according to user Key

    new_head = [ snak[0][0] , snak[0][1] ]

    if key == curses.KEY_DOWN:
        new_head[0] += 1

    if key == curses.KEY_UP:
        new_head[0] -= 1

    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    #insert New Head In Snak Body
    snak.insert(0, new_head)

    #snak ate food
    if snak[0] == food :
        food = None #remove food
        while food == None :
            new_food = [
                random.randint(0,screen_hight-1),
                random.randint(0,screen_width-1)]
            food = new_food if new_food not in snak else None
        window.addch(food[0], food[1],curses.ACS_PI)
    #food didn't take
    else:
        tail = snak.pop()
        window.addch(tail[0], tail[1],' ') #remove the tail because we add a new head in line # 73

    # add snak body shape in screen
    window.addch(snak[0][0], snak[0][1],'O')