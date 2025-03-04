import numpy as np

def demonstrate_1d_sum():
    """
    演示一维数组的sum函数操作
    对于一维数组，axis=-1 和不指定axis的效果是一样的，
    都是计算整个数组的总和
    """
    # 创建一个一维数组
    a = np.array([1, 2, 3, 4, 5])
    
    print("一维数组:")
    print(a)
    print("数组形状:", a.shape)
    
    # 不同的求和方式
    sum_no_axis = np.sum(a)          # 不指定axis
    sum_axis_minus_1 = np.sum(a, -1) # 指定axis=-1
    sum_axis_0 = np.sum(a, 0)        # 指定axis=0
    
    print("\n不同求和方式的结果:")
    print(f"sum(a)     = {sum_no_axis}")
    print(f"sum(a, -1) = {sum_axis_minus_1}")
    print(f"sum(a, 0)  = {sum_axis_0}")
    
    print("\n解释:")
    print("1. 对于一维数组，axis=-1 和 axis=0 的效果是一样的")
    print("2. 这是因为一维数组只有一个轴（维度）")
    print("3. 结果都是计算整个数组的总和")
    
    # 创建一个更复杂的例子
    b = np.array([10, 20, 30, 40, 50])
    print("\n另一个一维数组示例:")
    print(b)
    print(f"sum(b, -1) = {np.sum(b, -1)}")
    print("计算过程: " + " + ".join(str(x) for x in b) + f" = {np.sum(b, -1)}")

if __name__ == "__main__":
    demonstrate_1d_sum() 