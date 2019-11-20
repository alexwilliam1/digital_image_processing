#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int *histograma(int **imagem, int largura, int altura)
{
    int *hist = (int*) malloc(sizeof(int) * 256);

    for (int i = 0; i < 256; i++) {
        hist[i] = 0;
    }

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            int pixel = imagem[i][j];
            hist[pixel]++;
        }
    }
    return hist;
}

int main(int argc, const char * argv[]) 
{
    srand(time(NULL));
    int **imagem, largura = 500, altura = 500;

    imagem = (int**) malloc(sizeof(int*) * altura);

    for (int i = 0; i < altura; i++)
        imagem[i] = (int*) malloc(sizeof(int) * largura);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            imagem[i][j] = rand() % 256;
        }
    }
    
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            printf("%d ",imagem[i][j]);
        }
        printf("\n");
    }

    int *hist = histograma(imagem, largura, altura);

    for (int i = 0; i < 256; i++) {
        printf("O valor %d ocorreu %d vezes \n",i, hist[i]);
    }

    return 0;
}