import random 

# Array of all color faces on the megaminx
colors = [['white'], ['blue'], ['red'], ['green'], ['purple'], ['yellow'], ['light blue'], ['light yellow'], ['pink'], ['lime green'], ['orange'], ['grey']]

# Array of all of the spots on the megaminx and the color that is in that spot
megaminx_origional = [[[[0, 0], ['white']], [[0, 1], ['white']], [[0, 2], ['white']], [[0, 3], ['white']], [[0, 4], ['white']], [[0, 5], ['white']], [[0, 6], ['white']], [[0, 7], ['white']], [[0, 8], ['white']], [[0, 9], ['white']]], 
            [[[1, 0], ['blue']], [[1, 1], ['blue']], [[1, 2], ['blue']], [[1, 3], ['blue']], [[1, 4], ['blue']], [[1, 5], ['blue']], [[1, 6], ['blue']], [[1, 7], ['blue']], [[1, 8], ['blue']], [[1, 9], ['blue']]],
            [[[2, 0], ['red']], [[2, 1], ['red']], [[2, 2], ['red']], [[2, 3], ['red']], [[2, 4], ['red']], [[2, 5], ['red']], [[2, 6], ['red']], [[2, 7], ['red']], [[2, 8], ['red']], [[2, 9], ['red']]],
            [[[3, 0], ['green']], [[3, 1], ['green']], [[3, 2], ['green']], [[3, 3], ['green']], [[3, 4], ['green']], [[3, 5], ['green']], [[3, 6], ['green']], [[3, 7], ['green']], [[3, 8], ['green']], [[3, 9], ['green']]],
            [[[4, 0], ['purple']], [[4, 1], ['purple']], [[4, 2], ['purple']], [[4, 3], ['purple']], [[4, 4], ['purple']], [[4, 5], ['purple']], [[4, 6], ['purple']], [[4, 7], ['purple']], [[4, 8], ['purple']], [[4, 9], ['purple']]],
            [[[5, 0], ['yellow']], [[5, 1], ['yellow']], [[5, 2], ['yellow']], [[5, 3], ['yellow']], [[5, 4], ['yellow']], [[5, 5], ['yellow']], [[5, 6], ['yellow']], [[5, 7], ['yellow']], [[5, 8], ['yellow']], [[5, 9], ['yellow']]],
            [[[6, 0], ['light blue']], [[6, 1], ['light blue']], [[6, 2], ['light blue']], [[6, 3], ['light blue']], [[6, 4], ['light blue']], [[6, 5], ['light blue']], [[6, 6], ['light blue']], [[6, 7], ['light blue']], [[6, 8], ['light blue']], [[6, 9], ['light blue']]],
            [[[7, 0], ['light yellow']], [[7, 1], ['light yellow']], [[7, 2], ['light yellow']], [[7, 3], ['light yellow']], [[7, 4], ['light yellow']], [[7, 5], ['light yellow']], [[7, 6], ['light yellow']], [[7, 7], ['light yellow']], [[7, 8], ['light yellow']], [[7, 9], ['light yellow']]],
            [[[8, 0], ['pink']], [[8, 1], ['pink']], [[8, 2], ['pink']], [[8, 3], ['pink']], [[8, 4], ['pink']], [[8, 5], ['pink']], [[8, 6], ['pink']], [[8, 7], ['pink']], [[8, 8], ['pink']], [[8, 9], ['pink']]],
            [[[9, 0], ['lime green']], [[9, 1], ['lime green']], [[9, 2], ['lime green']], [[9, 3], ['lime green']], [[9, 4], ['lime green']], [[9, 5], ['lime green']], [[9, 6], ['lime green']], [[9, 7], ['lime green']], [[9, 8], ['lime green']], [[9, 9], ['lime green']]],
            [[[10, 0], ['orange']], [[10, 1], ['orange']], [[10, 2], ['orange']], [[10, 3], ['orange']], [[10, 4], ['orange']], [[10, 5], ['orange']], [[10, 6], ['orange']], [[10, 7], ['orange']], [[10, 8], ['orange']], [[10, 9], ['orange']]],
            [[[11, 0], ['grey']], [[11, 1], ['grey']], [[11, 2], ['grey']], [[11, 3], ['grey']], [[11, 4], ['grey']], [[11, 5], ['grey']], [[11, 6], ['grey']], [[11, 7], ['grey']], [[11, 8], ['grey']], [[11, 9], ['grey']]],
            ]

