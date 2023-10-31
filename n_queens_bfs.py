from queue import Queue
import psutil
import time

class NQueens:

    def __init__(self, size):
        self.size = size

    def solve_bfs(self):
        if self.size < 4:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solution = queue.get()
            if self.attacked(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                break
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                queue.put(queens)
        # print(solutions)
        return solutions

    def attacked(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)


def main():
    print('.: N-Queens Problem :.')
    size = int(input('Please enter the size of board: '))
    print_solutions = input(
        'Do you want the solutions to be printed (Y/N): ').lower() == 'y'
    n_queens = NQueens(size)
    # Get the initial memory usage
    initial_memory = psutil.Process().memory_info().rss
    
    # Get start time
    start = float(time.time())
    
    bfs_solutions = n_queens.solve_bfs()
    
    # Get end time
    end = float(time.time())
    
    # Get the final memory usage
    final_memory = psutil.Process().memory_info().rss

    # Calculate the total memory usage
    total_memory = final_memory - initial_memory
    
    # Calculate the execution time
    total_time = end - start

    if print_solutions:
        for i, solution in enumerate(bfs_solutions):
            print('BFS Solution %d:' % (i + 1))
            n_queens.print(solution)

    print('Total BFS solutions: %d' % len(bfs_solutions))
    print("The time of execution of above program is :", total_time * 10**3, "ms")
    print("Total memory usage:", total_memory, "bytes")


if __name__ == '__main__':
    main()
