using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Torres_de_Hanoi
{
    class Disco
    {
        /*TODO: Decidir tipo de Valor
        public int Valor { get; set; }
        public String Valor { get; set; }
        */

        private int tamano;

        public Disco (int tam)
        {
            tamano = tam;
        }
        public void setValor(int tamano)
        {
            this.tamano = tamano;
        }

        public int getValor()
        {
            return this.tamano;
        }

    }//Disco
}//Torres