megaminx = [[[[0, 0], ['white']], [[0, 1], ['white']], [[0, 2], ['white']], [[0, 3], ['white']], [[0, 4], ['white']], [[0, 5], ['white']], [[0, 6], ['white']], [[0, 7], ['white']], [[0, 8], ['white']], [[0, 9], ['white']]], 
            [[[1, 0], ['blue']], [[1, 1], ['blue']], [[1, 2], ['blue']], [[1, 3], ['blue']], [[1, 4], ['blue']], [[1, 5], ['blue']], [[1, 6], ['blue']], [[1, 7], ['blue']], [[1, 8], ['blue']], [[1, 9], ['blue']]],
            [[[2, 0], ['red']], [[2, 1], ['red']], [[2, 2], ['red']], [[2, 3], ['red']], [[2, 4], ['red']], [[2, 5], ['red']], [[2, 6], ['red']], [[2, 7], ['red']], [[2, 8], ['red']], [[2, 9], ['red']]],
            [[[3, 0], ['green']], [[3, 1], ['green']], [[3, 2], ['green']], [[3, 3], ['green']], [[3, 4], ['green']], [[3, 5], ['green']], [[3, 6], ['green']], [[3, 7], ['green']], [[3, 8], ['green']], [[3, 9], ['green']]],
            [[[4, 0], ['purple']], [[4, 1], ['purple']], [[4, 2], ['purple']], [[4, 3], ['purple']], [[4, 4], ['purple']], [[4, 5], ['purple']], [[4, 6], ['purple']], [[4, 7], ['purple']], [[4, 8], ['purple']], [[4, 9], ['purple']]],
            [[[5, 0], ['yellow']], [[5, 1], ['yellow']], [[5, 2], ['yellow']], [[5, 3], ['yellow']], [[5, 4], ['yellow']], [[5, 5], ['yellow']], [[5, 6], ['yellow']], [[5, 7], ['yellow']], [[5, 8], ['yellow']], [[5, 9], ['yellow']]],
            [[[6, 0], ['light blue']], [[6, 1], ['light blue']], [[6, 2], ['light blue']], [[6, 3], ['light blue']], [[6, 4], ['light blue']], [[6, 5], ['light blue']], [[6, 6], ['light blue']], [[6, 7], ['light blue']], [[6, 8], ['light blue']], [[6, 9], ['light blue']]],
            [[[7, 0], ['light yellow']], [[7, 1], ['light yellow']], [[7, 2], ['light yellow']], [[7, 3], ['light yellow']], [[7, 4], ['light yellow']], [[7, 5], ['light yellow']], [[7, 6], ['light yellow']], [[7, 7], ['light yellow']], [[7, 8], ['light yellow']], [[7, 9], ['light yellow']]],
            [[[8, 0], ['pink']], [[8, 1], ['pink']], [[8, 2], ['pink']], [[8, 3], ['pink']], [[8, 4], ['pink']], [[8, 5], ['pink']], [[8, 6], ['pink']], [[8, 7], ['pink']], [[8, 8], ['pink']], [[8, 9], ['pink']]],
            [[[9, 0], ['lime green']], [[9, 1], ['lime green']], [[9, 2], ['lime green']], [[9, 3], ['lime green']], [[9, 4], ['lime green']], [[9, 5], ['lime green']], [[9, 6], ['lime green']], [[9, 7], ['lime green']], [[9, 8], ['lime green']], [[9, 9], ['lime green']]],
            [[[10, 0], ['orange']], [[10, 1], ['orange']], [[10, 2], ['orange']], [[10, 3], ['orange']], [[10, 4], ['orange']], [[10, 5], ['orange']], [[10, 6], ['orange']], [[10, 7], ['orange']], [[10, 8], ['orange']], [[10, 9], ['orange']]],
            [[[11, 0], ['grey']], [[11, 1], ['grey']], [[11, 2], ['grey']], [[11, 3], ['grey']], [[11, 4], ['grey']], [[11, 5], ['grey']], [[11, 6], ['grey']], [[11, 7], ['grey']], [[11, 8], ['grey']], [[11, 9], ['grey']]],
            ]

# Print out the megaminx
def display_face(row):
    print('            _________________________________')
    print('           /           /         \\           \\') 
    print('          /', megaminx[row][0][1], '/', megaminx[row][1][1], '\\', megaminx[row][2][1], '\\')
    print('         /           /             \\           \\') 
    print('        /___________/_______________\\___________\\') 
    print('       /           /                 \\           \\') 
    print('      /\\', megaminx[row][9][1], '/                   \\', megaminx[row][3][1], '/\\') 
    print('     /  \        /                     \\        /  \\') 
    print('    /    \      /                       \\      /    \\') 
    print('   /      \    /                         \\    /      \\') 
    print('  /        \  /                           \\  /        \\') 
    print(' /          \/                             \\/          \\') 
    print(' \\', megaminx[row][8][1], '/\\        ', colors[row], '         /\\', megaminx[row][4][1], '/') 
    print('  \\        /  \\                           /  \\        /') 
    print('   \\      /    \\                         /    \\      /') 
    print('    \\    /      \\                       /      \\    /') 
    print('     \\  /        \\                     /        \\  /') 
    print('      \\/          \\                   /          \\/') 
    print('       \\           \\                 /           /') 
    print('        \\           \\               /           /') 
    print('         \\           \\             /           /') 
    print('          \\           \\           /           /') 
    print('           \\', megaminx[row][7][1], '\\         /', megaminx[row][5][1], '/') 
    print('            \\           \\       /           /') 
    print('             \\           \\     /           /') 
    print('              \\           \\   /           /') 
    print('               \\           \\ /           /') 
    print('                \\          / \\          /') 
    print('                 \\        /   \\        /') 
    print('                  \\      /     \\      /') 
    print('                   \\    /       \\    /') 
    print('                    \\  /         \\  /') 
    print('                     \\/           \\/') 
    print('                      \\', megaminx[row][6][1], '/') 
    print('                       \\         /') 
    print('                        \\       /') 
    print('                         \\     /') 
    print('                          \\   /') 
    print('                           \\ / \n') 

# Displays the number of incorrect cubbies
def display_number_incorrect():
    row = 0
    cubbie = 0
    correct = 0
    incorrect = 0
    for i in megaminx:
        for j in megaminx[0]:
            if megaminx[row][cubbie][1] == megaminx_origional[row][cubbie][1]:
                correct += 1
            else:
                # Print out the cubbies color on the megaminx followed by its correct color
                # print(megaminx[row][cubbie])
                # print(megaminx_origional[row][cubbie])
                if megaminx[row][cubbie][1] == ['']:
                    print(megaminx[row][cubbie])
            cubbie += 1
        cubbie = 0
        row += 1
    incorrect = 120 - correct
    print('Number of cubbies incorrect\n', incorrect)

