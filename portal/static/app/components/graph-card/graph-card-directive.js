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
            $scope.currencies = [];
            $scope.buyCurrency = {};
            $scope.sellCurrency = {};
            $scope.currencyId2Name = {};
            $scope.categories = [];
            $scope.highTradeDifferences = [];
            $scope.tradeValues = {
                low: [],
                average: [],
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

            $scope.drawGraph = function () {
                new Highcharts.Chart({
                    chart: {
                        type: 'spline',
                        renderTo: $scope.cardId,
                        backgroundColor: '#fbfbfb'
                    },
                    title: {
                        text: 'Buying ' + $scope.sellCurrency.name + ' with ' + $scope.buyCurrency.name,
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
                            text: $scope.sellCurrency.name + 's for one ' + $scope.buyCurrency.name
                        },
                        plotLines: [{
                            value: 0,
                            width: 1,
                            color: '#808080'
                        }]
                    },
                    tooltip: {
                        valueSuffix: ' ' + $scope.sellCurrency.name + 's per ' + $scope.buyCurrency.name
                    },
                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle',
                        borderWidth: 0
                    },
                    series: [
                        {
                            name: 'High',
                            data: $scope.tradeValues.high,
                            zIndex: 3,
                            color: '#90ed7d'
                        },
                        {
                            name: 'Average',
                            data: $scope.tradeValues.average,
                            zIndex: 2,
                            color: '#e6ed7d'
                        },
                        {
                            name: 'Low',
                            data: $scope.tradeValues.low,
                            zIndex: 1,
                            color: 'black'
                        },
                        {
                            type: 'column',
                            name: 'High Trade Change',
                            data: $scope.highTradeDifferences,
                            zIndex: 0,
                            color: '#7dd4ed'
                        }
                    ]
                });
            };

            $scope.getIntervaleDifferencesOnLowTrades = function() {
                var previousValue;
                $scope.highTradeDifferences = _.reduce(
                    $scope.tradeValues.high,
                    function (arr, lowValue) {
                        if (!previousValue && previousValue !== 0) {
                            previousValue = lowValue;
                            arr.push(0);
                            return arr;
                        }
                        arr.push(lowValue - previousValue);
                        previousValue = lowValue;
                        return arr;
                    },
                    []
                );
            };

            $scope.populateGraphData = function (requests) {
                _.each(requests, function (request) {
                    var plain_request = request.plain();
                    _.each(Object.keys($scope.tradeValues), function (key) {
                        $scope.tradeValues[key].push(plain_request[key]);
                    });
                });
                $scope.getIntervaleDifferencesOnLowTrades();
                $scope.drawGraph();
            };

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
                    var hourOfDay = nextDate.getHours() % 12 || 12;
                    var morningOrAfternoon = amOrPm[Math.floor((nextDate.getHours() % 24) / 12)];
                    $scope.categories.push('' + hourOfDay + morningOrAfternoon);
                    tradeRequests.push(Trade.getTradesForHour($scope.buyCurrency.id, $scope.sellCurrency.id, nextDate));
                }
                // TODO: populate hours and generate graph after data is fetched
                tradeRequests.reverse();
                $scope.categories.reverse();
                $q.all(tradeRequests).then($scope.populateGraphData);
            };

            (function init() {
                Currency.getAllCurrencies().then(function (response) {
                    $scope.tradeValues = {
                        low: [],
                        average: [],
                        high: []
                    };
                    $scope.currencies = response.plain();
                    $scope.currencyId2Name = {};
                    // defaults to trading some random currency for Chaos Orbs
                    var randomCurrencyId = 4;
                    while (randomCurrencyId === 4) {
                        randomCurrencyId = Math.ceil(Math.random() * $scope.currencies.length);
                    }
                    _.each($scope.currencies, function(currency) {
                        if (currency.id === randomCurrencyId) {
                            $scope.buyCurrency = currency;
                        }
                        if (currency.name === 'Chaos Orb') {
                            $scope.sellCurrency = currency;
                        }
                        $scope.currencyId2Name[currency.id] = currency.name;
                    });
                    $scope.getHourTradesForDay();
                });
            })();

            $scope.switchCurrency = function () {
                $scope.tradeValues = {
                    low: [],
                    average: [],
                    high: []
                };
                $scope.getHourTradesForDay();
            };
        }]
    };
});
