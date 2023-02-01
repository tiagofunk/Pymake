#include <stdio.h>

#include "a/a.h"
#include "b/b.h"
#include "a/d/d.h"

int main(){
    printf("%i\n", a(1)+b(1)+d(1));
    return 0;
}