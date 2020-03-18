using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Torres_de_Hanoi
{
    class Program
    {
        static void Main(string[] args)
        {

            Disco peque = new Disco(1);
            Disco medio = new Disco(2);
            Disco grande = new Disco(3); 

            Pila ini = new Pila();
            ini.push(grande);
            ini.push(medio);
            ini.push(peque);
            Pila aux = new Pila();
            Pila fin = new Pila();

            Hanoi nuevoHanoi = new Hanoi();
            //ini-->fin
            //ini-->aux
            //fin-->aux
            //ini-->fin
            //aux-->ini
            //aux-->fin
            //ini-->fin

            var res = nuevoHanoi.iterativo(7, ini, aux, fin);
            Console.WriteLine(res);


            var resultado0 = ini.peek();
            Console.WriteLine(resultado0);
            var resultado1 = aux.peek();
            Console.WriteLine(resultado1);
            var resultado2 = fin.peek();
            Console.WriteLine(resultado2);

            /*

            Console.WriteLine("-------------------");

            nuevoHanoi.mover_disco(ini, fin);
            nuevoHanoi.mover_disco(ini, aux);
            nuevoHanoi.mover_disco(fin, aux);
            nuevoHanoi.mover_disco(ini, fin);
            nuevoHanoi.mover_disco(aux, ini);
            nuevoHanoi.mover_disco(aux, fin);
            nuevoHanoi.mover_disco(ini, fin);

            var resultado0 = ini.peek();
           Console.WriteLine(resultado0);
            var resultado1 = aux.peek();
            Console.WriteLine(resultado1);
            var resultado2 = fin.peek();
            Console.WriteLine(resultado2);
            var resultado3 = fin.size();
            Console.WriteLine(resultado3);

    */

            // Keep the console window open in debug mode.
            Console.WriteLine("Press any key to exit.");
            Console.ReadKey();
        }//main
    }//program
}//torres
