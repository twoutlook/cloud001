{% extends 'projectnote/base_projectnote.html' %}
{% load bootstrap3 %}

{% block page_title %}
{{ page_title}}
{% endblock %}

{% block content %}


  ddlResult=Array(
    {% for item in item_list %}
      {% if item.seq == 0 %}
         Array("{{ item.seq}}","{{ item.title}}"),
      {% else %}
   		Array("{{ item.seq}}","({{ item.seq}}){{ item.title}}"),
      
      {% endif %} 

    {% endfor  %}
   )  ; <br>


    ddlSql=Array(
    {% for item in item_list %}
         "{{ item.sql}}",      
    {% endfor  %}
   )  ;  <br>

    ddlLbl=Array(
    {% for item in item_list %}
         Array({{ item.lbl_en}}),      
    {% endfor  %}
   )  ;  <br>




{% endblock %}
