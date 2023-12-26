import os
import random
import time

def get_file_path(directory):
    # Returns the file path of all files in the directory
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_paths.append(filepath)
    return file_paths

# Got this part from Michael Stacy which he said he got mostly from chatGPT
def open_file(filePath):
    clauses = []
    with open(filePath, 'r') as f:
        for newLine in f:
            # Grab the next line, then strip it into components
            newLine = newLine.strip()
            if newLine.startswith('c') or newLine.startswith('p') or newLine.startswith('%') or newLine.startswith('0'):
                continue
            # if newLine.startswith('p'):
            #     # Code written by Ryan Flores
            #     # Extract the number of variables and clauses in the file
            #     _, _, variableNumber, clauseNumber = newLine.split()
            #     continue
            # Skip empty lines
            if not newLine:
                continue

            # Convert the clauses to integers
            newClause = list(map(int, newLine.split()))

            # Add to our clauseHolder after removing the 0
            if newClause[-1] == 0:
                newClause = newClause[:-1]
            clauses.append(newClause)

    # Return our list of clauses
    # return clauses, int(variableNumber), int(clauseNumber)
    return clauses

def print_data(file):
    # Print data
    print(f'File: {file}')

#################### DPLL Algorithm ####################

def unit_propagation(unit_clause, clauses):
    clauses = [clause for clause in clauses if unit_clause[0] not in clause]
    return [[literal for literal in clause if literal != -unit_clause[0]] for clause in clauses]

def select_literal(clauses):
    # Selects the first leteral in the first clause
    return clauses[0][0]

def pure_literal_assign(clauses):
    # Get all literals in the clauses
    literalList = []
    for clause in clauses:
        for literal in clause:
            if literal not in literalList:
                literalList.append(literal)
    # print(literalList)

    # Check to see if the literals are pure literals
    pureLiterals = []
    for literal in literalList:
        if -literal not in literalList:
            pureLiterals.append(literal)
    return pureLiterals

def literal_propagation(pure_literal, clauses):
    return [clause for clause in clauses if pure_literal not in clause]

def dpll(clauses):
    # Unit Propogation
    unit_clauses = [clause for clause in clauses if len(clause) == 1]
    # Eliminate all unit_clauses using unit propagation
    while len(unit_clauses) > 0:
        clauses = unit_propagation(unit_clauses[0], clauses)
        unit_clauses = [clause for clause in clauses if len(clause) == 1]

    # Eliminate all clauses that have a pure literal   
    pure_literals = pure_literal_assign(clauses)

    # Remove clauses with pure literals from the assignment
    while len(pure_literals) > 0:
        clauses = literal_propagation(pure_literals[0], clauses)
        pure_literals = pure_literal_assign(clauses)

    # Stoping conditions
    # Formula is satisfiable only if there are no clauses
    # From wikipedia pseudocode
    if len(clauses) <= 0:
        return True 
    if any(len(clause) <= 0 for clause in clauses):
        return False

    # Get a literal from the clauses and make it a unit clause
    literal = select_literal(clauses)
    clauses2 = clauses.copy()
    clauses.append([literal])
    clauses2.append([-literal])

    return dpll(clauses) or dpll(clauses2)


#################### WalkSAT Algorithm ####################

def walksat_flip_random_variable(clauses, assignment, p):    
    if random.random() < p:
        # Flip a random literal
        variable = random.choice(range(len(assignment)))
        assignment[variable] = not assignment[variable]
    else:
        # Get all unsatisfied clauses
        unsatisfied_clauses = [clause for clause in clauses if not any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause)]
        # Pick a random unsatisfied clause and flip a variable to satisfy it
        literal = random.choice(random.choice(unsatisfied_clauses))
        assignment[abs(literal) - 1] = (literal > 0)

def number_of_true_clauses(assignment):
    number_true = 0
    for clause in assignment:
        if clause is True:
            number_true += 1
    return number_true

def find_best_assignment(best_assignment, assignment):
    if number_of_true_clauses(assignment) > number_of_true_clauses(best_assignment):
        return assignment
    else:
        return best_assignment

