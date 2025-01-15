from typing import TypedDict

SignalDataMetaToken = TypedDict('SignalDataMetaToken', {
    'chain': str,
    'address': str,
    'creator_address': str,
    'symbol': str,
    'name': str,
    'decimals': int,
    'logo': str,
    'total_supply': int,
    'launchpad': str,
    'launchpad_status': str,
    'creation_timestamp': int,
})

SignalDataMetaSignal = TypedDict('SignalDataMetaSignal', {
    'signal_count': int,
    'first_time': int,
    'first_price': float,
    'max_price': float,
    'max_price_gain': float,
    'signal_tags': list[str],
    'token_level': str,
})

SignalDataMetaMetric = TypedDict('SignalDataMetaMetric', {
    'pair': str,
    'token_reserve': int,
    'price': float,
    'liquidity': float,
    'volume_24h': float,
    'market_cap': float,
    'holder_count': int,
    'top10_position': float,
})

SignalDataMetaSafeDetail = TypedDict('SignalDataMetaSafeDetail', {
    'is_mint_abandoned': int,
    'is_block_address': int,
})

SignalDataMetaSafe = dict[str, SignalDataMetaSafeDetail]

SignalDataMetaSocial = TypedDict('SignalDataMetaSocial', {
    'uri': str,
    'logo': str,
    'telegram': str,
    'discord': str, 
    'website': str,
    'description': str,
    'twitter': str,
})

SignalDataMeta = TypedDict('SignalDataMeta', {
    'tokens': dict[str, SignalDataMetaToken],
    'signals': dict[str, SignalDataMetaSignal],
    'metrics': dict[str, SignalDataMetaMetric],
    'safe_info': dict[str, SignalDataMetaSafe],
    'social_info': dict[str, SignalDataMetaSocial],
    'token_tags': dict[str, list[str]],
})

SignalDataResultMetaStrategyInfo = TypedDict('SignalDataResultMetaStrategyInfo', {
    'group_id': int,
    'group_name': str,
    'group_type': str, 
    'strategy_id': int,
    'user_id': int,
})

SignalDataResultMeta = TypedDict('SignalDataResultMeta', {
    'create_time': int,
    'deleted': bool,
    'id': str,
    'read': bool,
    'strategy_info': SignalDataResultMetaStrategyInfo,
})

SignalDataResultMonitorRecordTokenTradingStat = TypedDict('SignalDataResultMonitorRecordTokenTradingStat', {
    'fdv': float,
    'holders': int,
    'lastUpdateTime': int,
    'liquidity': float,
    'mkt_cap': float,
    'percent12h': float,
    'percent1h': float,
    'percent1m': float,
    'percent24h': float,
    'percent5m': float,
    'volume_12h': float,
    'volume_1h': float,
    'volume_1minutes': float,
    'volume_24h': float,
    'volume_5minutes': float,
    'volume_6h': float,
})

SignalDataResultMonitorRecordWalletStat = TypedDict('SignalDataResultMonitorRecordWalletStat', {
    'alias': str,
    'amount': str,
    'amount_origin': int,
    'last_trade_time': int,
    'price': str,
    'token': str,
    'token_symbol': str,
    'volume': str,
    'wallet': str,
})

SignalDataResultMonitorRecord = TypedDict('SignalDataResultMonitorRecord', {
    'chain': str,
    'last_price': float | None,
    'strategy_id': int,
    'swap': str,
    'token': str,
    'token_symbol': str,
    'token_trading_stat': SignalDataResultMonitorRecordTokenTradingStat,
    'user_id': int,
    'wallet_stats': list[SignalDataResultMonitorRecordWalletStat],
})

SignalDataResultMonitorData = TypedDict('SignalDataResultMonitorData', {
    'monitor_type': str,
    'record_data': SignalDataResultMonitorRecord,
    'unix_time': int,
    'version': str,
})

SignalDataResult = TypedDict('SignalDataResult', {
    '_id': str,
    'meta': SignalDataResultMeta,
    'monitor_data': SignalDataResultMonitorData,
})

SignalData = TypedDict('SignalData', {
    'meta': SignalDataMeta,
    'results': list[SignalDataResult],
    'next': str | None,
    'total': int,
})

SignalResponse = TypedDict('SignalResponse', {
    'code': int,
    'message': str,
    'data': SignalData
})

StoryData = TypedDict('StoryData', {
    '_id': str,
    'token': str,
    'story': str,
    'createdAt': str,
    'updatedAt': str,
    '__v': int
})

StoryResponse = TypedDict('StoryResponse', {
    'code': int,
    'message': str,
    'data': StoryData
})

SmartWalletDailyProfit = TypedDict('SmartWalletDailyProfit', {
    'datetime': int,
    'realized_profit_7d': float
})

SmartWalletTokenDitribute = TypedDict('SmartWalletTokenDitribute', {
    'pnl_lt_minus_dot5_num': int,
    'pnl_minus_dot5_0x_num': int,
    'pnl_lt_2x_num': int,
    'pnl_2x_5x_num': int,
    'pnl_gt_5x_num': int
})

SmartWallet = TypedDict('SmartWallet', {
    'chain': str,
    'wallet': str,
    'realized_profit_1d': float,
    'pnl_1d': float,
    'realized_profit_7d': float,
    'realized_profit_30d': float,
    'pnl_7d': float,
    'pnl_30d': float,
    'win_rate_7d': float,
    'win_rate_30d': float,
    'token_winrate_7d': float,
    'token_winrate_30d': float,
    'avg_buy_volume_7d': float,
    'avg_buy_volume_30d': float,
    'buy_times_7d': int,
    'sell_times_7d': int,
    'buy_times_30d': int,
    'sell_times_30d': int,
    'buy_volume_7d': float,
    'sell_volume_7d': float,
    'buy_volume_30d': float,
    'sell_volume_30d': float,
    'last_active_timestamp': int,
    'daily_profit': list[SmartWalletDailyProfit],
    'token_distribute': SmartWalletTokenDitribute,
    'is_new_recommend': bool,
    'generate_time': int
})

SmartWalletResponse = TypedDict('SmartWalletResponse', {
    'code': int,
    'description': str,
    'data': SmartWallet
})