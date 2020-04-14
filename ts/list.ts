{% extends "base.html" %}
{% block title %}List - {table}{% endblock %}
{% block heading %}List - {table}{% endblock %}
{% block content %}

    <div class='w3-container w3-pale-yellow w3-padding'>
        <form method="post" action="/{table}/search/">
            <a href="/{table}/add/" class="w3-green w3-btn">Add</a>
            <a href="/import/{table}/" class="w3-green w3-btn">Import</a>
            <a href="/export/{table}/" class="w3-green w3-btn">Download</a>

            <input type="submit" name="" value="Search" class="w3-green w3-btn" />
            <input type="text" name="query" value="" placeholder="Search..." />
        </form>

    </div>

    <form method="post" action="/{table}/bulk/">
    <table class="w3-table w3-bordered data">
    <thead>
        <tr>
            __THEADS__
            <th>Edit</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        {% for d in data %}
        <tr>
            __TBODY__
            <td><a href='/{table}/edit/{{ d.{pk_id} }}'>Edit<a></td>
            <td><a href='/{table}/details/{{ d.{pk_id} }}'>Details<a></td>
        </tr>
        {% endfor %}
    </tbody>
    </table>
    </form>
{% endblock %}

