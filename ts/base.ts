<!DOCTYPE html>
<html lang="en" ng-app="crud">
<head>
    <title>{% block title %}{% endblock %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
    <link rel="stylesheet" href="/static/style.css" />

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
    <!-- <script src="/static/jquery-3.5.0.min.js"></script> -->

    <!--
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <script>$(function(){$("#datepicker").datepicker({dateFormat:"yy-mm-dd"})});</script>

    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
    <script src="/static/controller.js"></script>
    -->
</head>
<body class='w3-sand'>

    <div class='w3-container w3-blue'>
        <h1>CRUD Panel - {% block heading %}{% endblock %}</h1>
    </div>

    <div id="menus" class="w3-padding w3-amber w3-bottombar w3-border-red">
        <div style="text-align: right;">
            {% include 'inc.menus.html' %}
        </div>
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>

    <div id="footer" class="w3-container w3-padding">
        &copy; 2020. All rights reserved.
    </div>
</body>
</html>
