# Ehrenfest's Dog-Flea Model Simulation

This project simulates **Ehrenfest’s Dog-Flea Model**, where fleas jump between two dogs (ACE and REX) with a certain probability. The model explores the distribution of fleas between the two dogs over time and investigates long-term behavior.

## Project Overview

In the model:
- There are `N` fleas, initially all on dog REX.
- At each time step, a randomly selected flea jumps to the other dog with probability `p`.
- The program simulates this process over `tsym` time steps, tracking the number of fleas on each dog.

The results are saved in a text file and visualized through a plot showing the flea distribution over time.

## Project Structure


## Simulation Parameters

The user provides the following parameters:
- `p`: Probability of a flea jumping to the other dog (between 0 and 1).
- `N`: Number of fleas (up to 10^6).
- `tsym`: Total time steps (up to 10^6).

The simulation generates two trajectories:
- `NA`: Number of fleas on dog ACE at each time step.
- `NR`: Number of fleas on dog REX at each time step.

Results are saved in a file named according to the format:  
`N{N}p{p}t{tsym}.txt`

For example, the file `N100p0.3t1000.txt` contains results for 100 fleas, a jumping probability of 0.3, and 1000 time steps. Each row in the file records the time `t`, the number of fleas on ACE `NA`, and the number of fleas on REX `NR`.

## Plots & Analysis

The project generates a plot showing the number of fleas on both ACE and REX as a function of time `t`. 

Multiple simulations with different values of `N` can be run to observe how the flea distribution changes as the population increases. 
