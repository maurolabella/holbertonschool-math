#ifndef COMPLEX
#define COMPLEX

/**
 * struct Complex - complex number structure
 * @re: real component
 * @im: imaginary part
 */
typedef struct Complex
{
	double re;
	double im;
} complex;

int display_complex_number(complex x);

#include <stdio.h>

#endif
