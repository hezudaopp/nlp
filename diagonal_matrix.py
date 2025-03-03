import numpy as np

def create_subdiagonal_matrix():
    """
    创建一个5x5矩阵，在对角线下方放置值1,2,3,4
    """
    # 创建一个5x5的零矩阵
    matrix = np.zeros((5, 5), dtype=int)
    
    # 使用diag函数在对角线下方放置值
    # k=-1 表示在主对角线下方一行
    matrix += np.diag([1, 2, 3, 4], k=-1)
    
    print("方法1 - 使用 np.diag:")
    print(matrix)
    
    # 另一种方法：直接赋值
    matrix2 = np.zeros((5, 5), dtype=int)
    values = [1, 2, 3, 4]
    for i in range(len(values)):
        matrix2[i+1, i] = values[i]
    
    print("\n方法2 - 使用直接赋值:")
    print(matrix2)
    
    # 解释矩阵结构
    print("\n矩阵结构说明:")
    print("- 主对角线全为0")
    print("- 在主对角线下方一行依次是: 1, 2, 3, 4")
    print("- 其余位置都是0")

if __name__ == "__main__":
    create_subdiagonal_matrix() 