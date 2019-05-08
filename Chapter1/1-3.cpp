#include <iostream>
#include <iomanip>
#include <cstdio>

union Converter { float d; unsigned int ull; };

int main() {
    Converter sum, tmp;
    int i = 0;
    while (i < 2097152) {
        i += 1;
        sum.d += 1.0 / i;
        /*
        if (tmp.ull == sum.ull) {
            std::cout << i << " " << sum.d << " 0x" << std::hex << sum.ull << std:: endl;
            break;
        }
        tmp = sum;
        */
        if (i > 2097132) {
            printf("%d %.10f 0x%x\n", i, sum.d, sum.ull);
        }
    }
}
