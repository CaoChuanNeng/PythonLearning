import numpy as np


def check_rebalance(prev_weights, curr_weights, method='L1', threshold=0.05):
    """
    计算资产权重偏离度，并判断是否需要调仓。

    :param prev_weights: dict, 上一期资产权重
    :param curr_weights: dict, 本期资产权重
    :param method: str, 'L1' 代表 L1 偏离度，'L2' 代表 L2 偏离度
    :param threshold: float, 触发调仓的阈值
    :return: (bool, float)，是否需要调仓，偏离度数值
    """
    if method == 'L1':
        deviation = sum(abs(curr_weights[k] - prev_weights[k]) for k in prev_weights)
    elif method == 'L2':
        deviation = np.sqrt(sum((curr_weights[k] - prev_weights[k]) ** 2 for k in prev_weights))
    else:
        raise ValueError("method 只能是 'L1' 或 'L2'")

    return deviation > threshold, deviation


# 示例：
previous_weights = {
    '518880黄金ETF': 0.6,
    '510300沪深300ETF': 0.2,
    '513500标普500ETF': 0.2
}

current_weights = {
    '518880黄金ETF': 0.61179,
    '510300沪深300ETF': 0.19759,
    '513500标普500ETF': 0.19062
}

# 调用函数检测是否需要调仓
rebalance, deviation = check_rebalance(previous_weights, current_weights, method='L1', threshold=0.05)
print(f"L1 偏离度: {deviation:.5f}, 是否需要调仓: {rebalance}")
