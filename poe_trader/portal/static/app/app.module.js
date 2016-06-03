/**
 * Created by Nick on 6/3/16.
 */
var poeTrade = angular.module('poeTradeApp', ['restangular']);

poeTrade.config(['$httpProvider', function ($httpProvider) {
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]);

poeTrade.factory('TradeApi', ["Restangular", function (Restangular) {
    return Restangular.withConfig(function (RestangularConfigurer) {
        RestangularConfigurer.setBaseUrl('/api/');
        RestangularConfigurer.setRequestSuffix(('/'));
    });
}]);


poeTrade.run(['$window', "Restangular", "Request", function ($window, Restangular, Request) {
    Restangular.setDefaultHeaders({
        'Content-Type': 'application/json'
    });
    $window.myrequest = Request;
}]);
