# Maximum Bipartite Matching 

Let us say i have 7 batters, these 7 are the best in the nation so i want to play all of them. I have 7 positions in the team, each batter has his own prefernce that is he wants to play at a certain position. Using Maximum Bipartite Matching it would be easy to determine if the players would be able to play. That every position must have a single batsman

# Greedy won't work

<img src="screenshots/dp12.jpg">

This is an example, right now i have taken info about five players.

If we go greedy, that is i will move from 1st player to 5th player and for each player i would select the first position that is available.

In that case:

<img src="screenshots/dp13.jpg">

But the optimum answer would be:

<img src="screenshots/dp14.jpg">

This can be solved by Using Ford Fulkerson Algorithm for max flow.

We would need to change the graph a bit, we will add a dummy source and sink node, a source node will have outgoing edge to all the players and sink will have an incoming edge from all the positions.

The graph would look like:

<img src="screenshots/dp15.jpg">

Here an edge can have 2 values that is either 1 or 0. 1 meaning the batsman is going to play at that position, 0 meaning the opposite. We would apply Ford-Fulkerson Algorithm for max flow between Source and Sink which will give us our desired outcome.

This could have been done using DFS or Kuhn's Algorithm.