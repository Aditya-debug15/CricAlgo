# Project

# Aditya Malhotra

# 2020101052

Algorithms that we study have great significance in the world where we are living. In every domain algorithms have a huge role to play.

**In Security**

1. Encryption is when of the technique to send data from one place to another
2. MD5 hash, this technique gives a unquie id to the files, change in id you would there is no change with the file

**In operating system**

1. It is used for scheduling hte process
2. Having the shortest distance for client - server communication, solved using Dijkstra's algorithm.

**Stock prize** 

Machine learning and dynamic programming algorithms have in prediction of the stock prize.

**By police**

By mapping the crimes police can predict where there are high chances of another crime happening and thus resulting in catching the criminal.

**Winning games**

Through greedy and backtracking approach we can always become winner in the game we are playing, for example in chess and tic-tak-toe through algorithm we can make strategies so that we never lose

**In cricket**

This is the topic i have chosen. The game now-a-day is highly dependent upon mathematics, statistics and algorithms. There are many applications of it we will talk about many of them.

# Brute Force

In the middle of the tournament teams are worried whether they would be able to qualify for knockouts or not. There are permutations and combinations going on the in team's camp. For a second if we leave net run rate assign and try to find the probability that the team will qualify or not is to consider all the different scenarios possible. This is brute as we are considering every possible outcome. It has exponential order.

# Greedy Method

This method is not used directly by crickets but it used by organizers to schedule the games. There are teams which have more fans so organizers want that team to play match on sunday evenings to increase TRP. So during the scheduling they do greedy methods. 

It is also used to calculate the number of ways a team can qualify, in this we try to maximize the team's point and minimize the points of those team that are still in the race of qualification.

# Dynamic Programming

This have lots and lots of application in cricket or in general any sport.

The combination with probability allows us to do predictions and make win predictor

It's applications are 

1. Win predictor
2. Making strategies for batsman
3. Making startegies for bowler
4. Duckworth Lewis system
5. Even in other sports it is one most important algorithm for making startegies



More deatils can be found [here](Dynamic_Programming.md)



# PageRank Algorithm

Whenever we need to find the value associated with the player we use this algorithm. Since it gives rank based upon both upvotes and importance of those people who are upvoting.

Its applications are:

1. Breaking ties in important games
2. Helping teams to choose their retentions
3. Deciding the player of the match



More details can be found [here](Pagerank.md)



# Maximum Bipartite Matching

It can be used by the selectors to check whether the batters they have picked can actually play. I will explain the above line in detail. In cricket match we usually have 7 batting positions and we need to pick a batsman for each position. Each batter has its own preference where he wants to play (because that is where his maximum output is). But we must not have a situation where we don't have a batsman for a certain position. This will lead to a situation where the players won't be able to form a team.

Therefoe they can use Ford fulkerson's Algorithm or Kuhn's Algorithm to check if the team is selected properly or not.

For the details click [here](Maximum_Bipartite_Matching) 

# Set Cover

To select backup players we want them to have the maximum positions covered.

Most of the times selectors have to select 3 players from a pool of 6-7 players, so total combinations possible are 7C3.

For each combination we would find their set cover and would choose the set of players that have the highest set cover. 

This is solved without using but here's a twist, there are covid times going around the question is changed we are given a pool of players, we want the minimum number of players so that we have a backup for every position.

## The procedure
### Greedy choice property
We need to select the set that contains the most unique elements.

### Forming an induction
In the later stages we need to pick the set that contains most number of elements that are uncovered

Though we already know that greedy method is not optimum it takes k.ln(n) extra members but the optimum solution be exponential.

Though the pool of players is not that large so we may choose to go with either of the procedure.

# Linear Programming

Linear programming (LP, also called linear optimization) is **a method to achieve the best outcome** (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships.

I have used it to find a fantasy team. Each player has points associated with it, the goal is to maximize the points following the certain constrains.



For more details click [here](linear_programming.md)