# Updates the cubbies on the face being rotated clockwise
def rotate_face_clockwise(face):
    # Center pieces
    temp1 = megaminx[face][7][1]
    megaminx[face][7][1] = megaminx[face][5][1]
    megaminx[face][5][1] = megaminx[face][3][1]
    megaminx[face][3][1] = megaminx[face][1][1]
    megaminx[face][1][1] = megaminx[face][9][1]
    megaminx[face][9][1] = temp1
    # Corner pieces
    temp2 = megaminx[face][4][1]
    megaminx[face][4][1] = megaminx[face][2][1]
    megaminx[face][2][1] = megaminx[face][0][1]
    megaminx[face][0][1] = megaminx[face][8][1]
    megaminx[face][8][1] = megaminx[face][6][1]
    megaminx[face][6][1] = temp2

# Updates the cubbies on the face being rotated counterclockwise
def rotate_face_counterclockwise(face):
    # Center pieces
    temp1 = megaminx[face][9][1]
    megaminx[face][9][1] = megaminx[face][1][1]
    megaminx[face][1][1] = megaminx[face][3][1]
    megaminx[face][3][1] = megaminx[face][5][1]
    megaminx[face][5][1] = megaminx[face][7][1]
    megaminx[face][7][1] = temp1
    # Corner pieces
    temp2 = megaminx[face][6][1]
    megaminx[face][6][1] = megaminx[face][8][1]
    megaminx[face][8][1] = megaminx[face][0][1]
    megaminx[face][0][1] = megaminx[face][2][1]
    megaminx[face][2][1] = megaminx[face][4][1]
    megaminx[face][4][1] = temp2

