import timeit
import psutil


class NQueensDFS:

    def __init__(self, size):
        self.size = size

    def solve(self):
        # Check initial size
        if self.size < 1:
            return []
        # Create stack
        solutions = []
        stack = [[]]
        # N-queens solved
        while stack:
            # pop queen from stack to solution
            solution = stack.pop()
            # Check if queens conflict
            if self.attacked(solution):
                continue
            if self.size == len(solution):
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (len(solution), col)
                queens = solution.copy()
                queens.append(queen)
                stack.append(queens)
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

    start_time = timeit.default_timer()
    # # Get the initial memory usage
    # initial_memory = psutil.Process().memory_info().rss

    n_queens = NQueensDFS(size)
    dfs_solutions = n_queens.solve()

    # # Get the final memory usage
    # final_memory = psutil.Process().memory_info().rss

    # # Calculate the total memory usage
    # total_memory = final_memory - initial_memory

    # print("Total memory usage:", total_memory, "bytes")

    end_time = timeit.default_timer()
    execution_time = (end_time - start_time)*1000
    print("Execution time:", execution_time, "milliseconds")

    if print_solutions:
        for i, solution in enumerate(dfs_solutions):
            print('DFS Solution %d:' % (i + 1))
            n_queens.print(solution)
    print('Total DFS solutions: %d' % len(dfs_solutions))


if __name__ == '__main__':
    main()
