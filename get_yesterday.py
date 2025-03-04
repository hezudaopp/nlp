import numpy as np
from datetime import datetime, timedelta

def demonstrate_get_yesterday():
    """
    展示多种获取昨天日期的方法
    """
    # 方法1：使用datetime
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    print("方法1 - 使用 datetime:")
    print(f"今天: {today.strftime('%Y-%m-%d')}")
    print(f"昨天: {yesterday.strftime('%Y-%m-%d')}")
    
    # 方法2：使用NumPy
    np_today = np.datetime64('today')
    np_yesterday = np_today - np.timedelta64(1, 'D')
    
    print("\n方法2 - 使用 NumPy:")
    print(f"今天: {np_today}")
    print(f"昨天: {np_yesterday}")
    
    # 方法3：使用NumPy的business_day（工作日）
    np_business_yesterday = np_today - np.busday_offset(np_today, 1)
    
    print("\n方法3 - 使用 NumPy business_day:")
    print(f"今天: {np_today}")
    print(f"上一个工作日: {np_business_yesterday}")
    
    # 不同格式的显示
    print("\n不同格式的日期显示:")
    print(f"完整时间戳: {yesterday}")
    print(f"年-月-日: {yesterday.strftime('%Y-%m-%d')}")
    print(f"月/日/年: {yesterday.strftime('%m/%d/%Y')}")
    print(f"日-月-年: {yesterday.strftime('%d-%b-%Y')}")
    print(f"星期几: {yesterday.strftime('%A')}")

if __name__ == "__main__":
    demonstrate_get_yesterday() 