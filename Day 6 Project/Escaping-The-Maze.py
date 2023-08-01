def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while not at_goal():
    if at_goal():
        pause()
    if front_is_clear():
        move()
    if wall_in_front() and wall_on_right():
        turn_left()
    if wall_in_front() and right_is_clear():
        turn_right()
        if not at_goal():
            move()
    if front_is_clear() and right_is_clear():
        if is_facing_north():
            move()
        turn_right()
        if not at_goal() and front_is_clear():
            move()
  
    

  
        
 
        

    
    
    


   
 
  
        
    
    
