/**
 * Created by Nick on 6/3/16.
 */
var poeTrade = angular.module('poeTradeApp', ['restangular']);

poeTrade.config(['$httpProvider', function ($httpProvider) {
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]);

poeTrade.config(["RestangularProvider", function (RestangularProvider) {
    RestangularProvider.setBaseUrl('/api/v1');
    RestangularProvider.setRequestSuffix(('/'));
}]);


poeTrade.run(['$window', "Restangular", function ($window, Restangular) {
    Restangular.setDefaultHeaders({
        'Content-Type': 'application/json'
    });
}]);

console.log('hey')
