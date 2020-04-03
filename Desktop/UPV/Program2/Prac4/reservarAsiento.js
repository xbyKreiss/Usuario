// –––––––––––––––––––––––––––––––-
// –––––––––––––––––––––––––––––––-
var elAsiento = "nadie" // variable global (mala idea)
// –––––––––––––––––––––––––––––––-
// Texto -> cambiarNombre()
//
// Tras un intervalo, cambia el valor de la variable
// global (mala idea) elAsiento.
// –––––––––––––––––––––––––––––––-
function cambiarNombre( nombre ) {
  setTimeout( function () {
      console.log( " *** elAsiento es para: " + nombre + "***" )
      elAsiento = nombre
    }, 100 )
} // ()
// –––––––––––––––––––––––––––––––-
// Texto -> hacerReserva()
// colateralmente, cambia la variable global (mala idea)
// –––––––––––––––––––––––––––––––-
function hacerReserva( nombre ) {
  if ( elAsiento == "nadie" ) {
      cambiarNombre( nombre )
      return
    }
} // ()
// –––––––––––––––––––––––––––––––-
// main
// –––––––––––––––––––––––––––––––-
console.log( "Intento reservar para juan." )
console.log( "Como es el primero en reservar, el asiento ")
console.log( "debería ser para él" )
hacerReserva( "juan" )
console.log( "Intento reservar para pepe." )
hacerReserva( "pepe" )
//
// Sin embargo, al final, ¿qué vale elAsiento?
//
setTimeout( ()=>console.log("elAsiento finalmente es para "+elAsiento), 1000)
