using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Torres_de_Hanoi
{
    class Pila
    {


        public Stack<Disco> torre = new Stack<Disco>();


        // public int Size { get; set; }
        /* TODO: Elegir tipo de Top
        public int Top { get; set; }
        public String Top { get; set; }        
        */
        /* TODO: Elegir tipo de Elementos
        public Disco[] Elementos { get; set; }
        public List<Disco> Elementos { get; set; }
        */

        /* TODO: Implementar métodos */

        public Pila()
        {
           
        }
     

        public int size()
        {
            return torre.Count;
        }

        public void push(Disco d)
        {
            torre.Push(d);
        }

        public Disco pop()
        {
            return torre.Pop();
        }                

        public int peek()
        {

            if(torre.Count == 0)
            {
                return 99;
            }
            return torre.Peek().getValor();
        }

        public bool isEmpty()
        {
            if(torre.Count == 0) {
                return true;
            }
            return false;
        }

    }//pila
}//torres
