“Dame ideas para programar en Python usando tk” = De esta pregunta sacamos la idea de crear una agenda de contactos. 


1P Crea un código en Python sobre una agenda de contactos con tk que nos permita: 
Tener campos para nombre, apellidos, teléfono, correo y ubicación de la persona.
Ver la lista de contactos almacenados.
Poder agregar contactos o eliminarlos.

Este código nos da el problema de que no nos muestra la información guardada de las personas que hemos agregado así que habrá que formularle la siguiente pregunta. 

2P Añade a este código la opción de poder ver toda la información de las personas que agregamos. Además, dame otro botón para editar la información de los contactos ya agregados

Ahora que podemos acceder a la información de nuestros contactos, editarla y eliminarla vamos a hacer el código más exquisito con esta pregunta.


3P Ahora, prohíbe a los usuarios poner letras en el campo de teléfono y prohíbe poner letras en el campo de nombre, apellidos y correo. 

Para añadirle más detalle vamos a ponerle lo siguiente:

4P Añadele como predeterminado en cada campo lo siguiente:
1. Teléfono = +34 
2. Correo = @gmail.com
3. ubicación cambiale el nombre a “Dirección”

Ahora como en la clase fue mencionada que sea un tipo abstracto de dato se lo pediremos a la IA de la forma:

5P quiero que sea un tipo abstracto de dato

Nos hemos dado cuenta que el “+” predeterminado en el campo de teléfono nos da error porque no es un número así que vamos a editarlo para que lo acepte, además, haremos que los botones se ven en la misma posición horizontal y alineados. 

6P En el campo teléfono haz que él + también sea aceptado, además, haz que los botones estén alineados horizontalmente en la ventana.
Ahora para hacerlo más funcional,le pediremos a la IA que se nos agreguen los contactos únicamente dando al enter en el teclado y además añadiremos un botón de “salir” en la parte de abajo que nos permita cerrar la agenda de contactos y nos  salga una ventana que nos avise si estamos seguros. 


7P Agregame la opción de agregar el contacto dándole a la tecla enter del teclado, además, añade un botón que se llame “Salir” en la parte de abajo de la ventana en el lado derecho y que cuando sea seleccionado este botón se abra otra ventana que ponga “¿Estás seguro de que quieres salir de tu agenda de contactos?” con dos botones que pongan “Sí” (este cerrará las ventanas) y “No” (nos hará volver a la ventana de contactos).

Otro error que hemos visto es que los valores predeterminados no prevalecen cuando se crea un contacto, debemos hacer que estén 100% mantenidos en el campo cada vez que queramos agregar un contacto. Además vamos a agregarle color a la página pidiéndole que ponga colores de fondo.


8P Haz que el fondo de la ventana sea de color naranja pastel y las letras esten negrita y en letra monsterrat, haz que las letras con las que rellenos los campos salgan en color azul oscuro y en arial. Los botones también deben ser en montserrat. Además, haz que los valores predeterminados permanezcan en su campo sin borrarse cada vez que agreguemos a alguien.

Tenemos en cuenta que el valor predeterminado no funciona o no sabe ponerlo, y que además se agregó al nombre así que le pediremos que lo quite de ahí incluido del nombre de los campos.

9P Quita el +34 del campo de relleno de Nombre, también quita el (+34) de Teléfono y el (@gmail.com) de Correo en el nombre de los campos. 


Ahora aunque el modelo sea más simple es más útil, así que continuaremos a partir de esta base. Para hacerlo más visible le pediremos que cuando nos muestre su información lo haga desde otra ventana donde se vean todos los datos ordenados y en grande, además el apellido buscaremos que este dividido en dos campos y que el segundo campo de apellido sea opcional. 

10P Cuando el usuario le de a Ver Información haz que la información se vea ordenada en otra ventana aparte, además, quita el campo apellidos y pon “Primer Apellido” y “Segundo Apellido”, haz que ambos solo acepte letras y además el segundo deja que sea opcional.


Ahora vamos también a ponerle color a la ventana de ver información y vamos a hacer que los apartados como Nombre o Correo estén en negrita y se vean más grandes que los campos rellenados.

11P Haz que la ventana emergente de Ver Información tenga el fondo del mismo color que la agenda de contactos, además, haz que los títulos de los campos como Nombre o Correo están en negrita y aumentarles un poco el tamaño para que los campos rellenados se vean un poco más pequeños y se diferencie mejor. 


Al agregar estas funciones el teclado enter ya no funciona para agregar contactos así que habrá que volverlo a pedir, además sería genial hacer que se pueda bajar de los campos con las flechas del teclado una  vez la información sea rellenada. También el botón de salir deja de mostrarnos su ventana emergente de si estamos seguros. 

12P Añade al código que se pueda agregar contactos dándole a la tecla enter del teclado una vez los campos estén rellenados, además haz que se pueda bajar con las flechas del teclado entre los diferentes campos. También haz que salga una ventana emergente cada vez que le demos al botón de salir que diga “¿Estás seguro de que quieres salir de tu agenda de contactos?” y que tenga dos botones que pongan “Sí quiero” (cierra las ventanas) “No quiero” (Vuelve a la ventana de la agenda de contactos)


Los botones del teclado no funcionan así que eso no lo podemos devolver, además no salen los botones como si quiero y no quiero únicamente salen como si y no.
De esta forma la agenda de contactos estaría finalizada, pero si queremos hacer más podríamos pedirle datos adicionales cómo que nos deje organizarlo.

13P Ahora añade que se puedan organizar los contactos en “Amigos”, “Familiares” o “Otros” y que en otros se pueda especificar que son.
