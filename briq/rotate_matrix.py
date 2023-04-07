"""
Author Devendra
"""

"""
Author Devendra
"""


class RotateMatrix:
    def rotate_matrix(self, input_matrix) -> None:
        if input_matrix is None or len(input_matrix) == 0 or len(input_matrix[0]) == 0:
            return 0
        rows = len(input_matrix)
        cols = len(input_matrix[0])

        first, last = 0, rows - 1

        while first < last:
            input_matrix[first], input_matrix[last] = input_matrix[last], input_matrix[first]
            first += 1
            last -= 1

        for i in range(0, rows):
            for j in range(i + 1, cols):
                input_matrix[i][j], input_matrix[j][i] = input_matrix[j][i], input_matrix[i][j]

        return input_matrix


if __name__ == "__main__":
    rotate_matrix = RotateMatrix()
    input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix.rotate_matrix(input_data))
