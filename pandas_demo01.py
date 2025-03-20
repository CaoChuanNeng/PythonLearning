import pandas as pd

def merge_etf_close_prices(file_paths, output_file='merged_stock_prices.csv'):
    """
    读取多个 ETF CSV 文件，提取收盘价数据，并合并到一个 DataFrame 按日期对齐后保存。

    参数：
    file_paths (list): 包含多个 ETF CSV 文件路径的列表。
    output_file (str): 生成的合并 CSV 文件的保存路径，默认 'merged_stock_prices.csv'。

    返回：
    pandas.DataFrame: 合并后的 DataFrame，索引为日期，每列为不同 ETF 的收盘价。
    """

    # 创建一个空 DataFrame 用于存放合并数据
    df_all = pd.DataFrame()

    for path in file_paths:
        # 读取 CSV，解析日期，并设置 'date' 作为索引
        df = pd.read_csv(path, parse_dates=['date'], index_col='date')
        df = df.tail(50)

        # 提取 'close' 列（请确认你的 CSV 文件中收盘价列的名称）
        df = df[['close']].rename(columns={'close': path.split('\\')[-1].split('.')[0]})  # 以文件名命名列

        # 合并数据，确保不同 ETF 的数据日期可以对齐
        if df_all.empty:
            df_all = df
        else:
            df_all = df_all.join(df, how='outer')  # 使用外连接，保留所有日期数据

    # 按日期排序，确保数据时间序列正确
    df_all.sort_index(inplace=True)

    # 保存到 CSV 文件
    df_all.to_csv(output_file, encoding='utf-8-sig')

    return df_all


# 示例 ETF 数据路径
file_paths = [
    r'C:\\Users\\Administrator\\Desktop\\Quant_\\back_data\\bc_data\\ETF回测数据\\518880黄金ETF.csv',
    r'C:\\Users\\Administrator\\Desktop\\Quant_\\back_data\\bc_data\\ETF回测数据\\510300沪深300ETF.csv',
    r'C:\\Users\\Administrator\\Desktop\\Quant_\\back_data\\bc_data\\ETF回测数据\\513500标普500ETF.csv'
]

# 调用函数，合并数据并保存
df_result = merge_etf_close_prices(file_paths)

# 检查结果
print(df_result)
