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
// main()
// –––––––––––––––––––––––––––––––-
var a
var b
var c
porDos( 3 ) // pido calcular 2*3
.then( function( r ) { // cuando esté, entonces ...
a = r // guardo el resultado
return porDos( 4 ) // pido calcular 2*4
})
.then( function( r ) { // cuando esté, entonces ...
b = r // guardo el resultado
return porDos( 5 ) // pido calcular 2*5
})
.then( function( r ) { // cuando esté, entonces ...
c = r // guardo el resulatdo
return (a+b+c) // hago la suma de todo y devuelvo el valor
})
.then( function( total ) { // cuando esté, entonces ...
console.log( "total = " + total )
})
