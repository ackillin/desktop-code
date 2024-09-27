bits 64


section .data
    userMsg db 'Enter a number: '
    lenUserMsg equ $-userMsg

    even_msg db 'Even Number!', 0xA, 0xD
    len1 equ $-even_msg

    odd_msg db 'Odd_Number!', 0xA, 0xD
    len2 equ $-odd_msg
    
section .bss
    num resb 10

section .text
    global _start

_start:
    ;Get user input and then continue with regular code
    mov rax, 4
    mov rbx, 1
    mov rcx, userMsg    ;Asks user for data
    mov rdx, lenUserMsg
    int 0x80

    ;Read and Store input
    mov rax, 3
    mov rbx, 2
    mov rcx, num    ;Reads from rcx registry (see above)
    mov rdx, 10
    int 0x80

    
    mov eax, [num]
    sub eax, '0' ;Converts it to an int to compare
    and eax, 1   ;Compares last byte to 0001, takes "and" from that
    jz evnn     ;If it is 0 (is even) then jmp to "evnn"
    jmp oddd    ;Jump to odd (else clause)
    ; Start odd Section
    ;mov eax, 4
    ;mov ebx, 1
    ;mov ecx, odd_msg
    ;mov edx, len2
    ;int 0x80
    ;jmp outprog

evnn:
    mov eax, 4
    mov ebx, 1
    mov ecx, even_msg
    mov edx, len1
    int 0x80

    mov eax, 1
    int 0x80

oddd:
    mov eax, 4
    mov ebx, 1
    mov ecx, odd_msg
    mov edx,len2
    int 0x80

    mov eax,1
    int 0x80

