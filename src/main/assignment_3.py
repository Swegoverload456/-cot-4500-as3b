"""
Programming assignment 3b
Student: Juan Velasquez
NID: ju460863
"""


"""Solve linear system using Gaussian elimination"""
def question_1():
    # Matrix
    m = [[2, -1, 1, 6],
         [1, 3, 1, 0],
         [-1, 5, 4, -3]]
    
    n = len(m)
    
    # Gaussian elimination with partial pivoting
    for i in range(n):
        # Partial pivoting
        max_row = max(range(i, n), key=lambda r: abs(m[r][i]))
        m[i], m[max_row] = m[max_row], m[i]
        
        # Elimination
        for j in range(i+1, n):
            factor = m[j][i] / m[i][i]
            for k in range(i, n+1):
                m[j][k] -= factor * m[i][k]
    
    # Back substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = m[i][n]
        for j in range(i+1, n):
            x[i] -= m[i][j] * x[j]
        x[i] /= m[i][i]
    
    return x

"""LU Factorization"""
def question_2():
    
    m = [[1, 1, 0, 3],
         [2, 1, -1, 1],
         [3, -1, -1, 2],
         [-1, 2, 3, -1]]
    
    n = len(m)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    # Perform LU decomposition
    for i in range(n):
        # Upper triangular
        for j in range(i, n):
            U[i][j] = m[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        
        # Lower triangular
        for j in range(i+1, n):
            L[j][i] = m[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]
    
    # Set diagonal of L to 1
    for i in range(n):
        L[i][i] = 1.0
    
    # Calculate determinant
    det = 1.0
    for i in range(n):
        det *= U[i][i]
    
    return det, L, U

"""Check if matrix is diagonally dominant"""
def question_3():
    
    m = [[9, 0, 5, 2, 1],
         [3, 9, 1, 2, 1],
         [0, 1, 7, 2, 3],
         [4, 2, 3, 12, 2],
         [3, 2, 4, 0, 8]]
    
    for i in range(len(m)):
        diagonal = abs(m[i][i])
        row_sum = sum(abs(m[i][j]) for j in range(len(m[i])) if j != i)
        if diagonal <= row_sum:
            return False
    return True

"""Check if matrix is positive definite"""
def question_4():
    
    m = [[2, 2, 1],
         [2, 3, 0],
         [1, 0, 2]]
    
    # Check if symmetric
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != m[j][i]:
                return False
    
    # Check all leading principal minors have positive determinants
    # Minor 1x1
    if m[0][0] <= 0:
        return False
    
    # Minor 2x2
    det2 = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if det2 <= 0:
        return False
    
    # Minor 3x3
    det3 = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
           m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
           m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    if det3 <= 0:
        return False
    
    return True

"""Function to print matrices"""
def print_matrix(matrix):
    for row in matrix:
        print([int(x) for x in row])

if __name__ == "__main__":
    # Question 1
    x = question_1()
    print("Question 1 Solution:")
    question_1_string = '['
    for val in x:
        question_1_string += ' ' + str(int(val))
    question_1_string += ']'
    print(question_1_string)
    
    # Question 2
    det, L, U = question_2()
    print("\nQuestion 2 Solutions:")
    print("a. Determinant:", det)
    print("b. L matrix:")
    print_matrix(L)
    print("c. U matrix:")
    print_matrix(U)
    
    # Question 3
    dd = question_3()
    print("\nQuestion 3 Solution:")
    print("Is diagonally dominant?", dd)
    
    # Question 4
    pd = question_4()
    print("\nQuestion 4 Solution:")
    print("Is positive definite?", pd)