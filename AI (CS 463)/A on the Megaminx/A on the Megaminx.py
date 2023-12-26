import random 
import math
from queue import PriorityQueue 


"""
Each face is designated by a unique color that is in the center since the center cannot rotate.
Cubies are represented as numbers from 0 to 9. Their position on a face are as follows:
            _________________________________
           /           /         \           \ 
          /     0     /     1     \      2    \
         /           /             \           \ 
        /___________/_______________\___________\ 
       /           /                 \           \ 
      /\    9     /                   \     3    /\ 
     /  \        /                     \        /  \ 
    /    \      /                       \      /    \ 
   /      \    /                         \    /      \ 
  /        \  /                           \  /        \ 
 /          \/                             \/          \ 
 \    8     /\         face color          /\    4     / 
  \        /  \                           /  \        / 
   \      /    \                         /    \      / 
    \    /      \                       /      \    / 
     \  /        \                     /        \  / 
      \/          \                   /          \/ 
       \           \                 /           / 
        \           \               /           / 
         \           \             /           / 
          \           \           /           / 
           \     7     \         /     5     / 
            \           \       /           / 
             \           \     /           / 
              \           \   /           / 
               \           \ /           / 
                \          / \          / 
                 \        /   \        / 
                  \      /     \      / 
                   \    /       \    / 
                    \  /         \  / 
                     \/           \/ 
                      \     6     / 
                       \         / 
                        \       / 
                         \     / 
                          \   / 
                           \ / 
"""

class Megaminx:  
    # Faces and their adjacent faces  
    # Tuple order dictates which cubies are adjacent to that face
    _colors = {'white':  ('blue',  'red',    'green',  'purple', 'yellow'),
               'blue':   ('white', 'yellow', 'lime',   'pink',   'red'),
               'red':    ('white', 'blue',   'pink',   'tan',    'green'),
               'green':  ('white', 'red',    'tan',    'cyan',   'purple'),
               'purple': ('white', 'green',  'cyan',   'orange', 'yellow'),
               'yellow': ('white', 'purple', 'orange', 'lime',   'blue'),
               'cyan':   ('grey',  'orange', 'purple', 'green',  'tan'),
               'tan':    ('grey',  'cyan',   'green',  'red',    'pink'),
               'pink':   ('grey',  'tan',    'red',    'blue',   'lime'),
               'lime':   ('grey',  'pink',   'blue',   'yellow', 'orange'),
               'orange': ('grey',  'lime',   'yellow', 'purple', 'cyan'),
               'grey':   ('cyan',  'tan',    'pink',   'lime',   'orange')}
    
    def __init__(self, state=None, parent=None, rotated_face=None):
        # Default to a solved megaminx
        self.state = state if state is not None else {color: [color] * 10 for color in self._colors}
        self.depth = parent.depth + 1 if parent is not None else 0
        self.rotated_face = rotated_face
        self.parent = parent

    def __lt__(self, megaminx):
        return

    def _get_edge_index(self, face, adjacent_face):
        # Get the starting cubie of an edge touching an adjacent face
        return self._colors[face].index(adjacent_face) * 2

    def _get_edge(self, face, index):
        # Get cubies along an edge
        return self.state[face][index:index + 3] if index < 8 else self.state[face][8:] + self.state[face][:1]

    def rotate(self, face, clockwise):
        # Rotate the input face
        index = 8 if clockwise else 2
        self.state[face] = self.state[face][index:] + self.state[face][:index]

        # Rotate each adjacent edge on each adjacent face
        indices = [self._get_edge_index(adjacent_face, face) for adjacent_face in self._colors[face]]
        edges = [self._get_edge(adjacent_face, edge_index) for adjacent_face, edge_index in zip(self._colors[face], indices)]
        index = 4 if clockwise else 1
        edges = edges[index:] + edges[:index]
        for adjacent_face, edge_index, edge in zip(self._colors[face], indices, edges):
            for i, color in enumerate(edge):
                self.state[adjacent_face][(edge_index + i) % len(self.state[adjacent_face])] = color

    def heuristic(self):
        # Calculates the huristic value used for A* by taking all of the pieces that are out of place and dividing them by 15 since there are exactly 15 pieces that move for each rotation
        return math.ceil(sum(len(list(color for color in face if color != original_color)) for original_color, face in self.state.items()) / 15)

    def display(self):
        for face, colors in self.state.items():
            print(f'            _________________________________')
            print(f'           /           /         \\           \\') 
            print(f'          / {colors[0]:^10}/{colors[1]:^11}\\{colors[2]:^11}\\')
            print(f'         /           /             \\           \\') 
            print(f'        /___________/_______________\\___________\\') 
            print(f'       /           /                 \\           \\') 
            print(f'      /\\{colors[9]:^10}/                   \\{colors[3]:^10}/\\') 
            print(f'     /  \        /                     \\        /  \\') 
            print(f'    /    \      /                       \\      /    \\') 
            print(f'   /      \    /                         \\    /      \\') 
            print(f'  /        \  /                           \\  /        \\') 
            print(f' /          \/                             \\/          \\') 
            print(f' \\{colors[8]:^10}/\\{face:^29}/\\{colors[4]:^10}/') 
            print(f'  \\        /  \\                           /  \\        /') 
            print(f'   \\      /    \\                         /    \\      /') 
            print(f'    \\    /      \\                       /      \\    /') 
            print(f'     \\  /        \\                     /        \\  /') 
            print(f'      \\/          \\                   /          \\/') 
            print(f'       \\           \\                 /           /') 
            print(f'        \\           \\               /           /') 
            print(f'         \\           \\             /           /') 
            print(f'          \\           \\           /           /') 
            print(f'           \\{colors[7]:^11}\\         /{colors[5]:^11}/') 
            print(f'            \\           \\       /           /') 
            print(f'             \\           \\     /           /') 
            print(f'              \\           \\   /           /') 
            print(f'               \\           \\ /           /') 
            print(f'                \\          / \\          /') 
            print(f'                 \\        /   \\        /') 
            print(f'                  \\      /     \\      /') 
            print(f'                   \\    /       \\    /') 
            print(f'                    \\  /         \\  /') 
            print(f'                     \\/           \\/') 
            print(f'                      \\{colors[6]:^11}/') 
            print(f'                       \\         /') 
            print(f'                        \\       /') 
            print(f'                         \\     /') 
            print(f'                          \\   /') 
            print(f'                           \\ / \n') 

    def randomize(self, k, clockwise=True):
        # Makes k number of clockwise rotations on random faces on megaminx
        rotations = [random.choice(list(self._colors)) for _ in range(k)]
        for color in rotations:
            self.rotate(color, clockwise)
        return rotations

    def clone(self, parent=None, rotated_face=None):
        # Make a deep copy of the current megaminx
        return Megaminx(
            state={color: face[:] for color, face in self.state.items()},
            parent=parent,
            rotated_face=rotated_face
        )

    def create_children(self, priority_queue):
        self.children = {color: self.clone(parent=self, rotated_face=color) for color in self._colors}
        for color, child in self.children.items():
            child.rotate(color, clockwise=False)
            priority_queue.put((child.heuristic() + child.depth, child))


def main():
    for k in range(3, 20):
        # Create 5 megaminx's for each number of rotations
        for i in range(5):
            print(f'Randomize rotations: {k}, Cube: {i}')
            # Initialize megaminx, priority queue, and variables
            root_megaminx = Megaminx()
            priority_queue = PriorityQueue()
            solution = []
            children_nodes_expanded = 0

            # Randomize the megaminx
            rotations = root_megaminx.randomize(k)

            priority_queue.put((0, root_megaminx))
            # Loop through the tree until a solution is found
            while not priority_queue.empty():
                weight, megaminx = priority_queue.get()
                # print(f'Exploring {megaminx.rotated_face} depth {megaminx.depth} weight {weight}')
                # Checks for solved state immediately before applying child function
                if megaminx.heuristic() == 0:
                    print('Megaminx is solved')
                    while megaminx.parent is not None:
                        solution.append(megaminx.rotated_face)
                        megaminx = megaminx.parent
                    break
                    
                # Make 12 deep copies of the megaminx and rotate a different face on each one
                megaminx.create_children(priority_queue)
                children_nodes_expanded += 1
            # Display output
            print(f'Solution from rotations:  {list(reversed(rotations))}')
            print(f'Solution from A*:         {list(reversed(solution))}')
            print(f'Number of nodes expanded: {children_nodes_expanded}')
            print(f'depth:                    {len(list(reversed(solution)))}\n')


if __name__ == '__main__':
    main()