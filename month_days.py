import numpy as np
from datetime import datetime, timedelta
import calendar

def get_month_days(year=None, month=None):
    """
    获取指定月份的所有日期
    如果不指定年月，则使用当前年月
    """
    # 如果没有指定年月，使用当前年月
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().month
        
    # 方法1：使用datetime
    print(f"\n方法1 - 使用datetime获取{year}年{month}月的所有日期:")
    first_day = datetime(year, month, 1)
    num_days = calendar.monthrange(year, month)[1]
    days = [(first_day + timedelta(days=i)).strftime('%Y-%m-%d') 
            for i in range(num_days)]
    
    for i, day in enumerate(days, 1):
        print(f"{i:2d}日: {day} ({(first_day + timedelta(days=i-1)).strftime('%A')})")
    
    # 方法2：使用NumPy
    print(f"\n方法2 - 使用NumPy获取{year}年{month}月的所有日期:")
    # 创建日期范围
    start_date = np.datetime64(f'{year}-{month:02d}-01')
    dates = np.array([start_date + np.timedelta64(i, 'D') for i in range(num_days)])
    
    for i, date in enumerate(dates, 1):
        day_of_week = np.datetime64(date).astype(datetime).strftime('%A')
        print(f"{i:2d}日: {date} ({day_of_week})")
    
    # 方法3：获取工作日
    print(f"\n方法3 - 获取{year}年{month}月的所有工作日:")
    start_date = np.datetime64(f'{year}-{month:02d}-01')
    end_date = np.datetime64(f'{year}-{month:02d}-{num_days}')
    business_days = np.busday_count(start_date, end_date + np.timedelta64(1, 'D'))
    
    print(f"本月共有 {num_days} 天")
    print(f"其中工作日有 {business_days} 天")
    print(f"周末有 {num_days - business_days} 天")
    
    # 按周显示日历
    print(f"\n{year}年{month}月日历:")
    print(calendar.month(year, month))

def main():
    # 获取当前月份的日期
    print("当前月份:")
    get_month_days()
    
    # 获取指定月份的日期（例如：2024年2月）
    print("\n指定月份（2024年2月）:")
    get_month_days(2024, 2)

if __name__ == "__main__":
    main() 