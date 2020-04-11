<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
    <title>{% block title %}{% endblock %}</title>
</head>
<body class='w3-sand'>

    <div class='w3-container w3-blue'>
        <h1>Urgent Slicing - {% block heading %}{% endblock %}</h1>
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
