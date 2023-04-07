

class LongestIncreasingPath(object):

    def calculate_longest_path(self, matrix):
        """  """
        if not matrix:
            return 0

        def _longest_path(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]

            max_depth = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                   matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, _longest_path(matrix, x, y, max_lengths));
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        res = 0
        max_lengths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, _longest_path(matrix, i, j, max_lengths))
        print(res)
        return res
if __name__ == "__main__":
    longest_increasing_path = LongestIncreasingPath()
    input_matrix = [[9,9,4],[6,6,8],[2,1,1]]
    longest_increasing_path.calculate_longest_path(input_matrix)
