# main.py

import argparse

def main():
    parser = argparse.ArgumentParser(description='Solve the VRP using a Genetic Algorithm.')
    parser.add_argument('--scenario', type=str, required=True, help='Path to the scenario file.')
    args = parser.parse_args()

    print(f"Running GA for scenario: {args.scenario}")
    # 1. Load data from scenario file
    # 2. Initialize population
    # 3. Run Genetic Algorithm
    # 4. Print or save results

if __name__ == "__main__":
    main()
