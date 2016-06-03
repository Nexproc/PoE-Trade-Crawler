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

    return request;
}]);