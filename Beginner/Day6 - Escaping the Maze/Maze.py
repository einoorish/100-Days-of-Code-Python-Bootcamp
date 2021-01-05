def turn_right() :
    turn_left()
    turn_left()
    turn_left()
    
#The secret is to have Reeborg follow along the right edge 
#of the maze, turning right if it can, going straight ahead 
#if it can’t turn right, or turning left as a last resort. 
    
while not at_goal() :
    if right_is_clear() : 
        turn_right()
        move()
    elif front_is_clear() :
        move()
    else: turn_left()
