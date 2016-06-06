/**
 * Created by Nick on 6/4/16.
 */
poeTrade.factory('Trade', ['Request', function (Request) {
    const trade = {};

    trade.getTradesForHour = function (buyCurrencyId, sellCurrencyId, date) {
        return Request.getTradesForHour(buyCurrencyId, sellCurrencyId, date);
    };

    trade.getTradesForDay = function (buyCurrencyId, sellCurrencyId, date) {
        return Request.getTradesForDay(buyCurrencyId, sellCurrencyId, date);
    };

    trade.getOneTrade = function (tradeId) {
        return Request.getOneTrade(tradeId);
    };

    trade.getAllTrades = function () {
        return Request.getAllTrades();
    };

    return trade;
}]);