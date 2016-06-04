/**
 * Created by Nick on 6/3/16.
 */
poeTrade.directive('homePage', function () {
    return {
        restrict: 'E',
        scope: {},
        templateUrl: '/portal/static/app/components/home-page/home-page.html',
        controller: ["$scope", 'Request', function ($scope, Request) {
            $scope.trade = {};
            $scope.tradeId = 1;

            $scope.getCurrentTrade = function (tradeId) {
                Request.getOneTrade(tradeId).then(function (response) {
                    $scope.trade = response.plain();
                });
            };

            (function init() {
                $scope.getCurrentTrade($scope.tradeId);
            })();
        }]
    };
});