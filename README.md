# Start2Impact Django&Redis project: SocialDex
Applicazione web che permette di scrivere articoli verificati tramite l'utilizzo della blockchain. 

#### Interfaccia grafica
1) Registrazione utente.
2) Possibilità di scrivere l'articolo
3) Lista utenti registrati con annessi articoli scritti
4) Hash & txId dei vari articoli scritti


## Framework e Tecnologie usate:
-[Django](https://docs.djangoproject.com/it/4.0/) - Back-end
-[Bootstrap] (https://getbootstrap.com/docs/5.1/getting-started/introduction/) - Front-end
-[Redis] (https://redis.io) - Server


## Setup progetto:
#### Configurazione virtual Environment:
```
progetto_dango_pierfrancesco_tripodi % virtualenv venv -p python3.9
progetto_dango_pierfrancesco_tripodi % source venv/bin/activate
(venv)progetto_dango_pierfrancesco_tripodi % pip install -r requirements.txt
```

## Avvio del progetto: 
```
progetto_dango_pierfrancesco_tripodi % cd social_dex
social_dex % python manage.py runserver
```
