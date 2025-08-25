# Midterm Project: VRP with a Quantum-Inspired Genetic Algorithm

This repository contains the solution for the ACIT 4610 Mid-Term Group Project, focusing on solving the Vehicle Routing Problem (VRP) using a Quantum-Inspired Evolutionary Algorithm.

## The Problem

The Vehicle Routing Problem (VRP) is a classic combinatorial optimization problem where the goal is to find the most efficient set of routes for a fleet of vehicles to serve a group of customers from a central depot.

The primary objective is to **minimize the total travel distance or time** for all vehicle routes while ensuring that every customer is visited exactly once. For the scope of this project, advanced constraints like vehicle capacity and customer time windows will be considered optional for the initial implementation.

### Problem Scenarios

The project requires the implementation and analysis of the algorithm across three categories of problem instances, with two distinct scenarios for each category:

*   **Small Scenarios:**
    *   1 Depot
    *   2 to 10 vehicles
    *   10 to 20 customer locations
*   **Medium Scenarios:**
    *   1 Depot
    *   11 to 25 vehicles
    *   15 to 30 customer locations
*   **Large Scenarios:**
    *   1 Depot
    *   26 to 50 vehicles
    *   20 to 50 customer locations

## Project Steps

1.  **Data Modeling & Parsing:**
    *   Define a clear data structure for the VRP instance (depot, customers with coordinates, distance matrix).
    *   Implement a parser to load the problem scenarios from a defined data format (e.g., text files, JSON).

2.  **Algorithm Implementation: Genetic Algorithm (GA)**
    *   Design and implement a Genetic Algorithm to solve the VRP. This includes:
        *   **Individual Representation:** Define how a chromosome represents a potential solution (a set of routes).
        *   **Initialization:** Create an initial population of random, valid solutions.
        *   **Genetic Operators:** Implement crossover, mutation, and selection operators tailored for the VRP.
        *   **Termination Criteria:** Define when the algorithm should stop (e.g., after a fixed number of generations).
    *   The code should be well-structured, commented, and organized within this repository.

3.  **Analysis & Evaluation:**
    *   Define and implement performance evaluation metrics (e.g., solution quality, convergence rate, execution time).
    *   Test the GA on all three problem categories (Small, Medium, Large).
    *   Analyze the impact of different GA parameters (population size, crossover/mutation probability, generation number) on the results.

4.  **Reporting:**
    *   Generate the final vehicle routes as the solution output.
    *   (Optional) Implement a visualization of the routes.
    *   Summarize the findings in a 1000-1500 word report, as per the assignment guidelines.

## Tech Stack

*   **Language:** Python
*   **Libraries (Recommended):**
    *   `NetworkX`: For graph-based data modeling and analysis.
    *   `OR-Tools`: A powerful suite for optimization problems.
    *   `Matplotlib` / `Plotly`: For visualizing the routes.

## How to Run

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Algorithm:**
    ```bash
    python main.py --scenario <scenario_file>
    ```
