

  ddlResult=Array(
    {% for item in item_list %}
      {% if item.seq == 0 %}
         Array("{{ item.seq}}","{{ item.title}}"),
      {% else %}
   		Array("{{ item.seq}}","({{ item.seq}}){{ item.title}}"),
      
      {% endif %} 

    {% endfor  %}
   )  ; 