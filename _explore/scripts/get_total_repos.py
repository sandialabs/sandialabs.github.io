"""
Count the total number of repositories being tracked and add to
index page and full catalog page
"""

import json
from os.path import abspath, dirname, join

# Get the root directory
rootDir = dirname(dirname(dirname(abspath(__file__))))
# Define affected files
datfilepath = join(rootDir, 'explore', 'github-data', 'labReposInfo.json')
jsfilepath = join(rootDir, 'js', 'focused-category-info.js')
indexfilepath = join(dirname(dirname(dirname(abspath(__file__)))), 'index.html')

# Read the repos info
with open(datfilepath, 'r') as f:
    contents = json.load(f)

# Count the unique repos
numberOfRepos = 0
for key in contents['data'].keys():
    numberOfRepos += 1


# HTML code for index.html
HTML = """---
title: Sandia Software Portal
layout: homepage
---

{% raw %}

<p class="page-title">Welcome to the Sandia National Laboratories software portal — a hub for our GitHub-hosted open source projects. <br />Our <a ng-click="categoryHref('ALL SOFTWARE')" style="cursor: pointer">full catalog</a> of numberOfRepos repositories is updated regularly as repositories are added or modified.</p>

<section class="flex-container" id="categories">
    <div ng-repeat="category in catData" class="flex-category dynamic" ng-click="categoryHref(category.title)">
        <img ng-src="{{ category.icon.path }}" style="width: 150px; height: 150px" alt="{{ category.icon.alt }}" />
        <h4>{{ category.title }}</h4>
        <p class="text-center">{{ category.description }}</p>

        <div ng-repeat="repo in topicRepos[catData.indexOf(category)]">
            <p class="links" ng-show="topicRepos[catData.indexOf(category)].indexOf(repo) < 4">
                <span>
                    <a href="https://github.com/{{ repo.ownerLogin }}" alt="View Owner on GitHub" title="Owner: {{ repo.ownerLogin }}">
                        <img class="orgAvatar" ng-src="{{ repo.ownerAvatar }}" />
                    </a>
                </span>

                <span>
                    <a href="{{ repo.gitUrl }}" alt="{{ repo.description || '[No Description]' }}" title="{{ repo.description || '[No Description]' }}">
                        {{ repo.name }}
                    </a>
                </span>

                <span>
                    <a href="{{ repo.gitUrl }}/stargazers" alt="Stargazers" title="Stargazers">
                        {{ repo.stars }} <span class="fa fa-star"></span>
                    </a>
                </span>

                <span>
                    <a ng-click="repoHref(repo.nameWithOwner); $event.stopPropagation();" alt="Rpo Info" title="Repo Info">
                        <span class="fa fa-info-circle"></span>
                    </a>
                </span>
            </p>
        </div>
        <a class="more" ng-if="topicRepos[catData.indexOf(category)].length > 4">...MORE</a>
    </div>
</section>

{% endraw %}

<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.8/angular.min.js"></script>
<script src="/js/app.js"></script>
<script src="/js/Category.service.js"></script>
<script src="/js/category-info.js"></script>
"""
HTML = HTML.replace('numberOfRepos', str(numberOfRepos))

# Overwrite index.html
with open(indexfilepath, 'w') as f:
    f.write(HTML)