# Clockwise rotation
def rotate_clockwise(face):
    # Temporary place holders for cubbies that get changed before updating other cubbies
    temp1 = ['']
    temp2 = ['']
    temp3 = ['']

    # Rotate white face
    if face == 0:
        # Modify white face
        rotate_face_clockwise(face)

        # Modify blue face
        # Store values of blue face in temperary values
        temp1 = megaminx[1][0][1]
        temp2 = megaminx[1][1][1]
        temp3 = megaminx[1][2][1]
        megaminx[1][0][1] = megaminx[5][0][1]
        megaminx[1][1][1] = megaminx[5][1][1]
        megaminx[1][2][1] = megaminx[5][2][1]
        # Modify yellow face
        megaminx[5][0][1] = megaminx[4][0][1]
        megaminx[5][1][1] = megaminx[4][1][1]
        megaminx[5][2][1] = megaminx[4][2][1]
        # Modify purple face
        megaminx[4][0][1] = megaminx[3][0][1]
        megaminx[4][1][1] = megaminx[3][1][1]
        megaminx[4][2][1] = megaminx[3][2][1]
        # Modify green face
        megaminx[3][0][1] = megaminx[2][0][1]
        megaminx[3][1][1] = megaminx[2][1][1]
        megaminx[3][2][1] = megaminx[2][2][1]
        # Modify red face
        megaminx[2][0][1] = temp1
        megaminx[2][1][1] = temp2
        megaminx[2][2][1] = temp3

    # Rotate blue face
    elif face == 1:
        # Modify blue face
        rotate_face_clockwise(face)

        # Store values of yellow face in temperary values
        temp1 = megaminx[5][8][1]
        temp2 = megaminx[5][9][1]
        temp3 = megaminx[5][0][1]
        # Modify yellow face
        megaminx[5][8][1] = megaminx[0][0][1]
        megaminx[5][9][1] = megaminx[0][1][1]
        megaminx[5][0][1] = megaminx[0][2][1]
        # Modify white face
        megaminx[0][0][1] = megaminx[2][2][1]
        megaminx[0][1][1] = megaminx[2][3][1]
        megaminx[0][2][1] = megaminx[2][4][1]
        # Modify red face
        megaminx[2][2][1] = megaminx[8][6][1]
        megaminx[2][3][1] = megaminx[8][7][1]
        megaminx[2][4][1] = megaminx[8][8][1]
        # Modify pink face
        megaminx[8][6][1] = megaminx[9][4][1]
        megaminx[8][7][1] = megaminx[9][5][1]
        megaminx[8][8][1] = megaminx[9][6][1]
        # Modify lime green face
        megaminx[9][4][1] = temp1
        megaminx[9][5][1] = temp2
        megaminx[9][6][1] = temp3

    # Rotate red face
    elif face == 2:
        # Modify red face
        rotate_face_clockwise(face)

        # Store values of light yellow face in temperary values
        temp1 = megaminx[7][6][1]
        temp2 = megaminx[7][7][1]
        temp3 = megaminx[7][8][1]
        # Modify blue face
        megaminx[1][8][1] = megaminx[0][2][1]
        megaminx[1][9][1] = megaminx[0][3][1]
        megaminx[1][0][1] = megaminx[0][4][1]
        # Modify white face
        megaminx[0][2][1] = megaminx[3][2][1]
        megaminx[0][3][1] = megaminx[3][3][1]
        megaminx[0][4][1] = megaminx[3][4][1]
        # Modify green face
        megaminx[3][2][1] = megaminx[7][6][1]
        megaminx[3][3][1] = megaminx[7][7][1]
        megaminx[3][4][1] = megaminx[7][8][1]
        # Modify light yellow face
        megaminx[7][6][1] = megaminx[8][4][1]
        megaminx[7][7][1] = megaminx[8][5][1]
        megaminx[7][8][1] = megaminx[8][6][1]
        # Modify pink face
        megaminx[8][4][1] = temp1
        megaminx[8][5][1] = temp2
        megaminx[8][6][1] = temp3

    # Rotate green face
    elif face == 3:
        # Modify green face
        rotate_face_clockwise(face)

        # Store values of white face in temperary values
        temp1 = megaminx[0][4][1]
        temp2 = megaminx[0][5][1]
        temp3 = megaminx[0][6][1]
        # Modify white face
        megaminx[0][4][1] = megaminx[4][2][1]
        megaminx[0][5][1] = megaminx[4][3][1]
        megaminx[0][6][1] = megaminx[4][4][1]
        # Modify purple face
        megaminx[4][2][1] = megaminx[6][6][1]
        megaminx[4][3][1] = megaminx[6][7][1]
        megaminx[4][4][1] = megaminx[6][8][1]
        # Modify light blue face
        megaminx[6][6][1] = megaminx[7][4][1]
        megaminx[6][7][1] = megaminx[7][5][1]
        megaminx[6][8][1] = megaminx[7][6][1]
        # Modify light yellow face
        megaminx[7][4][1] = megaminx[2][8][1]
        megaminx[7][5][1] = megaminx[2][9][1]
        megaminx[7][6][1] = megaminx[2][0][1]
        # Modify red face
        megaminx[2][8][1] = temp1
        megaminx[2][9][1] = temp2
        megaminx[2][0][1] = temp3

    # # Rotate purple face
    elif face == 4:
        # Modify purple face
        rotate_face_clockwise(face)

        # Store values of white face in temperary values
        temp1 = megaminx[10][6][1]
        temp2 = megaminx[10][7][1]
        temp3 = megaminx[10][8][1]
        # Modify orange face
        megaminx[10][6][1] = megaminx[6][4][1]
        megaminx[10][7][1] = megaminx[6][5][1]
        megaminx[10][8][1] = megaminx[6][6][1]
        # Modify light blue face
        megaminx[6][4][1] = megaminx[3][8][1]
        megaminx[6][5][1] = megaminx[3][9][1]
        megaminx[6][6][1] = megaminx[3][0][1]
        # Modify green face
        megaminx[3][8][1] = megaminx[0][6][1]
        megaminx[3][9][1] = megaminx[0][7][1]
        megaminx[3][0][1] = megaminx[0][8][1]
        # Modify white face
        megaminx[0][6][1] = megaminx[5][2][1]
        megaminx[0][7][1] = megaminx[5][3][1]
        megaminx[0][8][1] = megaminx[5][4][1]
        # Modify yellow face
        megaminx[5][2][1] = temp1
        megaminx[5][3][1] = temp2
        megaminx[5][4][1] = temp3

    # # Rotate yellow face
    elif face == 5:
        # Modify yellow face
        rotate_face_clockwise(face)

        # Store values of white face in temperary values
        temp1 = megaminx[0][8][1]
        temp2 = megaminx[0][9][1]
        temp3 = megaminx[0][0][1]
        # Modify white face
        megaminx[0][8][1] = megaminx[1][2][1]
        megaminx[0][9][1] = megaminx[1][3][1]
        megaminx[0][0][1] = megaminx[1][4][1]
        # Modify blue face
        megaminx[1][2][1] = megaminx[9][6][1]
        megaminx[1][3][1] = megaminx[9][7][1]
        megaminx[1][4][1] = megaminx[9][8][1]
        # Modify lime green face
        megaminx[9][6][1] = megaminx[10][4][1]
        megaminx[9][7][1] = megaminx[10][5][1]
        megaminx[9][8][1] = megaminx[10][6][1]
        # Modify orange face
        megaminx[10][4][1] = megaminx[4][8][1]
        megaminx[10][5][1] = megaminx[4][9][1]
        megaminx[10][6][1] = megaminx[4][0][1]
        # Modify purple face
        megaminx[4][8][1] = temp1
        megaminx[4][9][1] = temp2
        megaminx[4][0][1] = temp3

    # Rotate light blue face
    elif face == 6:
        # Modify light blue face
        rotate_face_clockwise(face)

        # Store values of grey face in temperary values
        temp1 = megaminx[11][0][1]
        temp2 = megaminx[11][1][1]
        temp3 = megaminx[11][2][1]
        # Modify grey face
        megaminx[11][0][1] = megaminx[7][2][1]
        megaminx[11][1][1] = megaminx[7][3][1]
        megaminx[11][2][1] = megaminx[7][4][1]
        # Modify lime green face
        megaminx[7][2][1] = megaminx[3][6][1]
        megaminx[7][3][1] = megaminx[3][7][1]
        megaminx[7][4][1] = megaminx[3][8][1]
        # Modify green face
        megaminx[3][6][1] = megaminx[4][4][1]
        megaminx[3][7][1] = megaminx[4][5][1]
        megaminx[3][8][1] = megaminx[4][6][1]
        # Modify purple face
        megaminx[4][4][1] = megaminx[10][8][1]
        megaminx[4][5][1] = megaminx[10][9][1]
        megaminx[4][6][1] = megaminx[10][0][1]
        # Modify orange face
        megaminx[10][8][1] = temp1
        megaminx[10][9][1] = temp2
        megaminx[10][0][1] = temp3

    # Rotate light yellow face
    elif face == 7:
        # Modify light yellow face
        rotate_face_clockwise(face)

        # Store values of grey face in temperary values
        temp1 = megaminx[11][2][1]
        temp2 = megaminx[11][3][1]
        temp3 = megaminx[11][4][1]
        # Modify grey face
        megaminx[11][2][1] = megaminx[8][2][1]
        megaminx[11][3][1] = megaminx[8][3][1]
        megaminx[11][4][1] = megaminx[8][4][1]
        # Modify pink face
        megaminx[8][2][1] = megaminx[2][6][1]
        megaminx[8][3][1] = megaminx[2][7][1]
        megaminx[8][4][1] = megaminx[2][8][1]
        # Modify red face
        megaminx[2][6][1] = megaminx[3][4][1]
        megaminx[2][7][1] = megaminx[3][5][1]
        megaminx[2][8][1] = megaminx[3][6][1]
        # Modify green face
        megaminx[3][4][1] = megaminx[6][8][1]
        megaminx[3][5][1] = megaminx[6][9][1]
        megaminx[3][6][1] = megaminx[6][0][1]
        # Modify light blue face
        megaminx[6][8][1] = temp1
        megaminx[6][9][1] = temp2
        megaminx[6][0][1] = temp3

 # Rotate pink face
    elif face == 8:
        # Modify pink face
        rotate_face_clockwise(face)

        # Store values of grey face in temperary values
        temp1 = megaminx[11][4][1]
        temp2 = megaminx[11][5][1]
        temp3 = megaminx[11][6][1]
        # Modify grey face
        megaminx[11][4][1] = megaminx[9][2][1]
        megaminx[11][5][1] = megaminx[9][3][1]
        megaminx[11][6][1] = megaminx[9][4][1]
        # Modify lime green face
        megaminx[9][2][1] = megaminx[1][6][1]
        megaminx[9][3][1] = megaminx[1][7][1]
        megaminx[9][4][1] = megaminx[1][8][1]
        # Modify blue face
        megaminx[1][6][1] = megaminx[2][4][1]
        megaminx[1][7][1] = megaminx[2][5][1]
        megaminx[1][8][1] = megaminx[2][6][1]
        # Modify red face
        megaminx[2][4][1] = megaminx[7][8][1]
        megaminx[2][5][1] = megaminx[7][9][1]
        megaminx[2][6][1] = megaminx[7][0][1]
        # Modify light yellow face
        megaminx[7][8][1] = temp1
        megaminx[7][9][1] = temp2
        megaminx[7][0][1] = temp3

    # Rotate lime green face
    elif face == 9:
        # Modify lime green face
        rotate_face_clockwise(face)

        # Store values of grey face in temperary values
        temp1 = megaminx[11][6][1]
        temp2 = megaminx[11][7][1]
        temp3 = megaminx[11][8][1]
        # Modify grey face
        megaminx[11][6][1] = megaminx[10][2][1]
        megaminx[11][7][1] = megaminx[10][3][1]
        megaminx[11][8][1] = megaminx[10][4][1]
        # Modify orange face
        megaminx[10][2][1] = megaminx[5][6][1]
        megaminx[10][3][1] = megaminx[5][7][1]
        megaminx[10][4][1] = megaminx[5][8][1]
        # Modify yellow face
        megaminx[5][6][1] = megaminx[1][4][1]
        megaminx[5][7][1] = megaminx[1][5][1]
        megaminx[5][8][1] = megaminx[1][6][1]
        # Modify blue face
        megaminx[1][4][1] = megaminx[8][8][1]
        megaminx[1][5][1] = megaminx[8][9][1]
        megaminx[1][6][1] = megaminx[8][0][1]
        # Modify pink face
        megaminx[8][8][1] = temp1
        megaminx[8][9][1] = temp2
        megaminx[8][0][1] = temp3

    # Rotate orange face
    elif face == 10:
        # Modify orange face
        rotate_face_clockwise(face)

        # Store values of grey face in temperary values
        temp1 = megaminx[11][8][1]
        temp2 = megaminx[11][9][1]
        temp3 = megaminx[11][0][1]
        # Modify grey face
        megaminx[11][8][1] = megaminx[6][2][1]
        megaminx[11][9][1] = megaminx[6][3][1]
        megaminx[11][0][1] = megaminx[6][4][1]
        # Modify light blue face
        megaminx[6][2][1] = megaminx[4][6][1]
        megaminx[6][3][1] = megaminx[4][7][1]
        megaminx[6][4][1] = megaminx[4][8][1]
        # Modify purple face
        megaminx[4][6][1] = megaminx[5][4][1]
        megaminx[4][7][1] = megaminx[5][5][1]
        megaminx[4][8][1] = megaminx[5][6][1]
        # Modify yellow face
        megaminx[5][4][1] = megaminx[9][8][1]
        megaminx[5][5][1] = megaminx[9][9][1]
        megaminx[5][6][1] = megaminx[9][0][1]
        # Modify lime green face
        megaminx[9][8][1] = temp1
        megaminx[9][9][1] = temp2
        megaminx[9][0][1] = temp3

