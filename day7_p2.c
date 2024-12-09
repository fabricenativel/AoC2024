#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

#define MSIZE 100
#define LINESIZE 500

struct equation
{
    uint64_t result;
    int size;
    uint64_t operands[MSIZE];
};
typedef struct equation equation;

equation read(FILE *reader)
{
    equation c;
    if (fscanf(reader, "%ld: ", &c.result) != 1)
    {
        c.size = 0;
        return c;
    }
    char buffer[LINESIZE];
    fgets(buffer, sizeof(buffer), reader);
    char *op = strtok(buffer, " ");
    int i = 0;
    while (op != NULL)
    {
        c.operands[i++] = atoi(op);
        op = strtok(NULL, " ");
    }
    c.size = i;
    return c;
}

void display(equation c)
{
    for (int i = 0; i < c.size; i++)
    {
        printf("%ld; ", c.operands[i]);
    }
    printf(" -> %ld\n", c.result);
}

bool endwith(uint64_t n, uint64_t m)
{
    while (m != 0)
    {
        if (n % 10 != m % 10)
        {
            return false;
        }
        n = n / 10;
        m = m / 10;
    }
    return true;
}

uint64_t concat(uint64_t n, uint64_t m)
{
    uint64_t k = 1;
    while (k <= m)
    {
        k = k * 10;
    }
    return k * n + m;
}

uint64_t cut(uint64_t n, uint64_t m)
{
    uint64_t k = 1;
    while (k <= m)
    {
        k = k * 10;
        n = n / 10;
    }
    return n;
}

bool check(equation c, int cop, uint64_t target)
{
    if (cop == 1)
        return ((target == c.operands[0] + c.operands[1] || target == c.operands[0] * c.operands[1] || target == concat(c.operands[0], c.operands[1])));
    bool addok = (target >= c.operands[cop]);
    bool multok = (target % c.operands[cop] == 0);
    bool concatok = endwith(target, c.operands[cop]);
    return (addok && check(c, cop - 1, target - c.operands[cop])) || (multok && check(c, cop - 1, target / c.operands[cop])) || (concatok && check(c, cop - 1, cut(target, c.operands[cop])));
}

int main()
{
    FILE *reader = fopen("day7.txt", "r");
    equation c;
    uint64_t res = 0;
    while (!feof(reader))
    {
        c = read(reader);
        if (c.size != 0 && check(c, c.size - 1, c.result))
        {
            res += c.result;
        }
    }
    printf("Réponse partie 2 = %ld\n", res);
}