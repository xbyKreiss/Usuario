// leerFichero crea una promesa que tras un segundo lee  y devuelve el texto de un archivo
// -> Nombre Fichero
// -> leerFichero()
// -> Texto

function leerFichero(nombreArchivo) {
    var promesa = new Promise(function (resolver, rechazar) {
        setTimeout(function () {
            var fs = require("fs")
            fs.readFile(nombreArchivo, "utf8", function (err, contenido) {
                if (err) {
                    rechazar()
                }
                resolver(contenido)
            })
        }, 1000)

    })

    return promesa;
}

// escribir

function escribirFichero(nombreArchivo, contenido) {
    var promesa = new Promise(function (resolver, rechazar) {
        setTimeout(function () {
            var fs = require("fs")
            fs.writeFile(nombreArchivo, contenido, function (err) {
                if (err) {
                    rechazar()
                }
                resolver(contenido)
            })
        }, 1000)

    })

    return promesa;
}

async function concatenarFicheros(nombreOrigen1, nombreOrigen2, nombreDestino) {

    var contenidoFichero1 = await leerFichero(nombreOrigen1)
    var contenidoFichero2 = await leerFichero(nombreOrigen2)

    var contenido = contenidoFichero1 + contenidoFichero2
    var escribirFichero1 = await escribirFichero(nombreDestino,contenido)


    return (contenido)
}

concatenarFicheros("1.txt","2.txt","concatenarArchivos1y2.txt").then(function (contenido) {
    console.log(contenido);


})
