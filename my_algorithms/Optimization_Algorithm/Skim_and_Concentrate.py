#   Version: 1.0
#   Date: 31/10/2019
#   Author
#---------------------------------------------------------------------------------

import math
import random
from autograd import grad, numpy
from heapq import nsmallest
import time

def objective(x):
    return x**2

def find_iter(max_evals, n_find_size=0.5):
    '''
    Purpose: Returns the number of iterations out of max evals should be used to find the range(n_find_size)
             and the number of iterations out of max_evals should be used to find the minima greedily.
    Parameters:
        max_evals: max_number of iterations in each fmin.
        n_find_size: % of max_eval to be considered for skimming.
    '''

    n_find_range = math.floor(n_find_size*max_evals)
    n_greedy = max_evals - n_find_range

    return n_find_range, n_greedy

def calc_agent(r1,r2,n_agents,objective,trials):
    '''
    Purpose: set trials dictionary with agents, their gradients and their dirction
    Parameters:
        r1: search space start (min allowed value for x)
        r2: search space end (max allowed value for x)
        n_agents: number of agents
        objective: loss function
        trials: dictionary
    Sets following values in trials dictionary:
        n_agents: list of random points in the space ( between r1 and r2 )
        grad_func: differentitation of objective function.
        gradients: list of gradients for each agent.
        min_index: index of agent with minimum gradient.
        min_grad: minimum gradient out of all gradients.
        min_agent: agent with min gradient out of all agents.
        smin_index: index of agent with second minimum gradient.
        smin_grad: second minimum gradient out of all gradients.
        smin_agent: agent with 2nd minimum gradient out of all agents.
        loss: loss of min_agent.
    '''
    if len(trials['n_agents']) == 0:

        trials['n_agents'].extend(list(numpy.random.uniform(r1,r2,n_agents)))

        # calculate gradient
        grad_func = grad(objective)
        trials['grad_func'] =  grad_func

        # calculate gradients
        for agent in range(n_agents):
            trials['gradients'].append(grad_func(trials['n_agents'][agent]))

        indexes = range(n_agents)
        trials['min_index']=(nsmallest(1, indexes, key=lambda i: trials['gradients'][i])[-1])
        trials['min_agent']=(trials['n_agents'][trials['min_index']])
        trials['min_grad']=(trials['gradients'][trials['min_index']])


        trials['smin_index']=(nsmallest(2, indexes, key=lambda i: trials['gradients'][i])[-1])
        trials['smin_agent']=(trials['n_agents'][trials['smin_index']])
        trials['smin_grad']=(trials['gradients'][trials['smin_index']])

        trials['loss']=(objective(trials['min_agent']))

        # calculate direction
        for ii in range(n_agents):
            trials['n_direction'].append(1*(numpy.sign(trials['gradients'][ii])))


        trials['min_dir']=(trials['n_direction'][trials['min_index']])
        trials['smin_dir']=(trials['n_direction'][trials['smin_index']])
    else:

        trials['n_agents']=(list(numpy.random.uniform(r1,r2,n_agents)))


        # calculate gradient
        grad_func = trials['grad_func']

        # calculate gradients
        trials['gradients'] = []
        for agent in range(n_agents):
            trials['gradients'].append(grad_func(trials['n_agents'][agent]))



        # calculate direction
        trials['n_direction'] = []
        for ii in range(n_agents):
            trials['n_direction'].append(1*(numpy.sign(trials['gradients'][ii])))

        indexes = range(n_agents)
        trials['min_index']=(nsmallest(1, indexes, key=lambda i: trials['gradients'][i])[-1])
        if (trials['min_grad']) > (trials['gradients'][trials['min_index']]):
            trials['min_grad'] = (trials['gradients'][trials['min_index']])
            trials['min_agent']=(trials['n_agents'][trials['min_index']])
            trials['min_dir']=(trials['n_direction'][trials['min_index']])


        trials['smin_index']=(nsmallest(2, indexes, key=lambda i: trials['gradients'][i])[-1])
        if (trials['smin_grad'])>((trials['gradients'][trials['smin_index']])):
            trials['smin_agent']=(trials['n_agents'][trials['smin_index']])
            trials['smin_grad']=(trials['gradients'][trials['smin_index']])
            trials['smin_dir']=(trials['n_direction'][trials['smin_index']])
            trials['loss']=(objective(trials['min_agent']))

    return

def find_greedily(r1,r2,n_agents,objective,trials):
    '''
    Purpose: Calculate r1 ( min value x can have ) and r2 ( max value x can have ) based on minimum and 2nd minimum agents.
    Parameters:
        r1: min value x can have.
        r2: max value x can have.
    Returns: updated r1 and r2.
    '''
    min_agent = trials['min_agent']
    min_grad = trials['min_grad']
    min_dir = trials['min_dir']

    smin_agent = trials['smin_agent']
    smin_grad = trials['smin_grad']
    smin_dir = trials['smin_dir']

    if min_agent < smin_agent:
        if min_dir == 1 and smin_dir == -1:
            r1 = min_agent
            r2 = smin_agent
        elif min_dir == -1 and smin_dir == -1:
            r2 = min_agent
        elif min_dir == 1 and smin_dir ==1:
            r1 = min_agent
            r2 = smin_agent
        else:
            r2 = min_agent
    elif min_agent > smin_agent:
        if min_dir == 1 and smin_dir == -1:
            r1 = min_agent
        elif min_dir == -1 and smin_dir == -1:
            r1 = smin_agent
            r2 = min_agent
        elif min_dir == 1 and smin_dir ==1:
            r1 = min_agent
        else:
            r1 = smin_agent
            r2 = min_agent

    calc_agent(r1,r2,n_agents,objective,trials)
    return r1,r2

def fmin(fn,r1,r2,max_evals,n_find_size,trials):
    '''
    Purpose: Calls calc_range and find_greedily one after other.
    Parameters:
        fn: function to minimize
        r1: minimum value x can have
        r2: max value x can have
        n_find_size: number of times calc_range should be called.
        trials: dictionary to store info.
    '''
    n_find_range, n_greedy = find_iter(max_evals, n_find_size)

    start = time.time()
    print('Skimming started\n','-'*40)
    for ii in range(n_find_range):
        calc_agent(r1,r2,10,fn,trials) # 10 agents

    print('calculating loss greedily...')
    for ii in range(n_greedy):
        r1, r2 = find_greedily(r1,r2,20,fn,trials) # 20 agents
    end = time.time()
    print('time_taken:\t',end-start)
    print('*'*40,'\n')

def main():
    _best_x = []
    _best_loss = []

    start = time.time()
    for i in range(100):
        trials = {
            'n_agents': [],
            'n_direction': [],
            'gradients': [],
            'min_index': [],
            'min_agent': [],
            'min_grad': [],
            'min_dir': [],
            'smin_index': [],
            'smin_agent': [],
            'smin_grad': [],
            'smin_dir': [],
            'loss': []
        }
        fmin(fn = objective,r1=10000,r2=50000,max_evals=100,n_find_size=0.8,trials=trials)
        _best_x.append(trials['min_agent'])
        _best_loss.append(trials['loss'])

    end = time.time()
    print('-*-'*30)
    print('\nMin_x:\t{}\nMin_loss:\t{}'.format(_best_x[_best_loss.index(min(_best_loss))],min(_best_loss)))
    print('Time taken for all iterations:\t',end-start)

if __name__ == '__main__':
    main()
