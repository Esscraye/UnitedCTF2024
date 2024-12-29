section .text
    global _start

    _start:
        ; Pousser "apapa" sur la pile
        mov  rax, 0x7061707061    ; "apap"
        push rax
        mov  rax, 0x6170617061     ; "\n"
        push rax

        ; Configurer les registres pour l'appel système write
        mov  rdx, 0xa     ; longueur de la chaîne est de 10 octets
        mov  rsi, rsp     ; l'adresse de la chaîne est RSP car la chaîne est sur la pile
        mov  rax, 0x1     ; syscall 1 est write
        mov  rdi, 0x1     ; stdout a un descripteur de fichier de 1
        syscall           ; faire l'appel système

        ; Appel système exit pour terminer le programme proprement
        mov  rax, 60      ; syscall 60 est exit
        xor  rdi, rdi     ; code de retour 0
        syscall           ; faire l'appel système