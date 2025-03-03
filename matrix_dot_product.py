import numpy as np

def demonstrate_dot_product():
    """
    展示不同类型的矩阵内积运算
    """
    print("1. 向量内积（点积）")
    print("-" * 40)
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    # 使用 np.dot
    dot_product = np.dot(v1, v2)
    # 手动计算
    manual_dot = sum(a*b for a, b in zip(v1, v2))
    
    print(f"向量1: {v1}")
    print(f"向量2: {v2}")
    print(f"内积 (np.dot): {dot_product}")
    print(f"内积 (手动计算): {manual_dot}")
    print(f"计算过程: ({v1[0]}×{v2[0]}) + ({v1[1]}×{v2[1]}) + ({v1[2]}×{v2[2]})")
    print()

    print("2. 矩阵与向量的内积")
    print("-" * 40)
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6]])
    vector = np.array([2, 1, 3])
    
    result = np.dot(matrix, vector)
    print(f"矩阵 (2x3):\n{matrix}")
    print(f"向量 (3x1): {vector}")
    print(f"内积结果: {result}")
    print("\n计算过程:")
    for i, row in enumerate(matrix):
        print(f"第{i+1}行: ({row[0]}×{vector[0]}) + ({row[1]}×{vector[1]}) + "
              f"({row[2]}×{vector[2]}) = {result[i]}")
    print()

    print("3. 矩阵与矩阵的内积")
    print("-" * 40)
    matrix1 = np.array([[1, 2],
                        [3, 4],
                        [5, 6]])
    matrix2 = np.array([[7, 8, 9],
                        [10, 11, 12]])
    
    result = np.dot(matrix1, matrix2)
    print(f"矩阵1 (3x2):\n{matrix1}")
    print(f"\n矩阵2 (2x3):\n{matrix2}")
    print(f"\n内积结果 (3x3):\n{result}")
    print("\n计算过程（第一个元素）:")
    print(f"result[0,0] = ({matrix1[0,0]}×{matrix2[0,0]}) + ({matrix1[0,1]}×{matrix2[1,0]})")
    print(f"           = {matrix1[0,0]*matrix2[0,0]} + {matrix1[0,1]*matrix2[1,0]}")
    print(f"           = {result[0,0]}")
    print()

    print("4. 复杂矩阵运算示例")
    print("-" * 40)
    # 创建一个简单的神经网络层的例子
    inputs = np.array([[1.0, 2.0, 3.0],    # 批量大小为2的输入
                       [0.5, 1.5, 2.5]])    # 每个输入是3维向量
    weights = np.array([[0.1, 0.2],         # 3x2的权重矩阵
                        [0.3, 0.4],
                        [0.5, 0.6]])
    
    output = np.dot(inputs, weights)        # 2x2的输出
    print("神经网络层的矩阵运算示例:")
    print(f"输入形状: {inputs.shape}")
    print(f"权重形状: {weights.shape}")
    print(f"输出形状: {output.shape}")
    print(f"\n输入:\n{inputs}")
    print(f"\n权重:\n{weights}")
    print(f"\n输出:\n{output}")

if __name__ == "__main__":
    np.set_printoptions(precision=2)  # 设置打印精度
    demonstrate_dot_product() 