# Rotate grey face
    elif face == 11:
        # Modify grey face
        rotate_face_clockwise(face)

        # Store values of pink face in temperary values
        temp1 = megaminx[8][0][1]
        temp2 = megaminx[8][1][1]
        temp3 = megaminx[8][2][1]
        # Modify pink face
        megaminx[8][0][1] = megaminx[7][0][1]
        megaminx[8][1][1] = megaminx[7][1][1]
        megaminx[8][2][1] = megaminx[7][2][1]
        # Modify light yellow face
        megaminx[7][0][1] = megaminx[6][0][1]
        megaminx[7][1][1] = megaminx[6][1][1]
        megaminx[7][2][1] = megaminx[6][2][1]
        # Modify light blue face
        megaminx[6][0][1] = megaminx[10][0][1]
        megaminx[6][1][1] = megaminx[10][1][1]
        megaminx[6][2][1] = megaminx[10][2][1]
        # Modify orange face
        megaminx[10][0][1] = megaminx[9][0][1]
        megaminx[10][1][1] = megaminx[9][1][1]
        megaminx[10][2][1] = megaminx[9][2][1]
        # Modify lime green face
        megaminx[9][0][1] = temp1
        megaminx[9][1][1] = temp2
        megaminx[9][2][1] = temp3

    # print('Rotate,', face, 'clockwise \n')

