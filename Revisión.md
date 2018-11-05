v0.8

# Trabajo
En estos archivos se encuentra todo lo relacionado con el trabajo **"mis perris"**, incluye archivos en ***Python - JS - HTML/CSS, conjunto con bootstrap / frameworks.***

Para empezar (ubuntu):
* **python3 manage.py makemigrations**
* **python3 manage.py migrate**
* **python3 manage.py runserver**

si tienen problemas con la base de datos:

- **python3 manage.py flush** /luego **Yes**

Si están en windows, solo poner **'python manage.py -command-'** sin el *3*.

## Proyecto
Aquí se agregó todo lo relacionado con Django al iniciar: **Settings, urls.**

## Registro
En esta carpeta se encuentra el trabajo, vienen las migraciones para **Django**, los statics **(css)** y Templates **(html)**.  En la base (/) se encuentran los archivos necesarios para trabajar en Django

Los archivos base serán:

#### models.py
Las clases postulantes y Perro se encuentran definidas aquí. Casi todas se agregaron como CharField 100, se espera cambiar más adelante.

#### urls.py
Todos los paths (caminos) que tenemos creados en views.py

#### views.py 
Este archivo tiene las vistas y lo que se guardará en la base de datos. Entre ellas está el regstro, crear, crearperro, logins, etc.

### Static
Aquí estan todos los archivos necesarios para lo visual: Css / images / Js (para validar rut)
- en css están desde los bootstrap css hasta el estilo para la página web (html)
- en img están las fotos de los perros rescatados, adoptados y necesarios.
- en js están los validadores, por ejemplo: de edad: "el año de nacimiento debe ser menor a 2001".
```Javascript
$.validator.addMethod("minDate", function(value, element) {
    var curDate = new Date("2000-12-31");
    var inputDate = new Date(value);
    if (inputDate <= curDate)
        return true;
    return false;
}, "El año de nacimiento debe ser menor a 2001");
```

### Templates
Aqui van los archivos en **HTML**  como formularios, index, etc... se agregarán en próximas versiones.

Cualquier falla o falta, se agregará a la brevedad.



