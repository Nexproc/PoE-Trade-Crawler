module.exports = function(grunt) {
    grunt.initConfig({
        uglify: {
            options: {
                sourceMap: true
            },
            build: {
                files: {
                    "portal/static/compressed/all<%= grunt.template.today('yymmddHHMM') %>.min.js": [
                        'portal/static/assets/bower_components/angular/angular.js',
                        'portal/static/assets/bower_components/jquery/dist/jquery.js',
                        'portal/static/assets/bower_components/bootstrap/dist/js/bootstrap.js',
                        'portal/static/assets/bower_components/highcharts/highcharts.src.js',
                        'portal/static/assets/bower_components/angular-ui-router/release/angular-ui-router.js',
                        'portal/static/assets/bower_components/angular-route/angular-route.js',
                        'portal/static/assets/bower_components/underscore/underscore.js',
                        'portal/static/assets/bower_components/restangular/dist/restangular.js',
                        'portal/static/app/*.js',
                        'portal/static/app/common/*.js',
                        'portal/static/app/components/**/*.js'
                    ]
                }
            }
        },
        cssmin: {
            dist: {
                files: {
                    "portal/static/compressed/all<%= grunt.template.today('yymmddHHMM') %>.min.css": [
                        'portal/static/assets/bower_components/bootstrap/dist/css/bootstrap.min.css',
                        'portal/static/assets/bower_components/bootstrap/dist/css/bootstrap-theme.min.css',
                        'portal/static/assets/bower_components/font-awesome/css/font-awesome.min.css',
                        'portal/static/assets/css/poe_trade_ninja.css'
                    ]
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify'); // load the given tasks
    grunt.loadNpmTasks('grunt-contrib-cssmin'); // load the given tasks
    grunt.registerTask('default', ['uglify', 'cssmin']); // Default grunt tasks maps to grunt
};