# Clockwise rotation
def rotate_counterclockwise(face):
    # Temporary place holders for cubbies that get changed before updating other cubbies
    temp1 = ['']
    temp2 = ['']
    temp3 = ['']

    # Rotate white face
    if face == 0:
        # Modify white face
        rotate_face_counterclockwise(face)

        # Modify blue face
        # Store values of purple face in temperary values
        temp1 = megaminx[4][0][1]
        temp2 = megaminx[4][1][1]
        temp3 = megaminx[4][2][1]
        megaminx[4][0][1] = megaminx[5][0][1]
        megaminx[4][1][1] = megaminx[5][1][1]
        megaminx[4][2][1] = megaminx[5][2][1]
        # Modify yellow face
        megaminx[5][0][1] = megaminx[1][0][1]
        megaminx[5][1][1] = megaminx[1][1][1]
        megaminx[5][2][1] = megaminx[1][2][1]
        # Modify blue face
        megaminx[1][0][1] = megaminx[2][0][1]
        megaminx[1][1][1] = megaminx[2][1][1]
        megaminx[1][2][1] = megaminx[2][2][1]
        # Modify red face
        megaminx[2][0][1] = megaminx[3][0][1]
        megaminx[2][1][1] = megaminx[3][1][1]
        megaminx[2][2][1] = megaminx[3][2][1]
        # Modify green face
        megaminx[3][0][1] = temp1
        megaminx[3][1][1] = temp2
        megaminx[3][2][1] = temp3

    # Rotate blue face
    if face == 1:
        # Modify blue face
        rotate_face_counterclockwise(face)

        # Store values of red face in temperary values
        temp1 = megaminx[2][2][1]
        temp2 = megaminx[2][3][1]
        temp3 = megaminx[2][4][1]
        # Modify red face
        megaminx[2][2][1] = megaminx[0][0][1]
        megaminx[2][3][1] = megaminx[0][1][1]
        megaminx[2][4][1] = megaminx[0][2][1]
        # Modify white face
        megaminx[0][0][1] = megaminx[5][8][1]
        megaminx[0][1][1] = megaminx[5][9][1]
        megaminx[0][2][1] = megaminx[5][0][1]
        # Modify yellow face
        megaminx[5][8][1] = megaminx[9][4][1]
        megaminx[5][9][1] = megaminx[9][5][1]
        megaminx[5][0][1] = megaminx[9][6][1]
        # Modify lime green face
        megaminx[9][4][1] = megaminx[8][6][1]
        megaminx[9][5][1] = megaminx[8][7][1]
        megaminx[9][6][1] = megaminx[8][8][1]
        # Modify pink face
        megaminx[8][6][1] = temp1
        megaminx[8][7][1] = temp2
        megaminx[8][8][1] = temp3

    # Rotate red face
    if face == 2:
        # Modify red face
        rotate_face_counterclockwise(face)

        # Store values of light yellow face in temperary values
        temp1 = megaminx[3][2][1]
        temp2 = megaminx[3][3][1]
        temp3 = megaminx[3][4][1]
        # Modify green face
        megaminx[3][2][1] = megaminx[0][2][1]
        megaminx[3][3][1] = megaminx[0][3][1]
        megaminx[3][4][1] = megaminx[0][4][1]
        # Modify white face
        megaminx[0][2][1] = megaminx[1][8][1]
        megaminx[0][3][1] = megaminx[1][9][1]
        megaminx[0][4][1] = megaminx[1][0][1]
        # Modify blue face
        megaminx[1][8][1] = megaminx[8][4][1]
        megaminx[1][9][1] = megaminx[8][5][1]
        megaminx[1][0][1] = megaminx[8][6][1]
        # Modify pink face
        megaminx[8][4][1] = megaminx[7][6][1]
        megaminx[8][5][1] = megaminx[7][7][1]
        megaminx[8][6][1] = megaminx[7][8][1]
        # Modify light yellow face
        megaminx[7][6][1] = temp1
        megaminx[7][7][1] = temp2
        megaminx[7][8][1] = temp3

    # Rotate green face
    if face == 3:
        # Modify green face
        rotate_face_counterclockwise(face)

        # Store values of purple face in temperary values
        temp1 = megaminx[4][2][1]
        temp2 = megaminx[4][3][1]
        temp3 = megaminx[4][4][1]
        # Modify purple face
        megaminx[4][2][1] = megaminx[0][4][1]
        megaminx[4][3][1] = megaminx[0][5][1]
        megaminx[4][4][1] = megaminx[0][6][1]
        # Modify light blue face
        megaminx[6][6][1] = megaminx[4][2][1]
        megaminx[6][7][1] = megaminx[4][3][1]
        megaminx[6][8][1] = megaminx[4][4][1]
        # Modify light yellow face
        megaminx[7][4][1] = megaminx[6][6][1]
        megaminx[7][5][1] = megaminx[6][7][1]
        megaminx[7][6][1] = megaminx[6][8][1]
        # Modify red face
        megaminx[2][8][1] = megaminx[7][4][1]
        megaminx[2][9][1] = megaminx[7][5][1]
        megaminx[2][0][1] = megaminx[7][6][1]
        # Modify red face
        megaminx[7][4][1] = temp1
        megaminx[7][5][1] = temp2
        megaminx[7][6][1] = temp3

    # Rotate purple face
    if face == 4:
        # Modify purple face
        rotate_face_counterclockwise(face)

        # Store values of white face in temperary values
        temp1 = megaminx[6][4][1]
        temp2 = megaminx[6][5][1]
        temp3 = megaminx[6][6][1]
        # Modify white face
        megaminx[0][6][1] = megaminx[3][8][1]
        megaminx[0][7][1] = megaminx[3][9][1]
        megaminx[0][8][1] = megaminx[3][0][1]
        # Modify green face
        megaminx[3][8][1] = megaminx[6][4][1]
        megaminx[3][9][1] = megaminx[6][5][1]
        megaminx[3][0][1] = megaminx[6][6][1]
        # Modify light blue face
        megaminx[6][4][1] = megaminx[10][6][1]
        megaminx[6][5][1] = megaminx[10][7][1]
        megaminx[6][6][1] = megaminx[10][8][1]
        # Modify yellow face
        megaminx[10][6][1] = megaminx[5][2][1]
        megaminx[10][7][1] = megaminx[5][3][1]
        megaminx[10][8][1] = megaminx[5][4][1]
        # Modify yellow face
        megaminx[5][2][1] = temp1
        megaminx[5][3][1] = temp2
        megaminx[5][4][1] = temp3

    # Rotate yellow face
    if face == 5:
        # Modify yellow face
        rotate_face_counterclockwise(face)

        # Store values of white face in temperary values
        temp1 = megaminx[4][8][1]
        temp2 = megaminx[4][9][1]
        temp3 = megaminx[4][0][1]
        # Modify purple face
        megaminx[4][8][1] = megaminx[10][4][1]
        megaminx[4][9][1] = megaminx[10][5][1]
        megaminx[4][0][1] = megaminx[10][6][1]
        # Modify orange face
        megaminx[10][4][1] = megaminx[9][6][1] 
        megaminx[10][5][1] = megaminx[9][7][1] 
        megaminx[10][6][1] = megaminx[9][8][1] 
        # Modify lime green face
        megaminx[9][6][1] = megaminx[1][2][1] 
        megaminx[9][7][1] = megaminx[1][3][1] 
        megaminx[9][8][1] = megaminx[1][4][1] 
        # Modify white face
        megaminx[1][2][1] = megaminx[0][8][1] 
        megaminx[1][3][1] = megaminx[0][9][1] 
        megaminx[1][4][1] = megaminx[0][0][1] 
        # Modify purple face
        megaminx[0][8][1] = temp1
        megaminx[0][9][1] = temp2
        megaminx[0][0][1] = temp3

    # Rotate light blue face
    if face == 6:
        # Modify light blue face
        rotate_face_counterclockwise(face)

        # Store values of grey face in temperary values
        temp1 = megaminx[4][4][1]
        temp2 = megaminx[4][5][1]
        temp3 = megaminx[4][6][1]
        # Modify purple face
        megaminx[4][4][1] = megaminx[3][6][1] 
        megaminx[4][5][1] = megaminx[3][7][1] 
        megaminx[4][6][1] = megaminx[3][8][1] 
        # Modify green face
        megaminx[3][6][1] = megaminx[7][2][1] 
        megaminx[3][7][1] = megaminx[7][3][1] 
        megaminx[3][8][1] = megaminx[7][4][1] 
        # Modify lime green face
        megaminx[7][2][1] = megaminx[11][0][1]
        megaminx[7][3][1] = megaminx[11][1][1]
        megaminx[7][4][1] = megaminx[11][2][1]
        # Modify grey face
        megaminx[11][0][1] = megaminx[10][8][1]
        megaminx[11][1][1] = megaminx[10][9][1]
        megaminx[11][2][1] = megaminx[10][0][1]
        # Modify orange face
        megaminx[10][8][1] = temp1
        megaminx[10][9][1] = temp2
        megaminx[10][0][1] = temp3

    # Rotate light yellow face
    if face == 7:
        # Modify light yellow face
        rotate_face_counterclockwise(face)

        # Store values of light blue face in temperary values
        temp1 = megaminx[6][8][1]
        temp2 = megaminx[6][9][1]
        temp3 = megaminx[6][0][1]
        # Modify light blue face
        megaminx[6][8][1] = megaminx[3][4][1] 
        megaminx[6][9][1] = megaminx[3][5][1] 
        megaminx[6][0][1] = megaminx[3][6][1] 
        # Modify green face
        megaminx[3][4][1] = megaminx[2][6][1] 
        megaminx[3][5][1] = megaminx[2][7][1] 
        megaminx[3][6][1] = megaminx[2][8][1] 
        # Modify red face
        megaminx[2][6][1] = megaminx[8][2][1] 
        megaminx[2][7][1] = megaminx[8][3][1] 
        megaminx[2][8][1] = megaminx[8][4][1] 
        # Modify pink face
        megaminx[8][2][1] = megaminx[11][2][1]
        megaminx[8][3][1] = megaminx[11][3][1]
        megaminx[8][4][1] = megaminx[11][4][1]
        # Modify grey face
        megaminx[11][2][1] = temp1
        megaminx[11][3][1] = temp2
        megaminx[11][4][1] = temp3

 # Rotate pink face
    if face == 8:
        # Modify pink face
        rotate_face_counterclockwise(face)

        # Store values of lime green face in temperary values
        temp1 = megaminx[7][8][1]
        temp2 = megaminx[7][9][1]
        temp3 = megaminx[7][0][1]
        # Modify light yellow face
        megaminx[7][8][1] = megaminx[2][4][1] 
        megaminx[7][9][1] = megaminx[2][5][1] 
        megaminx[7][0][1] = megaminx[2][6][1] 
        # Modify red face
        megaminx[2][4][1] = megaminx[1][6][1] 
        megaminx[2][5][1] = megaminx[1][7][1] 
        megaminx[2][6][1] = megaminx[1][8][1] 
        # Modify blue face
        megaminx[1][6][1] = megaminx[9][2][1] 
        megaminx[1][7][1] = megaminx[9][3][1] 
        megaminx[1][8][1] = megaminx[9][4][1] 
        # Modify lime green face
        megaminx[9][2][1] = megaminx[11][4][1]
        megaminx[9][3][1] = megaminx[11][5][1]
        megaminx[9][4][1] = megaminx[11][6][1]
        # Modify grey face
        megaminx[11][4][1] = temp1
        megaminx[11][5][1] = temp2
        megaminx[11][6][1] = temp3

    # Rotate lime green face
    if face == 9:
        # Modify lime green face
        rotate_face_counterclockwise(face)

        # Store values of pink face in temperary values
        temp1 = megaminx[8][8][1]
        temp2 = megaminx[8][9][1]
        temp3 = megaminx[8][0][1]
        # Modify pink face
        megaminx[8][8][1] = megaminx[1][4][1] 
        megaminx[8][9][1] = megaminx[1][5][1] 
        megaminx[8][0][1] = megaminx[1][6][1] 
        # Modify blue face
        megaminx[1][4][1] = megaminx[5][6][1] 
        megaminx[1][5][1] = megaminx[5][7][1] 
        megaminx[1][6][1] = megaminx[5][8][1] 
        # Modify yellow face
        megaminx[5][6][1] = megaminx[10][2][1]
        megaminx[5][7][1] = megaminx[10][3][1]
        megaminx[5][8][1] = megaminx[10][4][1]
        # Modify orange face
        megaminx[10][2][1] = megaminx[11][6][1]
        megaminx[10][3][1] = megaminx[11][7][1]
        megaminx[10][4][1] = megaminx[11][8][1]
        # Modify grey face
        megaminx[11][6][1] = temp1
        megaminx[11][7][1] = temp2
        megaminx[11][8][1] = temp3

    # Rotate orange face
    if face == 10:
        # Modify orange face
        rotate_face_counterclockwise(face)

        # Store values of lime green face in temperary values
        temp1 = megaminx[9][8][1]
        temp2 = megaminx[9][9][1]
        temp3 = megaminx[9][0][1]
        # Modify lime green face
        megaminx[9][8][1] = megaminx[5][4][1] 
        megaminx[9][9][1] = megaminx[5][5][1] 
        megaminx[9][0][1] = megaminx[5][6][1] 
        # Modify yellow face
        megaminx[5][4][1] = megaminx[4][6][1] 
        megaminx[5][5][1] = megaminx[4][7][1] 
        megaminx[5][6][1] = megaminx[4][8][1] 
        # Modify purple face
        megaminx[4][6][1] = megaminx[6][2][1] 
        megaminx[4][7][1] = megaminx[6][3][1] 
        megaminx[4][8][1] = megaminx[6][4][1] 
        # Modify light blue face
        megaminx[6][2][1] = megaminx[11][8][1]
        megaminx[6][3][1] = megaminx[11][9][1]
        megaminx[6][4][1] = megaminx[11][0][1]
        # Modify grey face
        megaminx[11][8][1] = temp1
        megaminx[11][9][1] = temp2
        megaminx[11][0][1] = temp3

