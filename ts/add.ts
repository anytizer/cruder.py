{% extends "base.html" %}
{% block title %}Add - {table}{% endblock %}
{% block heading %}Add - {table}{% endblock %}

{% block content %}
    <div class='w3-container w3-pale-yellow w3-padding'>
        <a href="/{table}/list" class="w3-green w3-btn">Back</a>
    </div>

    <form name='add' action='/{table}/add/' method='post' onsubmit="document.getElementById('{table}-submit').disabled=true; return true;" autocomplete="off">

        {__htmls_add__}
        
        {__foreign__}

        <div class="w3-row w3-padding">
            <div class='w3-col l2'>&nbsp;</div>
            <div class='w3-col l10'>
                <input type="hidden" name="{pk_id}" value="{{ guid }}" />
                <input type="submit" id="{table}-submit" name="" value="Add" class="w3-green w3-btn" />
                <a href="/{table}">Cancel</a>
            </div>
        </div>
    </form>
{% endblock %}
