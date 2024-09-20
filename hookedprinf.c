#define _GNU_SOURCE
#include <stdio.h>
#include <stdarg.h>
#include <dlfcn.h>

// Define a function pointer for the original printf
static int (*original_printf)(const char *, ...) = NULL;

// Custom printf implementation
int printf(const char *format, ...) {
    if (!original_printf) {
        // Load the original printf function
        original_printf = dlsym(RTLD_NEXT, "printf");
    }

    // Call the original printf function
    va_list args;
    va_start(args, format);
    int result = original_printf("Hooked: ");
    result += original_printf(format, args);
    va_end(args);

    return result;
}
