# Manejo de Ramas en Git

Git es una herramienta de control de versiones que permite a los usuarios crear, compartir y administrar proyectos a gran escala. Esto se logra a través de ramas, 
que son versiones separadas del proyecto principal. Estas ramas se pueden utilizar para desarrollar nuevas características, probar cambios, 
administrar versiones anteriores, etc.

A continuación se muestran algunos conceptos básicos al trabajar con ramas en Git:

## Crear una Rama

Para crear una nueva rama, utilice el comando `git branch` seguido del nombre de la rama. Por ejemplo, para crear una nueva rama llamada "mi-rama", 
utilice el siguiente comando:

git branch mi-rama


## Cambiar a una Rama

Una vez que haya creado una nueva rama, puede cambiar a ella utilizando el comando `git checkout`. 
Por ejemplo, para cambiar a la rama "mi-rama", utilice el siguiente comando:

git checkout mi-rama

## Fusionar Ramas

Para fusionar ramas, primero debe cambiar a la rama a la que desea fusionar los cambios. Luego, utilice el comando `git merge` seguido del nombre de la 
rama con los cambios que desea fusionar. Por ejemplo, para fusionar los cambios de la rama "mi-rama" en la rama actual, use el siguiente comando:

git merge mi-rama

## para las fusiones de ramas crear una pull request en github ##

crear una rama por funcionalidad y una vez finalizada la funcionalidad crear una pr para mergearlas a main
