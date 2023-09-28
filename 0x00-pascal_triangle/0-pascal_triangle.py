def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
    n (int): The number of rows to generate.

    Returns:
    List[List[int]]: A list of lists representing Pascal's triangle.

    Example:
    >>> pascal_triangle(5)
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] if i == 0 else [1, 1]
        if i > 1:
            for j in range(1, i):
                row.insert(j, triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle