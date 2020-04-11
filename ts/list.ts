{% extends "base.html" %}
{% block title %}List - {table}{% endblock %}
{% block heading %}List - {table}{% endblock %}
{% block content %}

    <div class='w3-container w3-pale-yellow w3-padding'>
        <a href="/{table}/add" class="w3-green w3-btn">Add</a>
        <a href="/import/{table}/" class="w3-green w3-btn">Import</a>
        <a href="/export/{table}/" class="w3-green w3-btn">Download</a>
    </div>

    <table class="w3-table w3-bordered">
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
{% endblock %}

