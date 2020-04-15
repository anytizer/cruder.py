{% extends "base.html" %}
{% block title %}Edit - {table}{% endblock %}
{% block heading %}Edit - {table}{% endblock %}
{% block content %}

    <div class='w3-container w3-pale-yellow w3-padding'>
        <a href="/{table}/list" class="w3-green w3-btn">Back</a>
    </div>

    <form name='edit' action='/{table}/edit/{{data.{pk_id}}}/' method="post">
        {htmls_edit}
        <div class="w3-row w3-padding">
            <div class='w3-col l2'>
                &nbsp;
            </div>
            <div class='w3-col l10'>
                <input type="hidden" name="{pk_id}" value="{{data.{pk_id}}}" />
                <input type="submit" value="Edit" class="w3-green w3-btn" />
                <a href="/{table}/">Cancel</a>
            </div>
        </div>
    </form>
{% endblock %}
