# Untitled

October 20, 2023 

Installed PDDL extension for VSCode, ran a couple examples in the github provided to see outputs and familiarise myself with running them.

October 26, 2023 

Researched use of test cases in PDDL and tried figuring out if it was feasible to use them in my project.

October 30, 2023 

Researched Constraint Satisfaction Problems through Artificial Intelligence Principles and Techniques 5. CSP, Part I: Basics and Na ̈ıve Search

November 2, 2023 

Ran Z3 solver on an altered file for Sudoku trying a 3x3 for proof of concept and had to figure out how to use z3. Got it to run successfully.

November 13, 2023

Tried multiple different approaches of using the fast-downward planner, finally got it working

Novemeber 14, 2023

Tried a different implementation of the 3x3 PDDL model, finally got it working
November 11, 2023

Ran Z3 solver on classic 9x9 grid, noted it takes some time to find a solution.
November 30, 2023

Decided on splitting up the code to see the breaking point as running the full implementation timed out the planner resulting in no plans

tests on 1 row and 3 rows are successful with 1 row taking 0.35 seconds on average to solve and the 3 rows implementation taking 0.55 seconds on average by the online solver.

testing 5x9 shows the first significant leap in time going from 1 second to 4.2 seconds on average to find a plan

December 1, 2023

6x9 found as the breaking point

December 4, 2023

Decided on moving onto problems more suited to modelling which do not require backtracking
as this is something that off the shelf planners lack.

December 7, 2023

Wanted to improve my testing methodology, decided to create a python script that can count how many times a digit appears
in each row, column and subgrid

added functionality to read files, and return valid if the plan is valid

January 18, 2024

Decided on a switch in project direction to pathfinding using the experience gained through modelling sudoku

January 19, 2024

Planning on modelling a 4x4 grid to model a pathfinding problem going from A to B for an agent,
will be done in pddl and csp to compare the implementations.

January 21, 2024

Researched A* and how it could be implemented into my planning solution, along with
backtracking with forward propagation for the csp solution as this shouldn't be too
complex and can provide insight into the strenghts and weaknesses.

February 12, 2024

Connected fast downward planner to pddl vscode extension allowing for problem files to be used as test cases

February 17, 2024

All actions for PDDL pathfinding model complete, start creating problem files.

February 22, 2024

Sample problem files along with tests complete, start researching different implementations of csp version of the pathfinding problem.

February 25, 2024

Development for constraint satisfaction version of the pathfinding problem,
Create variables, create domain, create constraints

February 26, 2024

Start thinking about how to develop in python using test driven development

February 29, 2024

Experiment with unittest

March 2, 2024

Research A*, start development using python

Develop manhattan distance heuristic as currently vertical and horizontal movements are allowed so the estimate is more realistic

Develop tests for the heuristic function

March 6, 2024

Research CSP methods for backtracking, constraints, Keep track of AIMA fig 6.5

Successor_generator

March 8, 2024

Look into parsing files

regex?

March 14, 2024

Noticed flaw in problem definition, double digits not accounted for

March 17, 2024

Parser needs accounting for new grid structure

March 22, 2024

Utilise adjacencies to get the max grid size

March 26, 2024

Test backtrack in csp

March 29, 2024

Maze generation possibilty, pyamaze

April 2, 2024

csp: new constraint for cell walls, update consistent and goal

April 6, 2024

Look into new heuristic possibilities/solving techniques

April 9, 2024

Chunking the maze, ipdb? hmax? lmcut? lama?

April 11, 2024

Pickle for storing paths, landmarks?