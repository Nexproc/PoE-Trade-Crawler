/**
 * Created by Nick on 6/4/16.
 */
poeTrade.directive('graphCard', function () {
    var runningGraphIds = 1;
    return {
        restrict: 'E',
        scope: {},
        templateUrl: '/portal/static/app/components/graph-card/graph-card.html',
        link: function (scope) {
            scope.cardId = 'graph' + runningGraphIds++;
        },
        controller: ['$scope', '$timeout', '$q', 'Currency', 'Trade', function ($scope, $timeout, $q, Currency, Trade) {
            $scope.cardDetails = "I'm a graph card.";
            $scope.currencies = [];
            $scope.buyCurrency = {};
            $scope.sellCurrency = {};
            $scope.categories = [];
            $scope.tradeValues = {
                low: [],
                medium: [],
                high: []
            };
            const months = [
                'Jan',
                'Feb',
                'March',
                'April',
                'May',
                'June',
                'July',
                'Aug',
                'Sept',
                'Oct',
                'Nov',
                'Dec'
            ];

            const days = [
                'Sun',
                'Mon',
                'Tues',
                'Wed',
                'Thurs',
                'Fri',
                'Sat'
            ];

            const amOrPm = [
                'am',
                'pm'
            ];


            $scope.getDayTradesForWeek = function () {
                $scope.categories = [];
                var tradeRequests = [];
                var now = new Date();
                for (var i = 0; i < 7; i++) {
                    var nextDate = new Date();
                    nextDate.setDate(now.getDate() - i);
                    tradeRequests.push(Trade.getTradesForDay($scope.buyCurrency.id, $scope.sellCurrency.id, nextDate));
                }
                $q.all(tradeRequests);
                // TODO: write callback function to populate days and hours
            };

            $scope.getDayTradesForMonth = function () {
                $scope.categories = [];
                var tradeRequests = [];
                var now = new Date();
                var daysInMonth = (new Date(now.getYear(), now.getMonth(), 0)).getDate;
                for (var i = 0; i < daysInMonth; i++) {
                    var nextDate = new Date();
                    nextDate.setDate(now.getDate() - i);
                    tradeRequests.push(Trade.getTradesForDay($scope.buyCurrency.id, $scope.sellCurrency.id, nextDate));
                }
                $q.all(tradeRequests);
            };

            $scope.getHourTradesForDay = function () {
                $scope.categories = [];
                var tradeRequests = [];
                var now = new Date();
                for (var i = 0; i < 24; i++) {
                    var nextDate = new Date();
                    nextDate.setHours(now.getHours() - i);
                    $scope.categories.push('' + (nextDate.getHours() % 12) + amOrPm[Math.floor(nextDate.getHours()/2)]);
                    tradeRequests.push(Trade.getTradesForHour($scope.buyCurrency.id, $scope.sellCurrency.id, nextDate));
                }
                // TODO: populate hours and generate graph after data is fetched
                $q.all(tradeRequests);
            };

            $scope.drawGraph = function () {
                new Highcharts.Chart({
                    chart: {
                        type: 'line',
                        renderTo: $scope.cardId
                    },
                    title: {
                        text: 'Graph Title',
                        x: -20
                    },
                    subTitle: {
                        text: 'Graph Subtitle'
                    },
                    xAxis: {
                        categories: $scope.categories
                    },
                    yAxis: {
                        title: {
                            text: 'Y-Axis Title'
                        },
                        plotLines: [{
                            value: 0,
                            width: 1,
                            color: '#808080'
                        }]
                    },
                    tooltip: {
                        valueSuffix: $scope.buyCurrency.name + " per " + $scope.sellCurrency.name
                    },
                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle',
                        borderWidth: 0
                    },
                    series: [
                        {
                            name: 'low',
                            data: $scope.tradeValues.low
                        },
                        {
                            name: 'med',
                            data: $scope.tradeValues.med
                        },
                        {
                            name: 'high',
                            data: $scope.tradeValues.high
                        }
                    ]
                });
            };

            (function init() {
                Currency.getAllCurrencies().then(function (response) {
                    $scope.currencies = response.plain();
                    $scope.sellCurrency = $scope.buyCurrency = $scope.currencies[0];
                    $scope.drawGraph();
                });
            })();

            $scope.switchCurrency = function () {
                console.log($scope.sellCurrency);
                return true
            }
        }]
    };
});