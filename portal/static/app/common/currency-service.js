/**
 * Created by Nick on 6/4/16.
 */
poeTrade.factory('Currency', ['Request', '$q', function (Request, $q) {
    const currency = {};
    var currencyCache = {};

    currency.getAllCurrencies = function () {
        if (currencyCache.getAllCurrencies) {
            return $q.resolve(currencyCache.getAllCurrencies);
        }
        currencyCache.getAllCurrencies = {};
        return Request.getAllCurrencies().then(function (response) {
            currencyCache.getAllCurrencies = response;
            return response;
        });
    };

    return currency;
}]);