# Rotate grey face
    if face == 11:
        # Modify grey face
        rotate_face_counterclockwise(face)

        # Store values of ime green face in temperary values
        temp1 = megaminx[9][0][1]
        temp2 = megaminx[9][1][1]
        temp3 = megaminx[9][2][1]
        # Modify lime green face
        megaminx[9][0][1] = megaminx[10][0][1]
        megaminx[9][1][1] = megaminx[10][1][1]
        megaminx[9][2][1] = megaminx[10][2][1]
        # Modify orange face
        megaminx[10][0][1] = megaminx[6][0][1] 
        megaminx[10][1][1] = megaminx[6][1][1] 
        megaminx[10][2][1] = megaminx[6][2][1] 
        # Modify light blue face
        megaminx[6][0][1] = megaminx[7][0][1] 
        megaminx[6][1][1] = megaminx[7][1][1] 
        megaminx[6][2][1] = megaminx[7][2][1] 
        # Modify light yellow face
        megaminx[7][0][1] = megaminx[8][0][1] 
        megaminx[7][1][1] = megaminx[8][1][1] 
        megaminx[7][2][1] = megaminx[8][2][1] 
        # Modify pink face
        megaminx[8][0][1] = temp1
        megaminx[8][1][1] = temp2
        megaminx[8][2][1] = temp3

    # print('Rotate,', face, 'counterclockwise \n')


