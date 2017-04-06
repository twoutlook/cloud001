

  ddlResult=Array(
    {% for item in item_list %}

Array("{{ item.seq}}","{{ item.title}}"),
    {% endfor  %}
   )  ; 