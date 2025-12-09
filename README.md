# Employee Hours Optimizer

A Python-based optimization tool that generates work schedules for employees based on their target weekly hours while minimizing the total number of days each employee works.

## Overview

This project uses mathematical optimization (via Gurobi) to create efficient employee schedules that:
- Meet each employee's target hours per week
- Minimize the number of working days for each employee
- Balance workload across the scheduling period

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager
- Gurobi Optimizer (requires a valid license)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd employee-hours-optimizer
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Ensure you have a valid Gurobi license configured on your system.

## Usage

Run the optimizer:
```bash
uv run python main.py
```

## License

MIT
