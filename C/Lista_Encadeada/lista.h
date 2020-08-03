typedef struct lista Lista;

//função para criar lista
Lista* criarLista();

//função para inserir elemento no inicio da lista
Lista* inserirLista(Lista* l, int i);

//função para imprimir elementos na lista
void imprimirLista(Lista* l);

//verifica se a lista é vazia
int verificaLista(Lista* l);

//busca elemento na lista
Lista* buscar(Lista* l, int v);

//remove elemento da lista
Lista* remover(Lista* l, int v);

//libera a lista
void liberar(Lista* l);

//compara duas listas
int compara(Lista* l1, Lista* l2);