def walk_sat(clauses, p, max_flips):
    # Initialize a random assignemnt
    variables = max(abs(literal) for clause in clauses for literal in clause)
    assignment = [random.choice([True, False]) for _ in range(variables + 1)]

    # Initialize best assignment
    best_assignemnt = assignment

    # Check if the assignment is satisfiable and flips a random literal if it is not and check again
    for _ in range(max_flips):
        # If all clauses are satisfied by the assignment, return the assignment
        if all(any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause) for clause in clauses):
            satisfiable = 'Satisfiable Assignment'
            return assignment, satisfiable
        # Flip a random variable until a satisfiable assignment is found or max flips has been reached
        walksat_flip_random_variable(clauses, assignment, p)

        # Check if assignment is better.
        best_assignemnt = find_best_assignment(best_assignemnt, assignment)
    satisfiable = 'Not Satisfiable Assignment'
    return best_assignemnt, satisfiable


#################### gsat Algorithm ####################

def gsat_flip_random_variable(clauses, assignment):    
    # Get all unsatisfied clauses
    unsatisfied_clauses = [clause for clause in clauses if not any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause)]
    # Pick a random unsatisfied clause and flip a variable to satisfy it
    literal = random.choice(random.choice(unsatisfied_clauses))
    assignment[abs(literal) - 1] = (literal > 0)

def gsat(clauses, max_flips, max_steps):
    for _ in range(max_flips):
        # Randomly chosen assignment of the variables in the formula
        variables = max(abs(literal) for clause in clauses for literal in clause)
        assignment = [random.choice([True, False]) for _ in range(variables + 1)]
        best_assignemnt = assignment
        
        for _ in range(max_steps):
            # If all clauses are satisfied by the assignment, return the assignment
            if all(any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause) for clause in clauses):
                satisfiable = 'Satisfiable Assignment'
                return assignment, satisfiable
            # Flip a random variable until a satisfiable assignment is found or max flips has been reached
            gsat_flip_random_variable(clauses, assignment)
    
            # Check if assignment is better.
            best_assignemnt = find_best_assignment(best_assignemnt, assignment)
    satisfiable = 'Not Satisfiable Assignment'
    return best_assignemnt, satisfiable


def main():
    # files = get_file_path('./CNF Formulas')
    files = get_file_path('./HARD CNF Formulas')
    # with open("SAT_Output.txt", "w") as f:
    # with open("SAT_Hard_Output.txt", "w") as f:
    for file in files:
        clauses = open_file(file)
        print(file)
        # f.write(file + '\n')
        
        # DPLL
        # f.write('DPLL\n')
        start_time = time.time()
        algorithm_1 = dpll(clauses)
        print('DPLL:\n', algorithm_1)
        print(f'{time.time() - start_time} Seconds')
        # Statements for recording output
        # f.write(str(algorithm_1) + '\n')
        # f.write(f'{time.time() - start_time}\n')

        # WalkSAT
        # f.write('\nWALFSat\n')
        for i in range(10):
            start_time = time.time()
            algorithm_2, satisfiable = walk_sat(clauses, p=0.5, max_flips=10000)
            print(f'WalkSAT {i}:\n', algorithm_2)
            print(satisfiable)
            print(f'{time.time() - start_time} Seconds\n')
            # Statements for recording output
            # f.write(f'WALKSAT {i}:\n' + str(algorithm_2) + '\n')
            # f.write(satisfiable + '\n')
            # f.write(f'{time.time() - start_time}\n')

        # GSAT
        # f.write('\nGSAT\n')
        for i in range(10):
            start_time = time.time()
            algorithm_3, satisfiable = gsat(clauses, max_flips=10, max_steps=1000)
            print(f'GSAT {i}:\n', algorithm_3)
            print(satisfiable)
            print(f'{time.time() - start_time} Seconds\n')
            # Statements for recording output
            # f.write(f'GSAT {i}:\n' + str(algorithm_3) + '\n')
            # f.write(satisfiable + '\n')
            # f.write(f'{time.time() - start_time}\n')

    # f.close()
if __name__ == '__main__':
    main()