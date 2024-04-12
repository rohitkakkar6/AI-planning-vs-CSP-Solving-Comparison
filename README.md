# Final Year Project

In order to run the model pddl files:
Follow the guide on https://www.fast-downward.org/QuickStart to download and build
run the following command while keeping file locations in mind
./fast-downward.py --alias seq-sat-lama-2011 ./location/to/domain.pddl ./location/to/problem.pddl
The resulting plan will be in the SAS file if found.

To run the .z3 CSP files:
prerequisites: python3
next run pip install z3 in the command line
use the following command to use the z3 solver
z3 ./location/to/file.z3

Required: Pyamaze
pip install pyamaze

https://youtu.be/my9SsdPvrSY
youtube video to follow along ^^