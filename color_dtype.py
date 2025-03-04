import numpy as np

def demonstrate_color_dtype():
    """
    演示如何创建和使用自定义的颜色数据类型
    RGBA格式：红(R)、绿(G)、蓝(B)、透明度(A)
    每个分量都是一个无符号字节(0-255)
    """
    # 创建自定义数据类型
    color_dtype = np.dtype([
        ('R', 'u1'),  # 无符号8位整数 (0-255)
        ('G', 'u1'),  # u1 是 uint8 的简写
        ('B', 'u1'),
        ('A', 'u1')
    ])
    
    # 创建一些颜色示例
    colors = np.array([
        (255, 0, 0, 255),      # 红色
        (0, 255, 0, 255),      # 绿色
        (0, 0, 255, 255),      # 蓝色
        (255, 255, 0, 255),    # 黄色
        (128, 0, 128, 255)     # 紫色
    ], dtype=color_dtype)
    
    print("颜色数据类型信息:")
    print(f"数据类型: {color_dtype}")
    print(f"每个颜色占用字节数: {color_dtype.itemsize}")
    print(f"字段名称: {color_dtype.names}")
    
    print("\n颜色数组:")
    for i, color in enumerate(colors):
        print(f"颜色 {i+1}:")
        print(f"  R: {color['R']:3d}")
        print(f"  G: {color['G']:3d}")
        print(f"  B: {color['B']:3d}")
        print(f"  A: {color['A']:3d}")
    
    # 演示如何访问和修改颜色值
    print("\n访问和修改颜色示例:")
    print(f"第一个颜色的红色分量: {colors[0]['R']}")
    
    # 修改透明度
    colors['A'] = 128
    print(f"修改所有颜色的透明度为128后:")
    print(colors['A'])
    
    # 创建半透明的白色
    white = np.zeros(1, dtype=color_dtype)
    white['R'] = white['G'] = white['B'] = 255
    white['A'] = 128
    print(f"\n创建的半透明白色: {white[0]}")

if __name__ == "__main__":
    demonstrate_color_dtype() 