#include"holberton.h"


/**
 * display_complex_number - compose and show complex
 * @x: receives a cmplx double struct
 * Return: int 1 or 0 in case of failure
 */
void display_complex_number(complex x)
{
	if (x.im != 0)
	{
		printf("%g+%gi\n", x.re, x.im);
		return (1);
	}
	else
	{
		printf("%.0f\n", x.re);
		return (1);
	}
}
