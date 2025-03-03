import numpy as np

def matrix_broadcasting():
    W = np.array([[1, 2, 3], [4, 5, 6]])
    X = np.array([[0, 1, 2], [3, 4, 5]])
    print(W + X)
    print(W * X)

    print(W + 1)
    print(W * 2)

    b = np.array([10, 20, 30])
    print(W * b)

if __name__ == "__main__":
    np.set_printoptions(precision=2)  # 设置打印精度
    matrix_broadcasting()