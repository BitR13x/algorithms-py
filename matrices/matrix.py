def createMatrix(width: int, height: int) -> list[list[int]]:
    return [[0 for _ in range(width)] for _ in range(height)]


def reverseMatix(matrix: list[list[int]]) -> list[list[int]]:
    matrix = matrix[::-1]
    for y in range(len(matrix)):
        matrix[y] = matrix[y][::-1]
    return matrix


if __name__ == "__main__":
    print(createMatrix(10, 10))