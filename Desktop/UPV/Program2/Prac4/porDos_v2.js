// –––––––––––––––––––––––––––––––-
// R -> porDos() -> R (versión con promesa)
// –––––––––––––––––––––––––––––––-
function porDos( n, callback ) {
var prom = new Promise( function( resolver, rechazar ) {
setTimeout( function () {
resolver( n*2 )
}, 1000 )
})
return prom
} // ()
// –––––––––––––––––––––––––––––––-
// main()
// –––––––––––––––––––––––––––––––-
var p = porDos( 3 )
p.then( function( a ) {
console.log( "el resultado de 2*3 es " + a )
})
