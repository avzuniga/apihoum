Crear un servicio REST que:

- Permita que la aplicación móvil mande las coordenadas del Houmer
Para un día retorne todas las coordenadas de las propiedades que visitó y cuanto tiempo se quedó en cada una
Para un día retorne todos los momentos en que el houmer se trasladó con una velocidad superior a cierto parámetro


Explicacion de la solución:

- Un houmer es una persona que va a arrendar o comprar una casa y quiere visitar propiedades
- Un houmer advicer es una persona que se encarga de mostrar las propiedades y agendar las visitas

- El houmer abre su aplicacion movil y esta envia los datos de sus coordenadas al endpoint (POST de coordenadas) cada cierto tiempo, enviando latitud,longitud, su usuario y creando asi un timestamp cronologico de su ubicacion

- Al llegar a la propiedad el houmer advicer hace el checkin del houmer a la propiedad y esto marca el tiempo en el que llega. Asi mismo al terminar la visita marca como finalizada y se guarda el tiempo de checkout. La duracion de la visita es la diferencia entre el checkout-checkin.

- Para obtener las coordenadas y el tiempo exacto en el que la velocidad a la que se movio el houmer son superiores a un valor se filtran todas las coordenadas que estan en ese intervalo de tiempo (dia) De esta forma se va obteniendo velocidades parciales a las cuales el houmer se movio entre una coordenada y otra. 


Correr el proyecto:

- mysql is running with this setting: (Asegurese de crear una base de datos MYSQL local con esta configuración)

'DATABASE': 'houm',
'USER':'houm',
'PASSWORD':'houm',
'HOST': 'localhost',
'PORT': '3306'

- Cree un env y clone el proyecto

- pip install -r requirements.txt

- python makemigrations

- python migrate

- python manage.py runserver 8086

- python manage.py createsuperuser

Ahora vamos a probar la solución:
Para efectos de prueba los endpoints estan desprotegidos

Ve al admin y realiza los siguientes pasos:
http://127.0.0.1:8086/admin/

1. Cree un houmer
2. Cree un houmer advicer
3. Cree una propiedad 
4. Cree una o varias visitas y asignele la propiedad, houmer y houmer advicer previamente creado
5. Cree varias coordenadas
6. Asigne tiempo de checkin y checkout (Superior al checkin) a las visitas

Ahora realice con los datos creados las siguientes peticiones:

8. Use endpoint de obtener visitas con duracion de un houmer 
date YYYY-MM-DD
houmer str

GET
http://127.0.0.1:8086/api/v1/analitic/visit/obtein_visits/?houmer=username&date=2021-12-08

Response example
[
    {
        "property_id": 1,
        "property_title": "centro comercial viva",
        "visit_duration": 0.23055555555555557,
        "latitude": 11.0018294,
        "length": -74.8206108
    },
    {
        "property_id": 2,
        "property_title": "centro comercial plaza norte",
        "visit_duration": 0.21583333333333332,
        "latitude": 11.0018294,
        "length": -74.8206108
    }
]

9. Use endpoint de obtener momentos velocidad superior a la dada
date YYYY-MM-DD
houmer str
velocity str (km/h)

GET
http://127.0.0.1:8086/api/v1/analitic/coordinate/obtein_coordenates_velocity/?velocity=15&houmer=username&date=2021-12-08

Response example
[
    {
        "time_start": "2021-12-08T00:43:40.187401Z",
        "time_end": "2021-12-08T00:45:50.486241Z",
        "velocity": 34.65707363940047
    }
]


to run TEST
python manage.py test --verbosity 2