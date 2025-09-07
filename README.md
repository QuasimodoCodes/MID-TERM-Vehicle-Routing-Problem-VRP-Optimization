# ACIT 4610 Mid-Term Project: Vehicle Routing Problem Using Genetic Algorithms

This repository contains the complete implementation for the ACIT 4610 Mid-Term Group Project, developing and implementing a Genetic Algorithm (GA) to solve the Vehicle Routing Problem (VRP) across multiple problem scales with comprehensive performance analysis.

## Project Overview

The Vehicle Routing Problem (VRP) involves finding the most efficient routes for a fleet of vehicles to serve a group of customers from a central depot. This project implements a genetic algorithm solution with rigorous experimental analysis across three problem categories.

### Objective

**Minimize total travel distance** for all vehicle routes while ensuring:

- Each customer is visited exactly once
- Every route begins and ends at the depot
- All customers are served by the available vehicle fleet

## Problem Definition (As per Assignment Requirements)

### Problem Scenarios: Three Categories with 2 Instances Each

#### **Small VRP (2-10 vehicles, 10-20 customers)**

- **Scenario 1**: Dense Cluster - 7 customers, 2 vehicles
- **Scenario 2**: Spread Pattern - 18 customers, 5 vehicles
- **Implementation**: `Victor/Small.ipynb`

#### **Medium VRP (11-25 vehicles, 15-30 customers)**

- **Scenario 1**: Compact Layout - 20 customers, 15 vehicles
- **Scenario 2**: Wide Distribution - 25 customers, 20 vehicles
- **Implementation**: `Herman/MediumH.ipynb`

#### **Large VRP (26-50 vehicles, 20-50 customers)**

- **Scenario 1**: Metropolitan Area - 35 customers, 30 vehicles
- **Scenario 2**: Regional Network - 45 customers, 40 vehicles
- **Implementation**: `Carl/LargeC.ipynb`

**Total Test Cases:** 6 problem instances (3 categories × 2 scenarios each)

## Implementation Components

### 1. Genetic Algorithm Core

- **Chromosome Representation:** Permutation with separators for multi-vehicle routes
- **Population Initialization:** Random valid route assignments
- **Fitness Function:** Inverse of total distance (shorter routes = higher fitness)
- **Crossover:** Order-based crossover preserving gene validity
- **Mutation:** Customer gene swapping (preserves route structure)
- **Selection:** Tournament or roulette wheel selection

### 2. Performance Evaluation Metrics (Assignment Section 2)

The project evaluates GA performance using the following metrics:

- **Solution Quality:** Best distance achieved, average performance across trials
- **Required Time:** Execution time per problem instance and parameter set
- **Convergence Rate:** Speed of reaching optimal/near-optimal solutions
- **Computational Efficiency:** Scalability across problem sizes

### 3. GA Parameter Sets Analysis (Assignment Section 3b)

**Three Parameter Configurations Tested:**

- **SET_1 (Conservative):** Population=30, Generations=50, Crossover=0.7, Mutation=0.1
- **SET_2 (Balanced):** Population=50, Generations=100, Crossover=0.8, Mutation=0.2
- **SET_3 (Aggressive):** Population=80, Generations=75, Crossover=0.9, Mutation=0.3

**Analysis Framework:** Each parameter set tested across all 6 problem instances with 10 independent trials per configuration for statistical reliability.

### 4. Example Data (Assignment Section 1c)

**Data Representation:**

```python
# Location coordinates (Euclidean distance model)
LOCATIONS = [(x, y), ...]  # Depot at index 0, customers at 1..n
DISTANCES = euclidean_distance(loc1, loc2)  # Distance calculation

# GA Chromosome representation
# Example: [3, 1, 0, 5, 2, 6, 4, 0]
# Routes: Vehicle 1: [3, 1], Vehicle 2: [5, 2, 6, 4]
# Separator (0) divides routes between vehicles
```

**Sample Problem Instance:**

- **Depot:** (0, 0)
- **Customers:** [(5, 5), (10, 3), (8, 8), (2, 7), ...]
- **Distance Matrix:** Calculated using Euclidean distance formula

