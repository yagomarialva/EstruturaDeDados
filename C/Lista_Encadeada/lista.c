#include "lista.h"
#include <stdio.h>
#include <stdlib.h>


struct lista
{
   int info;
   struct lista*prox;
   
};

//criamos a lista, ela será vazia apontando para o espaço null
Lista* criarLista() {
   return NULL;
}

//funçao para inserir somente no inicio da lista
Lista* inserirLista(Lista*l, int i){
   Lista* novo = (Lista*)malloc(sizeof(Lista));
   novo->info = i;
   novo->prox = l;
   return novo;
}

void imprimirLista(Lista* l) {
   Lista* p;
   for ( p = l; p != NULL; p = p->prox)
   {
      printf("%d\n", p->info);
   }
   
}

int verificaLista(Lista* l){
   if (l == NULL)
   {
      printf("Lista vazia!\n");
      return 1;
   }else
   {
      printf("Lista não vazia!\n");
      return 0;
   }
}

Lista* buscar(Lista* l, int v) {
   Lista* p;
   for (p = l; p != NULL; p = p->prox)
   {
      if (p->info == v)
      {  
         printf("O numero %d está na lista\n", v);
      }
   } 
    
}

Lista* remover(Lista* l,int v){
   Lista* ant = NULL;
   Lista* p = l;

   while (p != NULL  && p->info != v)
   {
      ant = p;
      p = p->prox;
   }
   if (p == NULL)
    return l;

   if (ant == NULL)
   {
      l = p->prox;
   }else
   {
      ant->prox = p->prox;
   }
   free(p);
   return l;
}

void liberar(Lista* l){
   Lista* p = l;
   while(p !=l){
      Lista* t = p->prox;
      free(p);
      p = t;
   } 
}

int compara(Lista* l1, Lista* l2){
   Lista* p1 = l1;
   Lista* p2 = l2;

   while(p1 != NULL && p2 != NULL){
      if(p1->info != p2->info)
         return 0;
      p1 = p1->prox;
      p2 = p2->prox;   
   }
   return p1 == p2;
}
