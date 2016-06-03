/**
 * Created by Nick on 6/3/16.
 */
poeTrade.factory('Request', ["TradeApi", function (TradeApi) {
    const request = {};

    request.getAllTrades = function (tradeId) {
        return TradeApi.one('trade', tradeId).get()
    };

    return request;
}]);