## Implementation Status

### Completed Implementation

- **Complete GA Algorithm:** Population initialization, selection, crossover, mutation
- **VRP-Specific Operators:** Route-preserving crossover and mutation
- **Performance Evaluation:** Statistical analysis across 180 experimental runs
- **Comprehensive Analysis:** Parameter effectiveness across all problem scales
- **Visualization Tools:** Route plotting and performance charts
- **Results Framework:** Automated comparison and statistical significance testing

### Experimental Results

- **Total GA Runs:** 180 (3 categories × 2 scenarios × 3 parameter sets × 10 trials)
- **Statistical Rigor:** 10 independent trials per configuration
- **Performance Metrics:** Solution quality, execution time, convergence analysis
- **Comprehensive Analysis:** Available in `Comprehensive_Results_Analysis.ipynb`

## Repository Structure

```
MID-TERM-Vehicle-Routing-Problem-VRP-Optimization/
├── Victor/
│   ├── Small.ipynb           # Small VRP implementation (2-10 vehicles)
│   └── README.md             # Small VRP documentation
├── Herman/
│   ├── MediumH.ipynb         # Medium VRP implementation (11-25 vehicles)
│   └── VRP_GA_AllInOneTEST3.ipynb  # Alternative implementation
├── Carl/
│   └── LargeC.ipynb          # Large VRP implementation (26-50 vehicles)
├── Comprehensive_Results_Analysis.ipynb  # Complete comparative analysis
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── Task/
    └── Assignment-1.pdf      # Project requirements
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

## How to Run the Analysis

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Execute Individual Problem Categories

```bash
# Small VRP problems
jupyter notebook Victor/Small.ipynb

# Medium VRP problems
jupyter notebook Herman/MediumH.ipynb

# Large VRP problems
jupyter notebook Carl/LargeC.ipynb
```

### 3. Run Comprehensive Analysis

```bash
# Complete comparative analysis across all categories
jupyter notebook Comprehensive_Results_Analysis.ipynb
```

**Note:** The comprehensive analysis notebook automatically imports results from all three problem categories and generates the complete comparison required by the assignment.

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

## Assignment Deliverables ✅

### 1. Problem Definition (Section 1)

- ✅ **Three problem categories** with 2 scenarios each (Small, Medium, Large VRP)
- ✅ **Clear objective:** Minimize total travel distance while serving all customers
- ✅ **Example datasets:** Coordinate-based instances with Euclidean distance calculation

### 2. Performance Evaluation Metrics (Section 2)

- ✅ **Solution Quality:** Best distance achieved per configuration
- ✅ **Required Time:** Execution time analysis across all test problems
- ✅ **Convergence Rate:** Statistical analysis of algorithm performance
- ✅ **Computational Efficiency:** Scaling behavior across problem sizes

### 3. Comparison and Analysis (Section 3)

- ✅ **Cross-category comparison:** Small vs Medium vs Large VRP performance
- ✅ **Three GA parameter sets:** Conservative, Balanced, and Aggressive configurations
- ✅ **Statistical rigor:** 10 trials per configuration for reliable results
- ✅ **Comprehensive analysis:** Parameter correlations and evolutionary stage effects

## Key Results Summary

- **180 Total Experiments:** Rigorous statistical analysis across all combinations
- **Parameter Effectiveness:** Balanced parameters optimal for Small/Medium, Aggressive for Large
- **Execution Time Scaling:** Super-linear growth with problem complexity
- **Statistical Significance:** Reliable conclusions based on multiple independent trials

## Research Questions Answered

✅ **Scalability:** GA performance scales predictably but super-linearly with problem size  
✅ **Parameter Optimization:** Different parameter sets optimal for different VRP scales  
✅ **Quality vs Resources:** Clear trade-offs identified between solution quality and computation time  
✅ **Convergence Analysis:** Early exploration vs late exploitation parameter effects characterized

## Contributors

**ACIT 4610 Mid-Term Project Team**

- Implementation across three problem scales with comprehensive statistical analysis
- Genetic Algorithm optimization for Vehicle Routing Problem
- Performance evaluation and parameter sensitivity analysis
