/**
 * Created by Nick on 6/3/16.
 */
poeTrade.factory('Request', ["TradeApi", function (TradeApi) {
    const request = {};

    request.getOneTrade = function (tradeId) {
        return TradeApi.one('trades', tradeId).get();
    };

    request.getAllTrades = function () {
        return TradeApi.one('trades').get();
    };

    request.getAllCurrencies = function () {
        return TradeApi.one('currencies').get();
    };

    request.getTradesForHour = function (buyCurrencyId, sellCurrencyId, date) {
        return TradeApi
            .one('trades')
            .one('trades_in_date_range')
            .get({
                startDate: date.toJSON(),
                rangeType: 'hour',
                buyCurrencyId: buyCurrencyId,
                sellCurrencyId: sellCurrencyId
            });
    };

    request.getTradesForDay = function (buyCurrencyId, sellCurrencyId, date) {
        return TradeApi
            .one('trades')
            .one('trades_in_date_range')
            .get({
                startDate: date.toJSON(),
                rangeType: 'day',
                buyCurrencyId: buyCurrencyId,
                sellCurrencyId: sellCurrencyId
            });
    };

    return request;
}]);