# Mixes up the megaminx however many times is specified
def randomize(rotations):
    rotation = 0
    while rotation < rotations:
        direction = random.randint(0,1)
        print('Rotation: ',rotation)
        if direction == 0:
            rotate_clockwise(random.randint(0,11))
        else:
            rotate_counterclockwise(random.randint(0,11))
        rotation += 1

def display_megaminx():
    # # Print out the megaminx
    face = 0
    for k in megaminx:
        display_face(face)
        face += 1

# ***** Main body of code *****
# Rotate random faces on the megaminx a random amount of times to the cubbie pattern
numberOfRatations = input('How many turns would you like the randomizer to make? ')
randomize(int(numberOfRatations))

# Print out the megaminx
display_megaminx()

# Checks how many cubbies are out of place on the megaminx
# display_number_incorrect()

input_face = input('Which face would you like to rotate and in which direction: \n'
             'white = 0, blue = 1, red = 2, green = 3, purple = 4, yellow = 5, light blue = 6, light yellow = 7, pink = 8, lime green = 9, orange = 10, grey = 11 \n')
input_direction = input('Which direction would you like to rotate? \n clockwise = 0, counterclockwise = 1 \n')
if int(input_direction) == 0:
    rotate_clockwise(int(input_face))
else:
    rotate_counterclockwise(int(input_face))

# display_megaminx()
display_megaminx()