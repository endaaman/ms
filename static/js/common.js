var endaApp;

endaApp = angular.module('endaApp', ['ngRoute', 'ngResource', 'ngSanitize', 'ui.bootstrap', 'ngDialog']);

endaApp.config([
  '$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
    $routeProvider.when('/', {
      templateUrl: '/templates/home.html',
      controller: 'HomeCtrl'
    }).when('/candidates/', {
      templateUrl: '/templates/candidates.html',
      controller: 'CandidateCtrl'
    }).when('/candidates/:entry_number', {
      templateUrl: '/templates/candidates-each.html',
      controller: 'CandidateEachCtrl'
    }).when('/contest/', {
      templateUrl: '/templates/contest.html',
      controller: 'ContestCtrl'
    }).when('/vote/', {
      templateUrl: '/templates/vote.html',
      controller: 'VoteCtrl'
    }).otherwise({
      redirectTo: '/'
    });
    return $locationProvider.html5Mode(true);
  }
]).config([
  '$httpProvider', function($httpProvider) {
    return $httpProvider.defaults.headers.common = {
      'X-Requested-With': 'XMLHttpRequest'
    };
  }
]).config([
  '$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    return $interpolateProvider.endSymbol('$}');
  }
]);

endaApp.factory('Candidate', [
  '$resource', function($resource) {
    return $resource('/api/candidates/:id/', {}, {
      'get': {
        method: 'GET',
        isArray: false
      }
    });
  }
]);

endaApp.factory('Photo', [
  '$resource', function($resource) {
    return $resource('/api/photos?candidate=:entry_number/', {}, {
      'get': {
        method: 'GET',
        isArray: false
      }
    });
  }
]);

endaApp.controller('MainCtrl', [
  '$scope', 'Candidate', function($scope, Candidate) {
    return Candidate.get(function(data) {
      var candidates;
      candidates = data.results;
      return $scope.candidates = candidates;
    });
  }
]);

endaApp.controller('NavCtrl', [
  '$scope', '$location', function($scope, $location) {
    return $scope.isActive = function(l) {
      return l === $location.path();
    };
  }
]);

endaApp.controller('SocialCtrl', [
  '$scope', '$http', function($scope, $http) {
    $http.jsonp('http://urls.api.twitter.com/1/urls/count.json?url=http://mshu2014.gallery/&callback=JSON_CALLBACK').success(function(data, status) {
      return $scope.tweets = data.count;
    });
    $http.jsonp('https://graph.facebook.com/?id=http://mshu2014.gallery&callback=JSON_CALLBACK').success(function(data, status) {
      return $scope.shares = data.shares;
    });
    return $http.jsonp('http://api.b.st-hatena.com/entry.count?url=http://mshu2014.gallery/&callback=JSON_CALLBACK').success(function(data, status) {
      return $scope.hatebu = data;
    });
  }
]);

endaApp.controller('HomeCtrl', [
  '$scope', function($scope) {
    $scope.message = 'This is HOME not HOMO';
    return $scope.$parent.bgClass = 'bg-home';
  }
]);

endaApp.controller('CandidateCtrl', [
  '$scope', function($scope) {
    $scope.message = 'This is CandidateCtrl!';
    return $scope.$parent.bgClass = 'bg-other';
  }
]);

endaApp.controller('VoteCtrl', [
  '$scope', function($scope) {
    return $scope.$parent.bgClass = 'bg-other';
  }
]);

endaApp.controller('CandidateEachCtrl', [
  '$scope', '$routeParams', '$window', 'ngDialog', 'Photo', function($scope, $routeParams, $window, ngDialog, Photo) {
    var num;
    $scope.$parent.bgClass = 'bg-other';
    num = $routeParams.entry_number;
    $scope.candidate = $scope.$parent.candidates[num - 1];
    Photo.get({
      entry_number: num
    }, function(data) {
      var photos;
      photos = data.results;
      return $scope.photos = photos;
    });
    $scope.OpenDialog = function(url) {
      $scope.image_url = url;
      return ngDialog.open({
        template: 'DialogTemplate',
        scope: $scope
      });
    };
    return $scope.OpenMail = function() {
      var name;
      num = $scope.candidate.entry_number;
      name = $scope.candidate.name;
      return $window.location = "mailto:mshu2014.vote+" + num + "@gmail.com?subject=エントリーNo." + num + " " + name + "さんに投票する&body=このまま編集せずに送信してください";
    };
  }
]);
