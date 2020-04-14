<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}{% endblock %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
    <link rel="stylesheet" href="/static/style.css" />

    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <script>$(function(){$("#datepicker").datepicker({dateFormat:"yy-mm-dd"})});</script>
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
