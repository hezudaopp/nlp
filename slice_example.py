import numpy as np

def demonstrate_slicing():
    """
    演示NumPy中的切片操作，特别是负索引的使用
    """
    # 创建一个5x5的示例数组
    a = np.arange(25).reshape(5, 5)
    
    print("原始数组:")
    print(a)
    print("\n索引说明:")
    print("a[1:-1, 1:-1] 表示:")
    print("- 行：从索引1（第2行）到-1（倒数第1行）之前")
    print("- 列：从索引1（第2列）到-1（倒数第1列）之前")
    
    # 使用[1:-1, 1:-1]切片
    center = a[1:-1, 1:-1]
    print("\n使用 a[1:-1, 1:-1] 提取的中心区域:")
    print(center)
    
    # 展示不同的负索引效果
    print("\n不同负索引的效果:")
    print("最后一个元素 a[-1, -1]:", a[-1, -1])
    print("倒数第二个元素 a[-2, -2]:", a[-2, -2])
    
    # 创建一个新数组并修改中心区域
    b = np.ones((5, 5), dtype=int)
    print("\n新数组:")
    print(b)
    
    # 将中心区域设为0
    b[1:-1, 1:-1] = 0
    print("\n将中心区域设为0后:")
    print(b)
    print("\n这个操作保留了边界的1，将内部区域（除了第一行/列和最后一行/列）设为0")

if __name__ == "__main__":
    demonstrate_slicing() 