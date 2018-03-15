/*exemple C
fichier test.c
*/
#include "test.h"
__declspec(dllexport) int sum(int a, int b) {
    return a + b;
}
