#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

int main() {
    // Shellcode for "Barbeapapa"
    unsigned char shellcode[] = 
        "\xeb\x1a"              // jmp short end
        "\x5e"                  // pop rsi
        "\x48\x31\xc0"          // xor rax, rax
        "\x88\x46\x0a"          // mov [rsi+10], al
        "\x48\x89\xf7"          // mov rdi, rsi
        "\x48\x83\xc6\x0b"      // add rsi, 11
        "\xb0\x01"              // mov al, 1 (syscall number for write)
        "\xb2\x0b"              // mov dl, 11 (length of the string)
        "\x0f\x05"              // syscall
        "\xb0\x3c"              // mov al, 60 (syscall number for exit)
        "\x48\x31\xff"          // xor rdi, rdi (exit code 0)
        "\x0f\x05"              // syscall
        "\xe8\xe1\xff\xff\xff"  // call start
        "Barbeapapa";           // The string to print

    // Allocate memory with execute permissions
    void *exec = mmap(0, sizeof(shellcode), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_ANON | MAP_PRIVATE, -1, 0);
    if (exec == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    // Copy shellcode to allocated memory
    memcpy(exec, shellcode, sizeof(shellcode));

    // Execute the shellcode
    ((void(*)())exec)();

    return 0;
}