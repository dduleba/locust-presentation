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

    Joe Friel - Triathlon biblia treningu

    * ~ 7 lat na doskonalenie umiejętności (aspekty fizyczne)
    * przez kolejne 3 lata lub więcej nadal poprawiają wyniki (aspekty psychiczne)
        * doświadczenie
        * znajomość reguł treningu
        * występowania w zawodach
        * tryb życia

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

Tworzenie virtualenv'a

.. code-block::

    $ pip install virtualenv
    $ pip install virtualenvwrapper
    $ mkvirtualenv -p python3 locust
    (locust)$

Instalacja

.. code-block::

    (locust)$ pip install locustio

Wczytanie virtualnego środowiska

.. code-block::

    $ source virtualenvwrapper.sh
    $ workon locust
    (locust)$ locust --help

oficjalna dokumentacja instalacji_

.. _instalacji: https://docs.locust.io/en/latest/installation.html

.. note::

    W razie problemów istnieją binarne paczki dla windows'a

----

Hello World!
=================

.. code-block:: python

    from locust import Locust, TaskSet, task

    class MyTaskSet(TaskSet):
        @task
        def my_task(self):
            print("executing my_task")

    class MyLocust(Locust):
        task_set = MyTaskSet
        min_wait = 5000
        max_wait = 15000

locust_local_url_

Dokumentacja locustfile_

.. _locustfile: https://docs.locust.io/en/stable/writing-a-locustfile.html

.. note::

    locustfile - zwykły plik pythonowy który musi zawierać przynajmniej jedną class'e dziedziczącą z class'y Locust

    Locust class - reprezentuje jednego urzytkownika - locust utworzy jedną instacje class'y dla każdego symulowanego urzytkownika

    task_set attribute - powinien wskazywać na klase TaskSet definiującą zachowanie urzytkownika

    min_wait and max_wait attribute - symuluje czas oczekiwania urzytkownika pomiędzy akcjiami [ms] - default value 1000

----

Hosts
=====

TODO: add content :)

----

Inny klient
===========

https://docs.locust.io/en/stable/testing-other-systems.html

----

Narzędzia
=========

Pythonowa szarańcza locust_

Zarządzanie virtualnymi środowiskami virtualenvwrapper_

Biblioteka do generowania prezentacji hovercraft_

.. _hovercraft: https://hovercraft.readthedocs.io/en/latest/presentations.html
.. _locust: https://locust.io/
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _locust_local_url: http://localhost:8089/
