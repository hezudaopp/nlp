import numpy as np

def demonstrate_sum_axis():
    """
    演示NumPy中sum函数在不同轴上的操作
    axis=-1 表示最后一个轴（维度）
    """
    # 创建一个3维数组
    a = np.array([
        [[1, 2, 3],
         [4, 5, 6]],
        [[7, 8, 9],
         [10, 11, 12]]
    ])
    
    print("原始3维数组形状:", a.shape)
    print("原始数组:")
    print(a)
    
    # 沿着最后一个轴（axis=-1）求和
    sum_last_axis = np.sum(a, axis=-1)
    print("\n沿着最后一个轴求和 (axis=-1):")
    print("结果形状:", sum_last_axis.shape)
    print("结果:")
    print(sum_last_axis)
    print("解释: 每一行的元素相加")
    
    # 沿着第一个轴（axis=0）求和
    sum_first_axis = np.sum(a, axis=0)
    print("\n沿着第一个轴求和 (axis=0):")
    print("结果形状:", sum_first_axis.shape)
    print("结果:")
    print(sum_first_axis)
    print("解释: 相同位置的元素相加")
    
    # 沿着第二个轴（axis=1）求和
    sum_second_axis = np.sum(a, axis=1)
    print("\n沿着第二个轴求和 (axis=1):")
    print("结果形状:", sum_second_axis.shape)
    print("结果:")
    print(sum_second_axis)
    print("解释: 每个2D切片中的行相加")
    
    # 创建一个2维数组的例子
    b = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print("\n2维数组示例:")
    print(b)
    print("\n沿着最后一个轴求和 (axis=-1):")
    print(np.sum(b, axis=-1))
    print("解释: 每一行的元素相加")

if __name__ == "__main__":
    demonstrate_sum_axis() 