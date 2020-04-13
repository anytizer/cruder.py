{% extends "base.html" %}
{% block title %}Details - {table}{% endblock %}
{% block heading %}Details - {table}{% endblock %}
{% block content %}
    <div class='w3-container w3-pale-yellow w3-padding'>
        <a href="/{table}/list" class="w3-green w3-btn">Back</a>
    </div>

    {detail_fields}

    <!-- @todo Extra Flags -->

    <div class="w3-container w3-pale-red w3-padding">
        <div class="w3-left">
            <a class='w3-btn w3-red' href="/{table}/edit/{{data.{pk_id}}}">Edit</a>
            {detail_extras}
        </div>
        <div class="w3-right">
            Are you sure? <a class='w3-btn w3-red' href="/{table}/delete/{{data.{pk_id}}}">Delete</a>
        </div>
    </div>

{% endblock %}
