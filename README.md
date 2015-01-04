the project is quite simple.

if you develop marionettejs with django. you can install the package and include js without too much effort.

just add the following setting

```python
INSTALLED_APPS = (
    'marionettejs',
)
```

and just include the template

```html

    {% include 'marionettejs.html' %}

```

belows are the content of marionettejs.html

```html
{% load staticfiles %}
{% if DEBUG %}
    <script src="{% static 'js/jquery.js' %}"></script>
    <script src="{% static 'js/csrf_token.js' %}"></script>
    <script src="{% static 'js/json2.js' %}"></script>
    <script src="{% static 'js/underscore.js' %}"></script>
    <script src="{% static 'js/backbone.js' %}"></script>
    <script src="{% static 'js/backbone.marionette.js' %}"></script>
{% else %}
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/csrf_token.js' %}"></script>
    <script src="{% static 'js/json2.js' %}"></script>
    <script src="{% static 'js/underscore.min.js' %}"></script>
    <script src="{% static 'js/backbone.min.js' %}"></script>
    <script src="{% static 'js/backbone.marionette.min.js' %}"></script>
{% endif %}
```
