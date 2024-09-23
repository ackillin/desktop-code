bits 64

segment .data
	msg1 db "Enter a digit ", 0xA, 0xD
	len1 equ $- msg1

	msg2 db "Please enter a second digit ", 0xA, 0xD
	len2 equ $- msg2

	msg3 db "The sum is: "
	len3 equ $- msg3

segment .bss
	num1 resq 4
	num2 resq 4
	res resq 2

section .text
	global _start	;must be declared for using gcc

_start:
	mov rax, 4	;Sys_Write
	mov rbx, 1	;Move to STD_OUT
	mov rcx, msg1
	mov rdx, len1
	int 0x80

	mov rax, 3	;Sys_Read (The user input)
	mov rbx, 0	;STD_IN
	mov rcx, num1
	mov rdx, 2
	int 0x80

	mov rax, 4
	mov rbx, 1
	mov rcx, msg2
	mov rdx, len2
	int 0x80

	mov rax, 3
	mov rbx, 0
	mov rcx, num2
	mov rdx, 2
	int 0x80

	mov rax, 4
	mov rbx, 1
	mov rcx, msg3
	mov rdx, len3
	int 0x80

	; moving the first number to rax register and second number to rbx
	; and subtracting ascii '0' to convert it into a decmial number

	mov rax, [num1]
	sub rax, '0'

	mov rbx, [num2]
	sub rbx, '0'

	; add rax and rbx
	add rax, rbx
	; add '0' to convert the sum from decimal to ASCII
	add rax, '0'

	; storing the sum inmemory res
	mov [res], rax
	
	; print the sum
	mov rax, 4
	mov rbx, 1
	mov rcx, res
	mov rdx, 1
	int 0x80

exit:
	mov rax, 1	;SYS_EXIT (1)
	xor rbx, rbx	;Quickly set to 0
	int 0x80
