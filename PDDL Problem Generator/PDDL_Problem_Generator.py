import random

class PDDLProblemGenerator:
    def __init__(self, problem_name, grid_size):
        self.problem_name = problem_name
        self.grid_size = grid_size
        self.initial_position = None

    def generate_objects(self):
        """
        Generates PDDL (Planning Domain Definition Language) objects representing positions in the grid.

        Return:
            str: A string representing PDDL objects for positions in the grid.
        """
        objects = ''
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                objects += f'cellx{i}y{j} - position\n'
        return objects

    def generate_initial_state(self):
        """
        Generates the initial state representation for the PDDL problem.

        Return:
            str: A string representing the initial state for the PDDL problem.
        """
        initial_state = ''
        # Randomly select a cell for the initial position
        i_start, j_start = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
        self.initial_position = (i_start, j_start)
        initial_state += f'(at cellx{j_start}y{i_start})\n'

        for i in range(self.grid_size):
            for j in range(1, self.grid_size):
                initial_state += f'(right-of cellx{j}y{i} cellx{j-1}y{i})\n'

        for i in range(self.grid_size):
            for j in range(self.grid_size - 1):
                initial_state += f'(left-of cellx{j}y{i} cellx{j+1}y{i})\n'

        for i in range(1, self.grid_size):
            for j in range(self.grid_size):
                initial_state += f'(is-underneath cellx{j}y{i} cellx{j}y{i-1})\n'

        for i in range(self.grid_size - 1):
            for j in range(self.grid_size):
                initial_state += f'(is-above cellx{j}y{i} cellx{j}y{i+1})\n'

        return initial_state


    def generate_goal_state(self):
        """
        Generates the goal state representation for the PDDL problem.

        Returns:
            str: A string representing the goal state for the PDDL problem.
        """
        i_start, j_start = self.initial_position
        while True:
            i_goal, j_goal = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            if (i_goal, j_goal) != (i_start, j_start):
                break
        goal_state = f'(at cellx{i_goal}y{j_goal})'
        return goal_state

    def generate_pddl(self, file_path):
        """
        Generates a PDDL (Planning Domain Definition Language) file based on the maze problem.

        Args:
            file_path (str): The path to save the generated PDDL file.
        """
        with open(file_path, 'w') as f:
            f.write(f'(define (problem {self.problem_name})\n')
            f.write('  (:domain pathfinding)\n')
            f.write('  (:objects\n')
            f.write(self.generate_objects())
            f.write('  )\n')
            f.write('  (:init\n')
            f.write(self.generate_initial_state())
            f.write('  )\n')
            f.write('  (:goal\n')
            f.write('    (and\n')
            f.write(self.generate_goal_state())
            f.write('    )\n')
            f.write('  )\n')
            f.write(')\n')


generator = PDDLProblemGenerator(problem_name='problem-pathfinding', grid_size=3)
generator.generate_pddl('problem.pddl')
