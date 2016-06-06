/**
 * Created by Nick on 6/4/16.
 */
poeTrade.factory('Trade', ['Request', function (Request) {
    const trade = {};

    trade.getTradesForHour = function (buyCurrencyId, sellCurrencyId, time) {
        return Request.getTradesForHour(buyCurrencyId, sellCurrencyId, time);
    };

    trade.getTradesForDay = function (buyCurrencyId, sellCurrencyId, time) {
        return Request.getTradesForDay(buyCurrencyId, sellCurrencyId, time);
    };

    trade.getOneTrade = function (tradeId) {
        return Request.getOneTrade(tradeId);
    };

    trade.getAllTrades = function () {
        return Request.getAllTrades();
    };

    return trade;
}]);