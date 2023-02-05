#include <stdio.h>

#ifdef REALIZE_TEST

int main(){
    printf("testing...\n");
    return 0;
}

#else

#include "a/a.h"
#include "a/abc.h"
#include "b/b.h"
#include "a/d/d.h"

int main(){
    printf("%i\n", a(1)+b(1)+d(1)+abc(1));
    return 0;
}

#endif