

  ddlResult=Array(
    {% for item in item_list %}
      {% if item.seq == 0 %}
         Array("{{ item.seq}}","{{ item.title}}"),
      {% else %}
   		Array("{{ item.seq}}","({{ item.seq}}){{ item.title}}"),
      
      {% endif %} 

    {% endfor  %}
   )  ; 


    ddlSql=Array(
    {% for item in item_list %}
         "{{ item.sql}}",      
    {% endfor  %}
   )  ; 

    ddlLbl_en=Array(
    {% for item in item_list %}
         Array({{ item.lbl_en}}),      
    {% endfor  %}
   )  ; 

        ddlLbl_zh=Array(
    {% for item in item_list %}
         "{{ item.lbl_zh}}",      
    {% endfor  %}
   )  ; 