GlowScript 2.7 VPython
#
# Mario_Game
#Bea Litonjua
#Denise Hernandez
#
# Building an interaction with 3D graphics using python
#   Documentation: http://www.glowscript.org/docs/GlowScriptDocs/index.html
#   Examples:      http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#
scene.bind('keydown', keydown_fun)     # Function for key presses
#scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = color.black 
"""vector(0.034, 0.000, 0.246)""" # Light gray (0.8 out of 1.0)
scene.width = 1000                      # Make the 3D canvas larger
scene.height = 550
scene.userspin = False
scene.range = 10
scene.userzoom = False
scene.forward = vector(0,-0.15, -1)
scene.ambient = color.white
# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"
def make_alien(starting_position, starting_vel = vector(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vector(0, 0, 0).
       Compounds can have any number of components.  Here the
       alien's components:
    """
    alien_body = sphere(size = 1.0*vector(1, 1, 1), pos = vector(0, 0, 0), color = color.green)
    alien_eye1 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.7, .5, .2), color = color.white)
    alien_eye2 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.2, .5, .7), color = color.white)
    alien_hat = sphere(pos = 0.42*vector(0, .9, -.2), axis = vector(.02, .2, -.02), size = vector(0.2, 0.7, 0.7), color = color.magenta)
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_hat]  # make a list to "fuse" with a compound
    # now, we create a compound -- we'll name it com_alien:
    com_alien = compound(alien_objects, pos = starting_position)
    com_alien.vel = starting_vel   # set the initial velocity
    return com_alien
def make_alien_row(colour, starting_position, starting_vel = vector(1,0,0)):
    """ makes a block that will oscillate back and forth in game 
    """
    wallE = box(color = colour, pos = vector(0,0,0), axis = vector(1, 0, 0), size = vector(20, 1, 1.5), opacity = 1)
    com_alien_row = compound([wallE], pos = starting_position)
    com_alien_row.vel = starting_vel
    return com_alien_row
    
def make_row2(colour, starting_position, starting_vel = vector(1,0,0)):
    """Makes a block with a gap in the middle that will also oscillate back and forth
    """
    wallE = box(color = colour, pos = vector(-7,0,0), axis = vector(1, 0, 0), size = vector(12, 1, 1.5), opacity = 1)
    wallF = box(color = colour, pos = vector(12,0,0), axis = vec(1,0,0), size = vector(12, 1, 1.5), opacity = 1)
    com_make_row2 = compound([wallE,wallF], pos = starting_position)
    com_make_row2.vel = starting_vel
    return com_make_row2
    
def make_mario(starting_position, starting_vel = vec(1,0,0)):
    """Makes a Mario character that will act as an enemy!
    """
    rand = randcolor()
    mario_body1 = sphere(size=0.8*vector(1,1,1),  pos=vector(0,0,0),  color=rand)
    mario_body2 = sphere(size=0.50*vector(1,1,1),  pos=vector(0.2,0,0),  color=color.blue)
    mario_head = sphere(size = 0.8*vector(1,1,1), pos=vector(0,0.7,0), color=vector(1,0.999,0.7))
    mario_hat =sphere(size = 0.7*vector(1,1,1.2), pos=vector(0,0.9,0), color=rand)
    mario_hat2 =sphere(size = 0.4*vector(1,1,1.2), pos=vector(0,0.5,0), color=rand)
    mario_shoesL = box(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(0.09, -0.7, -0.25), color = rand)
    mario_shoesR = box(size = 1.4*vector(0.3, 0.3, 0.3), pos = vector(-0.31, -0.7, 0.25), color = rand)
    mario_shoesWL = box(size = 1.1*vector(0.3, 0.3, 0.3), pos = vector(0.09, -0.65, -0.25), color = rand)
    mario_shoesWR = box(size = 1.1*vector(0.3, 0.3, 0.3), pos = vector(-0.31, -0.65, 0.25), color = rand)
    mario_legL = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.000001,-0.45,-0.2), axis = vector(-1,1,1), color=color.blue)
    mario_legR = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.1,-0.45,0.2), axis = vector(1,1,-1), color=color.blue)
    mario_moustache = sphere(size=0.60*vector(1,0.5,.8), pos=vector(0.15,0.55,0), axis=vector(0,0,1), color=vector(0.46,0.28,0.10))
    mario_nose = sphere(size=0.2*vector(0.5,0.5,0.7), pos=vector(0.5,0.55,0), axis=vector(1,0.5,0), color=vector(1,0.999,0.7)) 
    mario_eye1 = sphere(size=0.4*vector(1,1,1), pos=vector(0.2,0.7,-0.1), axis=vector(1,0.5,0), color=color.white)
    mario_eye2 = sphere(size=0.4*vector(1,1,1), pos=vector(0.2,0.7,0.1), axis=vector(1,0.5,0), color=color.white)
    mario_arm1 = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.000001,0,0.4), axis = vector(-1,-1,1), color=color.blue)
    mario_arm2 = box(size=0.8*vector(0.6,0.1,0.2), pos=vector(-0.000001,0,-0.4), axis = vector(-1,-1,1), color=color.blue)
    mario_glove1 = sphere(size=0.35*vector(1,1,1),  pos=vector(0.1,0.2,-0.6),  color=color.white)
    mario_glove2 = sphere(size=0.35*vector(1,1,1),  pos=vector(-0.1,-0.2,0.5),  color=color.white)
    mario_list = [mario_body1, mario_body2, mario_head, mario_hat, mario_hat2, mario_shoesL, mario_shoesR, mario_shoesWL, mario_shoesWR, mario_legL, mario_legR,
    mario_moustache, mario_nose, mario_eye1, mario_eye2, mario_arm1, mario_arm2, mario_glove1, mario_glove2]  # make a list to "fuse" with a compound
    com_mario = compound(mario_list, pos = starting_position)
    com_mario.vel = starting_vel
    return com_mario
def make_shroom(starting_position, starting_vel = vec(0,0,0)):
    """Makes a shroom/ toad character that will serve as decorum in the game/ shroomie points
    """
    shroom_head = cylinder(size=0.7*vector(.8,.6,.5),pos=vector(0,0,0),color=vector(1,0.999,0.7 ), axis = vector(0,0.2,0))
    circ = shapes.circle(radius=3)
    circpath = paths.circle(radius=3)
    shroom_eye = sphere(size=0.2*vector(0.8,0.5,0.25), pos=vector(-0.1,0.1,.15), axis=vector(0,1,0), color=color.black)
    shroom_eye2 = sphere(size=0.2*vector(0.8,0.5,0.25), pos=vector(0.1,0.1,.15), axis=vector(0,1,0), color=color.black)
    hat = extrusion(path=circpath, shape=circ, color=color.red, size=vector(.8,.53,.8), pos=vector(0,0.5,0),radius=5)
    shroom_circ= sphere(size= 0.4*vector(1,1,1), color=color.white, pos= vector(0,0.5,.24), radius = 4)
    shroom_circ2= sphere(size= 0.4*vector(1,1,1), color=color.white, pos= vector(0,0.5,-.24), radius = 4)
    shroom_circ3= sphere(size= 0.4*vector(1,1,1), color=color.white, pos= vector(.24,0.5,0), radius = 4)
    shroom_circ4= sphere(size= 0.4*vector(1,1,1), color=color.white, pos= vector(-.24,0.5,0), radius = 4)
    #make a list to fuse with compund 
    shroom_list= [shroom_head,shroom_eye,shroom_eye2,hat,shroom_circ,shroom_circ2,shroom_circ3,shroom_circ4]
    com_shroom = compound(shroom_list, pos= starting_position)
    com_shroom.vel = starting_vel
    return com_shroom
    
def make_spaceship(starting_position, starting_vel = vector(0, 0, 0)):
    """Makes a spaceship compound."""
    spaceship_body = sphere(size = 2.0*vector(1, 1, 1), pos = vector(0, 1, 0), color = randcolor())
    alien_cylinder = cylinder(pos = 1*vector(0, 0, 0), axis = vector(0, 0.05, 0), size = vector(0.95, 5, 4), color = color.gray(.8))
    spaceship_objects = [spaceship_body, alien_cylinder]  # make a list to "fuse" with a compound
    com_spaceship = compound(spaceship_objects, pos = starting_position)
    com_spaceship.vel = starting_vel   # set the initial velocity
    return com_spaceship
red = vector(1.000, 0.000, 0.000)
orange = vector(1.000, 0.309, 0.000)
yellow = vector(1.000, 1.000, 0.000)
green = vector(0.000, 1.000, 0.000)
blue = vector(0.000, 0.000, 1.000)
violet = vector(1.000, 0.000, 1.000)
alien_row1 = make_alien_row(red, starting_position=vector(choice(list(range(-15,15))), 0, -20), starting_vel = vector(10,0,0))
mario_2 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -45), starting_vel=vector(5, 0, 1))
alien_row2 = make_alien_row(orange, starting_position=vector(choice(list(range(-15,15))),0,-50), starting_vel=vector(-10,0,0))
mario_1 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -75), starting_vel=vector(5, 0, 1))
block2_1 = make_row2(yellow, starting_position=vector(0, 0, -80), starting_vel = vector(10,0,0))
mario_3 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -105), starting_vel=vector(5, 0, 1))
alien_row4 = make_alien_row(green, starting_position=vector(choice(list(range(-15,15))),0,-110), starting_vel=vector(-10,0,0))
mario_4 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -135), starting_vel=vector(5, 0, 1))
alien_row5 = make_alien_row(blue, starting_position=vector(choice(list(range(-15,15))),0,-140), starting_vel=vector(10,0,0))
black_hole1 = cylinder(pos = vec(0,0,-152.5),color = color.blue, axis = vec(0, 1, 0), size = vec(0.05, 1, 1))
mario_5 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -165), starting_vel=vector(5, 0, 1))
block2_2 = make_row2(violet, starting_position=vector(0, 0, -170), starting_vel = vector(10,0,0))
mario_6 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -195), starting_vel=vector(5, 0, 1))
alien_row7 = make_alien_row(red, starting_position=vector(choice(list(range(-15,15))),0,-200), starting_vel=vector(10,0,0))
black_hole2 = cylinder(pos = vec(0,0,-215),color = color.blue, axis = vec(0, 1, 0), size = vec(0.05, 1, 1))
mario_7 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -225), starting_vel=vector(5, 0, 1))
alien_row8 = make_alien_row(orange, starting_position=vector(choice(list(range(-15,15))),0,-230), starting_vel=vector(-10,0,0))
alien_row9 = make_alien_row(yellow, starting_position=vector(choice(list(range(-15,15))), 0, -260), starting_vel = vector(10,0,0))
mario_8 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -285), starting_vel=vector(5, 0, 1))
alien_row10 = make_alien_row(green, starting_position=vector(choice(list(range(-15,15))),0,-265), starting_vel=vector(-10,0,0))
mario_9 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -290), starting_vel=vector(5, 0, 1))
block3_3 = make_row2(blue, starting_position=vector(0, 0, -295), starting_vel = vector(10,0,0))
mario_10 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -320), starting_vel=vector(5, 0, 1))
alien_row11 = make_alien_row(violet, starting_position=vector(choice(list(range(-15,15))),0,-325), starting_vel=vector(-10,0,0))
mario_11 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -350), starting_vel=vector(5, 0, 1))
alien_row12 = make_alien_row(red, starting_position=vector(choice(list(range(-15,15))),0,-355), starting_vel=vector(10,0,0))
black_hole3 = cylinder(pos = vec(0,0,-367.5),color = color.blue, axis = vec(0, 1, 0), size = vec(0.05, 1, 1))
mario_12 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -380), starting_vel=vector(5, 0, 1))
block4_4 = make_row2(violet, starting_position=vector(0, 0, -385), starting_vel = vector(10,0,0))
mario_13 = make_mario(starting_position=vec(choice(range(-14,14)), 0, -410), starting_vel=vector(5, 0, 1))
welcome_shroom = make_shroom( starting_position=vec(10,0,-5), starting_vel=vector(0,0,-1) )
shroom_1 = make_shroom( starting_position=vec(13,0,-45), starting_vel=vector(0,0,0) )
shroom_2 = make_shroom( starting_position=vec(10,0,-45), starting_vel=vector(0,0,0) )
shroom_3 = make_shroom( starting_position=vec(5,0,-45), starting_vel=vector(0,0,0) )
shroom_4 = make_shroom( starting_position=vec(6,0,-45), starting_vel=vector(0,0,0) )
shroom_5 = make_shroom( starting_position=vec(-13,0,-75), starting_vel=vector(0,0,0) )
shroom_6 = make_shroom( starting_position=vec(-9,0,-75), starting_vel=vector(0,0,0) )
shroom_7 = make_shroom( starting_position=vec(0,0,-80), starting_vel=vector(0,0,0) )
shroom_8 = make_shroom( starting_position=vec(-7,0,-75), starting_vel=vector(0,0,0) )
shroom_9 = make_shroom( starting_position=vec(-7,0,-95), starting_vel=vector(0,0,0) )
shroom_10 = make_shroom( starting_position=vec(6,0,-95), starting_vel=vector(0,0,0) )
shroom_11 = make_shroom( starting_position=vec(14,0,-95), starting_vel=vector(0,0,0) )
shroom_12 = make_shroom( starting_position=vec(0,0,-175), starting_vel=vector(0,0,0) )
shroom_13 = make_shroom( starting_position=vec(4,0,-175), starting_vel=vector(0,0,0) )
shroom_14 = make_shroom( starting_position=vec(8,0,-195), starting_vel=vector(0,0,0) )
shroom_15 = make_shroom( starting_position=vec(9,0,-195), starting_vel=vector(0,0,01) )
shroom_16 = make_shroom( starting_position=vec(6,0,-200), starting_vel=vector(0,0,0) )
shroom_17 = make_shroom( starting_position=vec(14,0,-200), starting_vel=vector(0,0,0) )
shrooms_list=[welcome_shroom,shroom_1,shroom_2,shroom_3,shroom_4,shroom_5,shroom_6,shroom_7,shroom_8,shroom_9,shroom_10,shroom_11,shroom_12,shroom_13,shroom_14,shroom_15,shroom_16,shroom_17]
text(text='Hit the welcome shroom for good luck!',align='center', depth=-0.3, color=color.green, pos= vector(10,5,-5))
#
    
    # corral_collide(com_alien)
# The ground is represented by a box (vpython's rectangular solid)
# http://www.glowscript.org/docs/GlowScriptDocs/box.html
# Create two walls, also boxes
original_color = randcolor()
wallB = box(pos = vector(-20, 0, 0), axis = vector(0, 0, 1), size = vector(1600, 2, 1), color = original_color, opacity = 1)
wallC = box(pos = vector(20, 0, 0), axis = vector(0, 0, 1), size = vector(1600, 2, 1), color = original_color, opacity = 1)
wallD = box(pos = vector(0, 0, -500), axis = vector(1, 0, 0), size = vector(10, 2, 1), color = color.black)
text(text='GAME OVER',align='center', depth=-0.3, color=color.green, pos= vector(0,0,-490))
star_maker()
# A ball that we will be able to control
bullet = cylinder(size = 0.4*vector(1, 1, 1), color = color.green)
bullet.vel = vec(0,0,0)
ball = sphere(size = 1.0*vector(1, 1, 1), color = vector(0.8, 0.5, 0.0))   # ball is an object of class sphere
ball.vel = vector(0, 0, 0)     # this is its initial velocity
# +++ end of OBJECT_CREATION section
# +++ start of ANIMATION section
# Other constants
spaceRATE = 10
bulletdt = 1.0/5
spacedt = 1.0/(1.0*spaceRATE)
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.center = vector(5,10,5)
scene.camera.follow(ball)
friction = 1
#Get the starting time 
t1 = clock()
# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
collided = False
alien_L = [alien_row1, alien_row2, alien_row4, alien_row5, alien_row7, alien_row8, alien_row9,  alien_row10, alien_row11,  alien_row12, alien_row12]
mario_L = [mario_1, mario_2, mario_3, mario_4, mario_5, mario_6, mario_7, mario_8, mario_9, mario_10, mario_11, mario_12, mario_13]
second_block = [block2_1, block2_2, block3_3, block4_4]
bullet.visible = False
bullet.pos = ball.pos
#Making a lot of Space Ships!
spaceship_1 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -10), starting_vel = vector(-1, 1, 0))
spaceship_2 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -50), starting_vel = vector(1, 1, 0))
spaceship_3 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -90), starting_vel = vector(-1, 1, 0))
spaceship_4 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -130), starting_vel = vector(-1, 1, 0))
spaceship_5 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -170), starting_vel = vector(-1, 1, 0))
spaceship_6 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -210), starting_vel = vector(-1, 1, 0))
spaceship_7 = make_spaceship(starting_position = vector(choice(list(range(-15,15))), 8, -250), starting_vel = vector(-1, 1, 0))
spaceship_L = [spaceship_1, spaceship_2, spaceship_3, spaceship_5, spaceship_6, spaceship_7]
shroom_counter=0
mario_counter = 0
#Makes a Welcome Text that will be read before the player commences the game
print("Welcome to Space Race! You are a magical ball that must navigate this space track.")
print("Watch out for a head on collison with the moving blocks.... The evil Marios will cause you to restart if touched...")
print("Luckily, you are equipped with a space gun: activate the gun with the space bar to eliminate the Marios.")
print("The toad heads (shroomie bois) do nothing to you, but you can gain shroom points by touching them!")
print("Good space racing!")
#Start of the While Loop
while True:
    rate(RATE)   # maximum number of times per second the while loop runs
    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step
    
    for i in range(len(alien_L)):
        alien_L[i].pos += alien_L[i].vel*dt
        alien_collide(alien_L[i])
    ball.vel *= friction
    #Makes Mario "die" if hit by bullet, will also keep track of elimenated Mario
    for i in range(len(mario_L)):
            mario_L[i].pos += mario_L[i].vel*dt
            
            mario_counter = mario_counter + mario_collide(mario_L[i],mario_counter)
            
 
    ball.pos = ball.pos + ball.vel*dt      # Update the ball's position
    
    bullet.vel = vec(0, 0, -10)
    bullet.pos += bullet.vel*bulletdt
    for i in range(len(second_block)):
        row2_collide(second_block[i])
        second_block[i].pos += second_block[i].vel*dt
    
    #checks to see if the player has reached the end of the game
    #Will output the total time the player has played the game!
    
    if ball.pos.z - wallD.pos.z < 35 :
        t2 = clock()
        print("Congratulations! You finished the game!")
        print("Total Time: " + str(t2-t1) + " seconds!")
        print("Number of shrooms infected: " + shroom_counter)
        print("Number of Marios destroyed: " + mario_counter)
        break
    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!
    # +++ Start of COLLISIONS -- check for collisions & do the "right" thing
    corral_collide(ball)
    bullet_collide(bullet)
    for i in range(len(spaceship_L)):
        space_collide(spaceship_L[i])
        spaceship_L[i].pos = spaceship_L[i].pos + spaceship_L[i].vel*spacedt
        
    for shroom in shrooms_list:
        if mag( ball.pos - shroom.pos ) < 0.8:
            shroom.color = vector(0.5,0,5,0.5)
            shroom.pos = vector(shroom.pos.x,3.5,shroom.pos.z)
            shroom_counter= shroom_counter + 1 
            print("Number of shrooms infected: " + shroom_counter)
    
    # If the alien ventures too far, restart randomly -- but only if it's
    # not moving vertically.
   
    # +++ End of COLLISIONS
# +++ start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...
def keydown_fun(event):
    """This function is called each time a key is pressed."""
    ball.color = randcolor()
    key = event.key
    ri = randint(0, 10)
    #print("key:", key, ri)  # Prints the key pressed -- caps only...
    amt = 1           # "Strength" of the keypress's velocity changes
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
    elif key in 'rR':
        ball.vel = vector(0, 0, 0) # Reset! via the spacebar, " "
        ball.pos = vector(0, 0, 0)
    elif key in ' ':
        bullet.visible = True
# +++ End of EVENT_HANDLING section
# +++ Other functions can go here...
def choice(L):
    """Implements Python's using the random() function."""
    LEN = len(L)              # Get the length
    randomindex = int(LEN*random())  # Get a random index
    return L[randomindex]     # Return that element
def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low        # Swap if out of order!
    LEN = int(hi) - int(low) + 1 # Get the span and add 1
    randvalue = LEN*random()     # Get a random value
    return int(randvalue)        # Return the integer part of it
def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    red = vector(1.000, 0.000, 0.000)
    orange = vector(1.000, 0.309, 0.000)
    yellow = vector(1.000, 1.000, 0.000)
    green = vector(0.000, 1.000, 0.000)
    blue = vector(0.000, 0.000, 1.000)
    violet = vector(1.000, 0.000, 1.000)
    randcolor = choice([red, orange, yellow, green, blue, violet])
    return randcolor   # A color is a three-element vector
def corral_collide(ball):
    """Corral collisions!
       Ball must have a .vel field and a .pos field.
    """
    change_color = randcolor()
    first_block = [alien_row1, alien_row2, alien_row4, alien_row5, alien_row7, alien_row8, alien_row9, alien_row10, alien_row11, alien_row12]
    second_block = [block2_1, block2_2, block3_3, block4_4]
    black_holes = [black_hole1, black_hole2,black_hole3]
    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x + 1:  # Hit -- check for x
        ball.pos.x = wallB.pos.x + 1  # Bring back into bounds
        ball.vel.x *= -1.0    
        wallB.color = change_color # Reverse the x velocity
        wallC.color = change_color
        wallD.color = change_color
    if ball.pos.x > wallC.pos.x - 1:
        ball.pos.x = wallC.pos.x - 1
        ball.vel.x *= -1.0
        wallC.color = change_color
        wallB.color = change_color
        wallD.color = change_color
    if ball.pos.z < wallD.pos.z:
        ball.pos.z = wallD.pos.z
        ball.vel.z *= -1.0
        wallD.color = change_color
        wallB.color = change_color
        wallC.color = change_color
    if ball.pos.z > 0:
        ball.pos.z = 0
        ball.vel.z *= -1.0
    for i in range(len(black_holes)):
        if mag(ball.pos - black_holes[i].pos) < 1.0:
            ball.pos = vec(0,0,0)
    
    # For the blocks.
    for i in range(len(first_block)):
        if ball.pos.z < first_block[i].pos.z + 0.75 and ball.pos.z > first_block[i].pos.z - 0.75 and ball.pos.x > first_block[i].pos.x - 10 and ball.pos.x < first_block[i].pos.x + 10:
            ball.pos.z = ball.pos.z
            ball.pos.x = ball.pos.x
            ball.vel.z *= -1.0
            ball.vel.x *= -1.0
    for i in range(len(second_block)):
        if ball.pos.z < second_block[i].pos.z + 0.75 and ball.pos.z > second_block[i].pos.z - 0.75 and ball.pos.x > second_block[i].pos.x + 3 and ball.pos.x < second_block[i].pos.x + 18:
            ball.pos.z = ball.pos.z
            ball.pos.z = ball.pos.z
            ball.pos.x = ball.pos.x
            ball.vel.z *= -1.0
            ball.vel.x *= -1.0
        if ball.pos.z < second_block[i].pos.z + 0.75 and ball.pos.z > second_block[i].pos.z - 0.75 and ball.pos.x < second_block[i].pos.x - 3 and ball.pos.x > second_block[i].pos.x - 16:
            ball.pos.z = ball.pos.z
            ball.pos.z = ball.pos.z
            ball.pos.x = ball.pos.x
            ball.vel.z *= -1.0
            ball.vel.x *= -1.0
    for i in range(len(mario_L)):
        if mario_L[i].visible:
            if mag(ball.pos - mario_L[i].pos) < 3:
                ball.vel = vector(0, 0, 0) # Reset! via the spacebar, " "
                ball.pos = vector(0, 0, 0)
        
                
                
        
        
        
def alien_collide(ball):
    """Corral collisions!
       Ball must have a .vel field and a .pos field.
    """
    change_color = randcolor()
 
    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x + 10:  # Hit -- check for x
        ball.pos.x = wallB.pos.x + 10  # Bring back into bounds
        ball.vel.x *= -1.0    
    if ball.pos.x > wallC.pos.x - 10:
        ball.pos.x = wallC.pos.x - 10
        ball.vel.x *= -1.0
    if ball.pos.z < wallD.pos.z:
        ball.pos.z = wallD.pos.z
        ball.vel.z *= -1.0
def row2_collide(ball):
    """
    dictates the inelastic collision that will occur if the ball hits one of the moving rows
    """
    change_color = randcolor()
 
    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x + 16:  # Hit -- check for x
        ball.pos.x = wallB.pos.x + 16  # Bring back into bounds
        ball.vel.x *= -1.0    
    if ball.pos.x > wallC.pos.x - 16:
        ball.pos.x = wallC.pos.x - 16
        ball.vel.x *= -1.0
    
def space_collide(ball):
    """Separate collision function for the spaceship.
    """
    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x + 5:  # Hit -- check for x
        ball.pos.x = wallB.pos.x + 5  # Bring back into bounds
        ball.vel.x *= -1.0        # Reverse the x velocity
    if ball.pos.x > wallC.pos.x - 5:
        ball.pos.x = wallC.pos.x - 5
        ball.vel.x *= -1.0
    
    
    if ball.pos.y > 20:
        ball.pos.y = 20
        ball.vel.y *= -1.0
    
    if ball.pos.y < 6:
        ball.pos.y = 6
        ball.vel.y *= -1.0
    if ball.pos.z < wallD.pos.z:
        ball.pos.z = wallD.pos.z
        ball.vel.z *= -1
        
        
        
    
def mario_collide(mario,mario_counter):
    """Makes the Mario characters oscillate back and forth between the two wall barriers. Also creates a "counter" argument everytime a Mario is destroyed
    """
        # If the ball hits wallB
    if mario.pos.x < wallB.pos.x + 2:  # Hit -- check for x
        mario.pos.x = wallB.pos.x + 2 # Bring back into bounds
        mario.vel.x *= -1.0     
        mario.vel.z *= -1.0 
        # Reverse the x velocity
    if mario.pos.x > wallC.pos.x - 2:
        mario.pos.x = wallC.pos.x - 2
        mario.vel.x *= -1.0
        mario.vel.z *= 1
    for i in range(len(alien_L)):
        if mario.pos.z < alien_L[i].pos.z + 0.75 and mario.pos.z > alien_L[i].pos.z - 0.75:
            mario.vel.z *= -1.0
    for i in range(len(mario_L)):
        if bullet.visible:
            if mag(bullet.pos - mario_L[i].pos) < 3:
                mario_L[i].pos.y = 100
                """mario_counter= mario_counter + 1
                print("Number of Marios destroyed is: " + mario_counter)
                """
                print('Marios destroyed: ' + (mario_counter+1))
                return 1
    return 0
                
            
            
                
    
def bullet_collide(bullet):
    """
    Dictates collision between the bullets and the moving obstacles
    """
    if bullet.pos.x < wallB.pos.x:
        bullet.visible = False
        bullet.pos = ball.pos
    if bullet.pos.x > wallC.pos.x:
        bullet.pos = ball.pos
        bullet.visible = False
    if bullet.pos.y > 20:
        bullet.pos = ball.pos
        bullet.visible = False
    if mag(bullet.pos - ball.pos) > 15:
        bullet.pos = ball.pos
        bullet.visible = False
        
        
        
def star_maker():
    """Generates random stars."""
    for x in range(1000): 
        points(pos = vector(choice(list(range(-30, 30))), choice(list(range(-10, 10))), 
        choice(list(range(-1000, 40)))), radius=2, color=vector(1.000, 0.996, 0.904))
 
    
