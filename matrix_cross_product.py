import numpy as np

def manual_cross_product(v1, v2):
    """
    手动计算两个三维向量的叉乘，展示计算过程
    参数:
        v1: 第一个向量 [a1, a2, a3]
        v2: 第二个向量 [b1, b2, b3]
    返回:
        叉乘结果 [c1, c2, c3]，其中：
        c1 = a2*b3 - a3*b2
        c2 = a3*b1 - a1*b3
        c3 = a1*b2 - a2*b1
    """
    # 获取向量分量
    a1, a2, a3 = v1
    b1, b2, b3 = v2
    
    # 计算每个分量
    c1 = a2*b3 - a3*b2
    c2 = a3*b1 - a1*b3
    c3 = a1*b2 - a2*b1
    
    print(f"\n计算过程:")
    print(f"第一个分量 (i): {a2}*{b3} - {a3}*{b2} = {c1}")
    print(f"第二个分量 (j): {a3}*{b1} - {a1}*{b3} = {c2}")
    print(f"第三个分量 (k): {a1}*{b2} - {a2}*{b1} = {c3}")
    
    return np.array([c1, c2, c3])

def vector_cross_product(v1, v2):
    """
    使用 NumPy 计算两个三维向量的叉乘
    """
    return np.cross(v1, v2)

def calculate_geometric_properties(v1, v2):
    """
    计算向量叉乘的几何性质
    """
    # 计算叉乘
    cross_product = np.cross(v1, v2)
    
    # 计算向量的模（长度）
    v1_magnitude = np.linalg.norm(v1)
    v2_magnitude = np.linalg.norm(v2)
    cross_magnitude = np.linalg.norm(cross_product)
    
    # 计算向量间的夹角（弧度）
    dot_product = np.dot(v1, v2)
    cos_theta = dot_product / (v1_magnitude * v2_magnitude)
    theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    
    # 计算平行四边形的面积
    area = cross_magnitude
    
    print("\n几何性质分析:")
    print(f"向量v1的长度: {v1_magnitude:.2f}")
    print(f"向量v2的长度: {v2_magnitude:.2f}")
    print(f"两向量夹角: {np.degrees(theta):.2f}度")
    print(f"叉乘结果向量的长度: {cross_magnitude:.2f}")
    print(f"两向量所围平行四边形的面积: {area:.2f}")
    print(f"验证: |v1|*|v2|*sin(θ) = {(v1_magnitude * v2_magnitude * np.sin(theta)):.2f}")
    
    # 验证垂直性
    dot_with_cross = np.dot(cross_product, v1)
    print(f"\n垂直性验证:")
    print(f"叉乘结果与v1的点积: {dot_with_cross:.2e}")
    print(f"叉乘结果与v2的点积: {np.dot(cross_product, v2):.2e}")
    print("（结果接近0表示垂直）")

# 示例1：基本的向量叉乘
v1 = np.array([1, 0, 0])  # i 方向的单位向量
v2 = np.array([0, 1, 0])  # j 方向的单位向量
print("\n示例1 - 单位向量叉乘:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
result1 = manual_cross_product(v1, v2)
print(f"v1 × v2 = {result1}")  # 应该得到 [0, 0, 1] (k 方向)

# 示例2：任意向量叉乘
v3 = np.array([2, 3, 4])
v4 = np.array([5, 6, 7])
print("\n示例2 - 任意向量叉乘:")
print(f"v3 = {v3}")
print(f"v4 = {v4}")
result2 = manual_cross_product(v3, v4)
print(f"v3 × v4 = {result2}")

# 打印叉乘的数学公式
print("\n向量叉乘的数学公式：")
print("对于向量 a = [a1, a2, a3] 和 b = [b1, b2, b3]")
print("a × b = [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1]")

# 示例3：几何性质分析
print("\n示例3 - 几何性质分析:")
v5 = np.array([3, 0, 0])  # 3倍的i方向单位向量
v6 = np.array([0, 4, 0])  # 4倍的j方向单位向量
print(f"v5 = {v5}")
print(f"v6 = {v6}")
result3 = manual_cross_product(v5, v6)
calculate_geometric_properties(v5, v6) 