/**
 * Created by Nick on 6/3/16.
 */
poeTrade.config(['$stateProvider', '$urlRouterProvider', '$urlMatcherFactoryProvider', '$locationProvider', function ($stateProvider, $urlRouterProvider, $urlMatcherFactoryProvider, $locationProvider) {
    //remove # from urls
    $locationProvider.html5Mode(true);

    // allow trailing slashes
    $urlMatcherFactoryProvider.strictMode(false);


    $stateProvider
        .state('home', {
            url: '/home',
            template: '<home-page></home-page>',
            data: {
                pageTitle: 'HomePage'
            }
        })
    ;

    // default route
    $urlRouterProvider.otherwise('/home');
}]);