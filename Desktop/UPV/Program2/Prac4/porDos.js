// –––––––––––––––––––––––––––––––-
// R -> porDos() -> R (versión con promesa)
// –––––––––––––––––––––––––––––––-
function porDos( n ) {
var prom = new Promise( function( resolver, rechazar ) {
setTimeout( function () {
resolver( n*2 )
}, 300 )
})
return prom
} // ()
// –––––––––––––––––––––––––––––––-
// –––––––––––––––––––––––––––––––-
async function hacerUnaSuma () {
var a = await porDos( 3 ) // llamo a calcular 2*3 y espero
var b = await porDos( 4 ) // llamo a calcular 2*4 y espero
var c = await porDos( 5 ) // llamo a calcular 2*5 y espero
// Hago la suma de todo y devuelvo el valor.
// En realidad devuelve una promesa con el valor
// resuelto y guardado dentro
return (a+b+c)
} // ()
// –––––––––––––––––––––––––––––––-
// main()
// –––––––––––––––––––––––––––––––-
hacerUnaSuma().then( function( total ) {
console.log( " total = " + total )
})
