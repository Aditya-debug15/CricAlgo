[link](.\readme.md)

# Dynamic Programming in Sports
## What is dynamic programming
It was introduced to us as a solution to the problems where we are unable to use greedy algorithms. The key point to apply dynamic programming in problems is to look at whether we are to break problem into smaller subparts and those subparts ends up in some case that we can solve.
Dynamic Programming is generally useful in cases where in problems we can identify 2 things

1) Overlapping Subproblems 
2) Optimal Substructure 

If the problem doesn't have Overlapping subproblems there is no use of dynamic programming
In DP problems we need to find relationships among the participating entities that will server the purpose of dp transitions, define the dp state.
DP state defines what our state at that given instance means.

## To show how dp can be applied in the field of sports i have chosen the following situations, these situations are cricket and tennis
1. Predicting the score a team will make depending upon the overs left and wickets in hand. [ex1](./dp_example1.md)
2. The way batsman should play to maximize run rate. [ex2](./dp_example2.md)
3. The way batsman should target different balls to maximize run rate. [ex3](./dp_example3.md)
4. Probability of chasing down the target with the given constraints. [ex4](./dp_example4.md)
5. Serving analysis for games like tennis. [ex5](./dp_example5.md)

