#include <stdio.h>
#include <stdlib.h>


int get_line_number(FILE * reader)
{
    int n= 0;
    int temp1, temp2;
    int res;
    while (fscanf(reader,"%d %d\n",&temp1, &temp2)!=-1)
    {
        n++;
    }
    return n;
}

void get_values(FILE *reader, int tab1[], int tab2[], int nb_lines)
{
    for (int i=0;i<nb_lines;i++)
    {
        fscanf(reader,"%d %d\n",&tab1[i],&tab2[i]);
    }
}

int compare(const void* a, const void *b)
{
    return (*(int*)a - *(int*)b);
}

int main()
{
    FILE * reader = fopen("day1.txt","r");
    int nb_lines = get_line_number(reader);
    int tab1[nb_lines], tab2[nb_lines];
    rewind(reader);
    get_values(reader,tab1,tab2,nb_lines);
    qsort(tab1, nb_lines,sizeof(int),compare);
    qsort(tab2, nb_lines,sizeof(int),compare);
    int res = 0;
    for (int i=0;i<nb_lines;i++)
    {
        res += abs(tab1[i]-tab2[i]);
    }
    printf("Résultat = %d\n",res);
}