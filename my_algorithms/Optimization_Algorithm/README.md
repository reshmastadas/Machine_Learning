Description for skim_and_concentrate algorithm:
Author: Reshma Tadas

-----------------------------------------------------------------------------------------------------

Abstract:
  1. Algorithms are mainly of two types:
    Random Algorithms
    Greedy Algorithms
  2. Random Algorithms have higher chance to get out of local minima.
  3. Greedy Algorithms are good in finding most optimal short term solution.
  4. This algorithm(skim and concentrate) is an attempt to get best of both worlds.

Approach:
  In this algorithm there are two phases:
    1. skimming
    2. concentrate
  Skimming:
    This phase contains following steps:
      1. Generation of Agents:
          An agent is merely a point in search space (1d uniform space).
          In every iteration new set of agents are generated.
          The number of agents is given by the parameter n_agents
      2. Calculation of gradients:
          Gradients are calculated by passing agents to the gradient function (differentitation of input function).
      3. Calculate min_index, min_grad, min_agent and loss:
          min_index is index of agent with minimum gradient
          min_grad is the minimum gradient Value
          min_agent is agent with minimum gradient.
          loss is minimum loss.
      3. Calculate smin_index, smin_grad, smin_agent:
          smin_index is index of agent with 2nd minimum gradient
          smin_grad is the 2nd minimum gradient Value
          smin_agent is agent with 2nd minimum gradient.
      4. Calculate direction:
          -1 if gradient of that agent is -ve
          +1 if gradient of that agent is +ve
    Skimming is done for floor(n_find_size*max_evals) times.
    where n_find_size is the % of max_evals for which skimming has to be done.

  Concentrate:
    After completion of skimming, the ranges r1 and r2 are greedily found for each iteration. This process is called Concentrate.
    The new ranges are calculated as below:
      1. if min_agent < smin_agent
          a. if direction fo min_agent is +1 and smin_agent is -1 respectively then,
              r1 = min_agent
              r2 = smin_agent
          b. if direction of both min_agent and smin_agent are -1 then,
              r2 = smin_agent
          c. if direction of min_agent and smin_agent are +1 then,
              r1 = min_agent
              r2 = smin_agent
          d. if direction of min_agent is -1 and smin_agent is +1 then,
              r2 = min_agent
      2. if min_agent > smin_agent
          a. if direction fo min_agent is +1 and smin_agent is -1 respectively then,
              r1 = min_agent
          b. if direction of both min_agent and smin_agent are -1 then,
              r1 = smin_agent
              r2 = min_agent
          c. if direction of min_agent and smin_agent are +1 then,
              r1 = min_agent
          d. if direction of min_agent is -1 and smin_agent is +1 then,
              r1 = smin_agent
              r2 = min_agent
    Finally for skimming is done with new r1 and r2 (so that the agents generated in skimming will lie between modified r1 and r2).
    This process of calculation of r1 and r2 and skimming is done max_eval-floor(n_find_size*max_evals) times.
    Best loss can be found in trials['loss'] value.
