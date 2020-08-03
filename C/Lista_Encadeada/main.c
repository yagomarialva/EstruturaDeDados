#include "lista.c"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    Lista* lista;
    lista = criarLista();
    lista = inserirLista(lista,10);
    lista = inserirLista(lista,20);
    lista = inserirLista(lista,5);
    lista = inserirLista(lista,2);
    verificaLista(lista);
    buscar(lista,10);
    imprimirLista(lista);
    lista = remover(lista,10);
    printf("===============================\n");
    imprimirLista(lista);
    return 0;

}