# JS code for focused-category-info.json
js = """
angular.module('app', []).controller('gitHubDataController', [
    '$scope',
    '$http',
    '$window',
    '$location',
    function($scope, $http, $window, $location) {
        var getCategoryInfo = $http.get('../category/category_info.json', {
            cache: true
        });

        var getReposTopics = $http.get('/explore/github-data/labRepos_Topics.json', {
            cache: true
        });

        var getReposInfo = $http.get('/explore/github-data/labReposInfo.json', {
            cache: true
        });

        //function to sort repos in descending order of stars
        function sortByStars(array, key) {
            return array.sort(function(a, b) {
                var x = a[key];
                var y = b[key];
                return x > y ? -1 : x < y ? 1 : 0;
            });
        }

        //sort by alphabetical key
        function sortAlphabetically(array, key) {
            return array.sort(function(a, b) {
                var x = a[key].toLowerCase();
                var y = b[key].toLowerCase();
                return x < y ? -1 : x > y ? 1 : 0;
            });
        }

        //check if repo is tagged as one of the categories
        function containsTopics(catTopics, repoTopics) {
            if (catTopics.length == 0) {
                return true;
            }
            for (var i = 0; i < catTopics.length; i++) {
                if ($.inArray(catTopics[i], repoTopics) != -1) {
                    return true;
                }
            }
            return false;
        }

        $scope.orderProp = '-stars';

        $scope.showHamburger = false;

        getCategoryInfo.then(function(response) {
            var catsObj = response.data.data;
            $scope.cats = Object.keys(catsObj);
            $scope.catData = [];
            angular.forEach($scope.cats, function(value, key) {
                var data = catsObj[value];
                data['displayTitle'] = data.icon.alt;
                $scope.catData.push(data);
            });
            $scope.catData = sortAlphabetically($scope.catData, 'title');
            var complete = {
                title: 'ALL SOFTWARE',
                icon: {
                    path: '/assets/images/all_icon_sandia.svg',
                    alt: 'All Software'
                },
                description: 'Browse all numberOfRepos Sandia open source projects',
                displayTitle: 'All Software',
                topics: []
            };
            $scope.catData.unshift(complete);

            var other = {
                title: 'OTHER',
                icon: {
                    path: '/assets/images/other_sandia.svg',
                    alt: 'Other'
                },
                description: 'Other software packages',
                displayTitle: 'Other',
                topics: ['snl-other']
            };

            $scope.catData.push(other);

            var catTitle = $location.path().slice(1);

            //set selected index to whatever category is currently being displayed
            for (var c in $scope.catData) {
                var modified = $scope.catData[c].title.replace(/ /g, '');
                console.log('modified: ' + modified + ' catTitle: ' + catTitle);
                if (modified == catTitle) {
                    $scope.currentLocation = $scope.catData[c].title;
                    $scope.selectedIndex = $scope.catData.indexOf($scope.catData[c]);
                    console.log('selectedIndex: ' + $scope.selectedIndex);
                }
                if (catTitle == '') {
                    var index = $scope.catData.length - 1;
                    $scope.selectedIndex = index;
                    var result = $scope.catData[index].title.replace(/ /g, '');
                    $window.location.href = '../category#' + result;
                }
            }

            getReposTopics.then(function(response) {
                var reposObj = response.data.data;
                var allRepos = Object.keys(reposObj);
                $scope.topicRepos = [];
                var inCategory = true;
                for (var c in $scope.catData) {
                    var cat = $scope.catData[c];
                    var catRepos = [];

                    for (var r in reposObj) {
                        var repo = reposObj[r];
                        var topics = [];
                        for (var t in repo.repositoryTopics.nodes) {
                            var repoTopic = repo.repositoryTopics.nodes[t].topic.name;
                            topics.push(repoTopic);
                        }
                        var included = containsTopics(cat.topics, topics);
                        if (included) {
                            catRepos.push({ nameWithOwner: r });
                        }
                    }
                    $scope.topicRepos.push(catRepos);
                }

                getReposInfo.then(function(response) {
                    var reposInfoObj = response.data.data;

                    for (var repo in reposInfoObj) {
                        //reposInfoObj[repo] is the actual repo object
                        for (var j in $scope.topicRepos) {
                            //var category is array of objects
                            var category = $scope.topicRepos[j];
                            for (var count in category) {
                                // category[count] is a specific repo within a category
                                //if we find a repo that is included in the category repos, we save more info on it
                                if (category[count].nameWithOwner == reposInfoObj[repo].nameWithOwner) {
                                    //save only necessary data fields
                                    category[count]['name'] = reposInfoObj[repo].name;
                                    category[count]['description'] = reposInfoObj[repo].description;
                                    category[count]['ownerAvatar'] = reposInfoObj[repo].owner.avatarUrl;
                                    category[count]['owner'] = reposInfoObj[repo].owner.login;
                                    category[count]['stars'] = reposInfoObj[repo].stargazers.totalCount;
                                    category[count]['gitUrl'] = reposInfoObj[repo].url;
                                    category[count]['homepageUrl'] = reposInfoObj[repo].homepageUrl;
                                    if (reposInfoObj[repo].primaryLanguage) {
                                        category[count]['language'] = reposInfoObj[repo].primaryLanguage.name;
                                    } else {
                                        category[count]['language'] = '';
                                    }
                                    category[count]['forks'] = reposInfoObj[repo].forks.totalCount;
                                }
                            }
                        }
                    }
                    //sort categories by stars descending
                    for (var i in $scope.topicRepos) {
                        $scope.topicRepos[i] = sortByStars($scope.topicRepos[i], 'stars');
                    }
                });

                //create function for generating hash url for each repo
                $scope.repoHref = function(nametag) {
                    $window.location.href = '../repo#' + nametag;
                };

                //function to generate hash url for each category
                $scope.categoryHref = function(nametag) {
                    var result = nametag.replace(/ /g, '');
                    $window.location.href = '../category#' + result;
                };
            });
        });
    }
]);
"""

js = js.replace('numberOfRepos', str(numberOfRepos))

# Overwrite JS file
with open(jsfilepath, 'w') as f:
    f.write(js)
