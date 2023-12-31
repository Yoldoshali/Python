def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        while front_is_clear():
            move()
    elif front_is_clear():
        move()
    elif wall_in_front() and not right_is_clear():
        turn_left()