# MID-TERM Vehicle Routing Problem (VRP) Optimization

This repository contains the implementation for the ACIT 4610 Mid-Term Project, focusing on solving the Vehicle Routing Problem (VRP) using Genetic Algorithms with comprehensive performance analysis across multiple problem scales.

## Project Overview

The Vehicle Routing Problem (VRP) is a combinatorial optimization challenge where the goal is to determine optimal routes for a fleet of vehicles serving customers from a central depot. This project implements and analyzes genetic algorithm solutions across different problem scales.

### Objective

**Minimize total travel distance** for all vehicle routes while ensuring:

- Each customer is visited exactly once
- All vehicles start and end at the depot
- Valid route assignments for the available fleet

## Problem Scale Requirements

This project implements and compares GA performance across three distinct categories:

### Small Instances

- **Vehicles:** 2-10
- **Customers:** 10-20
- **Depot:** 1
- **Scenarios:** 2 different instances

### Medium Instances

- **Vehicles:** 11-25
- **Customers:** 15-30
- **Depot:** 1
- **Scenarios:** 2 different instances

### Large Instances

- **Vehicles:** 26-50
- **Customers:** 20-50
- **Depot:** 1
- **Scenarios:** 2 different instances

**Total Test Cases:** 6 problem instances (3 categories × 2 scenarios each)

## Implementation Components

### 1. Genetic Algorithm Core

- **Chromosome Representation:** Permutation with separators for multi-vehicle routes
- **Population Initialization:** Random valid route assignments
- **Fitness Function:** Inverse of total distance (shorter routes = higher fitness)
- **Crossover:** Order-based crossover preserving gene validity
- **Mutation:** Customer gene swapping (preserves route structure)
- **Selection:** Tournament or roulette wheel selection

### 2. Performance Evaluation Metrics

- **Solution Quality:** Best, average, and worst fitness per generation
- **Convergence Rate:** Generation when optimal/near-optimal solution found
- **Computational Efficiency:** Execution time per instance size
- **Parameter Sensitivity:** Impact of GA parameters on performance

### 3. Parameter Analysis

Testing across **three parameter sets:**

- **Population Size:** Small, Medium, Large populations
- **Generation Count:** Different termination criteria
- **Crossover Probability:** Various crossover rates
- **Mutation Probability:** Different mutation rates

### 4. Data Structure

```python
# Location representation
LOCATIONS = [(x, y), ...]  # Coordinates for depot + customers
CUSTOMERS = [1, 2, ..., n]  # Customer indices (depot = 0)

# Chromosome example: [3, 1, 0, 5, 2, 6, 4]
# Routes: Vehicle 1: [3, 1], Vehicle 2: [5, 2, 6, 4]
# Separator (0) divides routes between vehicles
```

## Current Implementation Status

### ✅ Completed Components

- Basic VRP chromosome representation with separators
- Fitness function for multi-vehicle distance calculation
- Simplified crossover function (Order-based approach)
- VRP-specific mutation function (customer gene swapping)
- Small-scale testing framework (7 locations, 2 vehicles)

### 🚧 In Progress

- Problem instance generators for small/medium/large scales
- Complete GA loop with selection and elitism
- Performance metrics collection and analysis
- Parameter sensitivity testing framework

### 📋 Remaining Tasks

- Generate 6 test problem instances (2 per category)
- Implement performance tracking and convergence analysis
- Build comparison framework for different GA parameters
- Create visualization tools for routes and performance
- Comprehensive testing and results analysis
- Final report compilation (1000-1500 words)

## File Structure

```
MID-TERM-Vehicle-Routing-Problem-VRP-Optimization/
├── main.ipynb                 # Main implementation notebook
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── Task/
│   └── Assignment-1.pdf      # Project requirements
├── data/                     # Problem instances (to be generated)
├── results/                  # Performance analysis results
└── visualizations/           # Route and performance plots
```

## Tech Stack

- **Language:** Python 3.8+
- **Core Libraries:**
  - `random` - Genetic algorithm operations
  - `matplotlib` - Visualization and plotting
  - `numpy` - Numerical computations
  - `pandas` - Data analysis and results tracking
- **Development Environment:** Jupyter Notebook
- **Visualization:** Matplotlib for route plotting and performance graphs

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Notebook

```bash
jupyter notebook main.ipynb
```

### 3. Execute Components

The notebook contains modular sections for:

- Problem instance generation
- GA algorithm execution
- Performance analysis
- Results visualization

## Performance Metrics

The project evaluates GA performance using:

1. **Solution Quality Metrics:**

   - Best fitness achieved
   - Average fitness over generations
   - Solution consistency across runs

2. **Convergence Analysis:**

   - Generations to reach optimal solution
   - Convergence stability
   - Premature convergence detection

3. **Computational Efficiency:**

   - Execution time per problem size
   - Memory usage scaling
   - Algorithm complexity analysis

4. **Parameter Sensitivity:**
   - Population size impact
   - Crossover/mutation rate effects
   - Generation count optimization

## Expected Deliverables

1. **Working GA Implementation** - Complete genetic algorithm for VRP
2. **Problem Instance Generator** - Creates test cases for all three scales
3. **Performance Analysis Framework** - Metrics collection and comparison
4. **Visualization Tools** - Route plotting and performance graphs
5. **Comprehensive Results** - Analysis across all parameter combinations
6. **Final Report** - 1000-1500 word summary of findings and conclusions

## Research Questions

This project aims to answer:

- How does GA performance scale with problem size (small → medium → large)?
- What GA parameters are most effective for different VRP instance sizes?
- How does solution quality vary with computational resources (time/generations)?
- What are the convergence characteristics of GA for multi-vehicle routing problems?

## Contributors

ACIT 4610 Mid-Term Project Team
