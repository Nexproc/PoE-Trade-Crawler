/**
 * Created by Nick on 6/3/16.
 */
poeTrade.directive('homePage', function () {
    return {
        restrict: 'E',
        scope: {},
        templateUrl: '/static/app/components/home-page/home-page.html',
        controller: ["$scope", 'Trade', function ($scope, Trade) {
            $scope.graphs = [];

            $scope.addGraph = function(){
                $scope.graphs.push((($scope.graphs[$scope.graphs.length - 1] || 0) + 1));
            };
        }]
    };
});
