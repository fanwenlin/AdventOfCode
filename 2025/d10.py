import sys
import numpy as np
from collections import deque

from ortools.sat.python import cp_model

class Problem:    
    def __init__(self, line:str):
        self.target_state = 0
        self.target_states = []
        self.buttons = []
        self.button_states = []
        self.initial_state = 0
        self.target_counter = []
    

        for c in line.split(' '):
            c = c.strip()
            if c.startswith('['):
                self.target_state = c[1:-1][::-1].replace('.', '0').replace('#', '1')
                # convert from binary string to integer
                self.target_state = int(self.target_state, 2)
                self.target_states = [0 if ch == '.' else 1 for ch in c[1:-1]]
            elif c.startswith('('):
                self.buttons.append(list(map(int, c[1:-1].split(','))))
                self.button_states.append(sum([(1<< i) for i in self.buttons[-1]]))
            elif c.startswith('{'):
                self.target_counter = list(map(int, c[1:-1].split(',')))
    
    def solve1(self) -> int:
    
        q = deque([(self.initial_state, 0)])
        visited = set()
        while q:
            state, steps = q.popleft()
            if state == self.target_state:
                return steps
                
            for button in self.button_states:
                new_state = state ^ button
                if new_state not in visited:
                    visited.add((new_state, steps + 1))
                    q.append((new_state, steps + 1))
        
        return -1
    
    def solve1WithCP(self) -> int:
        model = cp_model.CpModel()
        variables = []
        
        for i in range(len(self.buttons)):
            x = model.NewBoolVar(f'x{i}')
            variables.append(x)

        pos = [[] for _ in range(len(self.target_states))]
        
        for i in range(len(self.buttons)):
            for position in self.buttons[i]:
                pos[position].append(variables[i])

        for i, state in enumerate(self.target_states):
            sum_var = model.NewIntVar(0, len(pos[i]), f'sum_pos_{i}')
            model.Add(sum_var == sum(pos[i]))

            model.AddModuloEquality(state, sum_var, 2)

        model.Minimize(sum(variables))
        solver = cp_model.CpSolver() 
        status = solver.Solve(model)
        
        if status == cp_model.OPTIMAL:
            return int(solver.ObjectiveValue())
        elif status == cp_model.FEASIBLE:
            return int(solver.ObjectiveValue())
        else:
            print(f'Status: {status}') # 3=INFEASIBLE, 0=UNKNOWN
            return -1
    
    def solve2(self) -> int:
        model = cp_model.CpModel()
        variables = []
        pos = [[] for _ in range(len(self.target_counter))] 
        
        for i in range(len(self.buttons)):
            # how many times to press the button
            x = model.NewIntVar(0, max([self.target_counter[position] for position in self.buttons[i]]), f'x{i}')
            variables.append(x)
            for position in self.buttons[i]:
                pos[position].append(x)
        for i, cnt in enumerate(self.target_counter):
            model.Add(sum(pos[i]) == cnt)

        model.minimize(sum(variables))
        
        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        if status == cp_model.FEASIBLE:
            print('not optimal')
            return int(solver.ObjectiveValue())
        elif status == cp_model.OPTIMAL:
            return int(solver.ObjectiveValue())
        else:
            print('not feasible')
            return -1

lines = [line for line in sys.stdin]

ans1 = 0
for line in lines:
    problem = Problem(line)
    ans1 += problem.solve1WithCP()

print('ans1: ', ans1)



ans2 = 0
for line in lines:
    problem = Problem(line)
    ans2 += problem.solve2()
print('ans2: ', ans2)