using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Torres_de_Hanoi
{
    class Hanoi
    {
        /*TODO: Implementar métodos*/
        public void mover_disco(Pila a, Pila b)
        {
        
                if (a.peek() != 99)//si es 99 la pila esta vacia
                {
                    Disco movido = a.pop();
                    b.push(movido);
                }
    
            else
            {
                if (b.peek() != 99)//si es 99 la pila esta vacia
                {
                    Disco movido = b.pop();
                    a.push(movido);
                }
            }
           
        }//mover_disco

        //ini-->fin
        //ini-->aux
        //fin-->aux
        //ini-->fin
        //aux-->ini
        //aux-->fin
        //ini-->fin
        public int iterativo(int n, Pila inicial, Pila final, Pila auxiliar) 
        {
            var resultado = 0;
           // var contador = 0;

            if(n%2 != 0)//impar
            {
                for (var i = 0; i < n; i++)
                {
                    mover_disco(inicial, final);
                    mover_disco(inicial, auxiliar);
                    mover_disco(final, auxiliar);
                    //contador++;
                }//for
                
            }//if

            else//par
            {

                for (var i = 0; i < n; i++)
                {
                    mover_disco(inicial, auxiliar);
                    mover_disco(inicial, final);
                    mover_disco(auxiliar, final);
                }//for

            }//else
             
                         if(final.size() == 3 && final.peek() == 1)
                         {
                             resultado = 1;
                         }

                         return resultado;
                         
           // return contador;
        }

    }
}
