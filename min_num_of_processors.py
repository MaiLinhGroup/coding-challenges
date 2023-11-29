# Senior Full-Stack Engineer (Presentations) opening at 
# Miro https://miro.com/careers/open-positions/
from typing import List, Tuple

def min_num_of_processors(tasks: List[Tuple[int,int]]) -> int:
    print(f"before sort: tasks = {tasks}")
    n = len(tasks)
    if (n <= 1):
        return n
     
    tasks.sort()
    print(f"after sort: tasks = {tasks}")
    p = 0
    for i in range(0, n):
        start, _ = tasks[i]
        for j in range(0, i):
            _, current_end = tasks[j]
            if start >= current_end:
                break
        else:
            p += 1   
    return p
    

if __name__ == '__main__':
    tasks: List[Tuple[int,int]] = [(30, 40), (0, 50), (40, 50), (0, 100)]
    result = min_num_of_processors(tasks)
    print(f"minimum number of processors: {result}")