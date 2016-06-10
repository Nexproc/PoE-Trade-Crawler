/**
 * Created by Nick on 6/4/16.
 */
poeTrade.factory('Trade', ['Request', '$q', function (Request, $q) {
    const trade = {};

    var tradesForHourCache = {};
    trade.getTradesForHour = function (buyCurrencyId, sellCurrencyId, date) {
        var cacheKey = '' + buyCurrencyId + sellCurrencyId + date.getHours();
        if (tradesForHourCache[cacheKey]) {
            return $q.resolve(tradesForHourCache[cacheKey]);
        }
        return Request.getTradesForHour(buyCurrencyId, sellCurrencyId, date)
            .then(function (response) {
                tradesForHourCache[cacheKey] = response;
                return response;
            });
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
