:title: Pythonowa Szarańcza

.. :skip-help: true

:css: css/my.css


.. header::

    .. image:: img/logo.png
        :width: 209
        :height: 50


.. .. footer::

..    Pythonowa szarańcza - "Hello World"


----


Pythonowa Szarancza
===================


Dariusz Duleba


----

O mnie
======


rodzina
-------

    * 10 rok małżeństwa
    * 2 synów
        * Filip i Damian

praca
-----

    * 13 rok pracy
        * ALU (6+)
        * Genesys (5+)
        * Nokia (1+)

wolny czas
----------

    * jeszcze raz rodzina - masa atrakcji :)
    * sport
        * pływanie + jazda na rowerze + bieganie = triathlon
            * 3 starty
            * 3 rok treningów

.. note::
    Znaleść info o 10 latach w treningu triathlonowym

    W testach ile lat by nie minęło człowiek cały czas musi nabywać masę nowych doświadczeń

----

Reklama :)
==========

* Open source'owe narzędzie do testów wydajnościowych

* Umożliwia definicje zachowania użytkownika

* Scenariusze użytkownika w kodzie

.. image:: img/logo_python.gif

* Skalowalny
    * tysiące użytkowników na jednej maszynie (event-based)

* Rozporoszony
    * uruchomienie na wielu maszynach umożliwia symulowanie miliony równoczesnych użytkowników

* webowy interfejs

.. image:: img/www_screen.png
        :width: 400
        :height: 300

----

Instalacja
==========

W celu wyizolowania narzędzi testowego polecam virtualenv

.. code-block::

    $ pip install virtualenv
    $ pip install virtualenvwrapper
    $ mkvirtualenv -p python3 locust

https://docs.locust.io/en/latest/installation.html

.. code-block::

    $ workon locust
    (locust)$ pip install locustio
    (locust)$ locust --help

----

Inny klient
===========

https://docs.locust.io/en/stable/testing-other-systems.html

----

Narzędzia
=========

https://locust.io/

https://hovercraft.readthedocs.io/en/latest/presentations.html
