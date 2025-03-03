import numpy as np

def show_numpy_info():
    """
    显示NumPy的版本和配置信息
    """
    print("NumPy 版本和基本信息")
    print("-" * 40)
    print(f"NumPy 版本: {np.__version__}")
    print(f"NumPy 安装路径: {np.__path__}")
    
    print("\nNumPy 配置信息")
    print("-" * 40)
    np.show_config()
    
    print("\nNumPy 编译信息")
    print("-" * 40)
    for key, value in np.__config__.__dict__.items():
        if not key.startswith('_'):
            print(f"{key}: {value}")
            
    print("\nNumPy 类型信息")
    print("-" * 40)
    print("可用的数据类型:")
    for type_name in sorted(dir(np)):
        if type_name.endswith(('64', '32', '16', '8')):
            print(f"- {type_name}")

if __name__ == "__main__":
    show_numpy_info() 