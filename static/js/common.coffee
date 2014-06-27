

endaApp = angular.module(
    'endaApp',
    [
        'ngRoute','ngResource', 'ngSanitize', 'ui.bootstrap', 'ngDialog',
    ]
)

endaApp
# .config(
#     [
#         '$resourceProvider',
#         ($resourceProvider)->
#             $resourceProvider.defaults.stripTrailingSlashes = false
#     ]
# )
.config(
    [
        '$locationProvider', '$routeProvider',
        ($locationProvider, $routeProvider) ->
            $routeProvider.when(
                '/',
                    templateUrl: '/templates/home.html',
                    controller: 'HomeCtrl',
            ).when(
                '/candidates/',
                    templateUrl: '/templates/candidates.html',
                    controller: 'CandidateCtrl',
            ).when(
                '/candidates/:entry_number',
                    templateUrl: '/templates/candidates-each.html',
                    controller: 'CandidateEachCtrl',
            ).when(
                '/contest/',
                    templateUrl: '/templates/contest.html',
                    controller: 'ContestCtrl',
            ).when(
                '/vote/',
                    templateUrl: '/templates/vote.html',
                    controller: 'VoteCtrl',
            ).otherwise(
                redirectTo: '/'
            )

            $locationProvider.html5Mode(true)
    ]
)
.config(
    [
        '$httpProvider',
        ($httpProvider)->
            $httpProvider.defaults.headers.common = 'X-Requested-With': 'XMLHttpRequest'
    ]
)
.config(
    [
        '$interpolateProvider',
        ($interpolateProvider)->
            $interpolateProvider.startSymbol('{$')
            $interpolateProvider.endSymbol('$}')
    ]
)





endaApp.factory(
    'Candidate',
    [
        '$resource',
        ($resource)->
            return $resource(
                '/api/candidates/:id/', {}, {
                    'get': {method:'GET', isArray:false},
                }
            )
    ]
)

endaApp.factory(
    'Photo',
    [
        '$resource',
        ($resource)->
            return $resource(
                '/api/photos?candidate=:entry_number/', {}, {
                    'get': {method:'GET', isArray:false},
                }
            )
    ]
)


# endaApp.factory(
#     'Shared',
#     [
#         'Candidate',
#         ($resource)->
#             return {
#                 candidates = Candidate.get().results
#             }
#     ]
# )


endaApp.controller(
    'MainCtrl',
    [
        '$scope', 'Candidate', '$rootScope',
        ($scope, Candidate, $rootScope) ->
            Candidate.get((data)->
                candidates = data.results
                $rootScope.candidates = candidates
            )
            # $scope.bgClass = 'bg-home'
    ]
)


endaApp.controller(
    'NavCtrl',
    [
        '$scope', '$location',
        ($scope, $location)->
            $scope.isActive = (l)->
                l is $location.path()
    ]
)


endaApp.controller(
    'SocialCtrl',
    [
        '$scope', '$http',
        ($scope, $http)->
            $http.jsonp(
                'http://urls.api.twitter.com/1/urls/count.json?url=http://mshu2014.gallery/&callback=JSON_CALLBACK',
            ).success((data, status)->
                $scope.tweets = data.count
            )

            $http.jsonp(
                'https://graph.facebook.com/?id=http://mshu2014.gallery&callback=JSON_CALLBACK',
            ).success((data, status)->
                $scope.shares = data.shares
            )

            # $http.jsonp(
            #     'http://api.b.st-hatena.com/entry.count?url=http://mshu2014.gallery/&callback=JSON_CALLBACK',
            # ).success((data, status)->
            #     $scope.hatebu = data
            # )
    ]
)


endaApp.controller(
    'HomeCtrl',
    [
        '$scope',
        ($scope) ->
            $scope.$parent.bgClass = 'bg-home'

            $scope.$on(
                '$includeContentLoaded',
                (event)->
                    # $timeout(()->
                    $('.poem').addClass('poem-animate')
                    console.log('aa')
            )
    ]
)


endaApp.controller(
    'CandidateCtrl',
    [
        '$scope',
        ($scope)->
            $scope.$parent.bgClass = 'bg-other'
    ]
)


endaApp.controller(
    'VoteCtrl',
    [
        '$scope',
        ($scope)->
            $scope.$parent.bgClass = 'bg-other'
    ]
)


endaApp.controller(
    'ContestCtrl',
    [
        '$scope',
        ($scope)->
            $scope.$parent.bgClass = 'bg-other'
    ]
)


endaApp.controller(
    'CandidateEachCtrl',
    [
        '$scope', '$routeParams', '$window', 'ngDialog', 'Photo', 'Candidate', '$rootScope',
        ($scope, $routeParams, $window, ngDialog, Photo, Candidate, $rootScope) ->
            $scope.$parent.bgClass = 'bg-other'
            # $scope.toggle = ()->
            num = $routeParams.entry_number
            $scope.index = num - 1
            # candidates = data.results
            # $scope.candidate = $rootScope.candidates[num-1]
            Photo.get(
                {entry_number: num},
                (data)->
                    photos = data.results
                    $scope.photos = photos
            )
            $scope.OpenDialog = (url)->
                $scope.image_url = url
                ngDialog.open(
                    template: 'DialogTemplate'
                    scope: $scope
                )

            $scope.tinko = 'tinko'

            $scope.OpenMail = ()->
                name = $scope.candidates[num-1].name
                $window.location = "mailto:mshu2014.vote+#{num}@gmail.com?subject=エントリーNo.#{num} #{name}さんに投票する&body=このまま編集せずに送信してください"
    ]
)
