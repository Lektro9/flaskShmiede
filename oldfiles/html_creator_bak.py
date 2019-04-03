from Testcontent import Content, Karten_Content
import os
import codecs

THEMEN_DICT = Content()
KARTEN_DICT = Karten_Content()

vorlage = """{% set sidenav = "true" %}

{% extends "header.html" %}

{% block body %}

<div class="p-5">
{% include "sidebar.html" %}
	<div class="main">
	  <h1>{{aktThema}}</h1>
	  <p><a href="{{kartenURL}}">Klicke hier</a> für die Flashcards</p>
	  <p></p>
	  <p></p>
	  <p></p>
	</div>  
</div>
<script src="{{ url_for('static', filename='js/jquery-3.3.1.min.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.bundle.js') }}"></script>

{% endblock %}"""

vorlage_karten = """
{% set flashcard = "true" %}

{% extends "header.html" %}


{% block body %}
  <div class="container">
  
  <h1>{{aktThema}}</h1>
  <h2>{{aktFach}}</h2>
  
  <dl>
  {% for t in Kartei %}
    <card>
      <dt>
			{{t[0]}}
	  </dt>
      <dd>
			{{t[1]}}
	  </dd>
    </card>
   {% endfor %}	
  </dl>
  
   </div>
   
    <div  class="mx-auto" style="width: 200px;"><a href="/"><button type="button" class="btn btn-primary" >Zurück</button></a></div>
	
	<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>
	<script src='https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.js'></script>

	<script  src="{{ url_for('static', filename='js/index.js') }}"></script>
{% endblock %}

"""

for fach in THEMEN_DICT:
    path = "{}/".format(fach)
    print(path)
    for thema in THEMEN_DICT[fach]:
        subdic = path+"{}/".format(thema[0].replace("-", "_").replace(".", "_").replace(" ", "_"))
        if not os.path.exists(subdic):
            os.makedirs(subdic)
        print(subdic)
        print((thema[1]+".html").replace("/", ""))
        html_name = (thema[1]+".html").replace("/", "")
        karten_html_name = (thema[1]+"-karten.html").replace("/", "")
        with codecs.open("{}{}".format(subdic, html_name), 'w', 'utf-8') as f:
            f.write(vorlage)
            f.close()
        with codecs.open("{}{}".format(subdic, karten_html_name), 'w', 'utf-8') as f:
            f.write(vorlage_karten)
            f.close()
## für karten htmls einfach gleichzeitig mit "-karten.html" erstellen




        
