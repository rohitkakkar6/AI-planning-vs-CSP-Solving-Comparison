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
