bits 64

segment .data
	msg1 db "Enter a digit ", 0xA, 0xD
	len1 equ $- msg1

	msg2 db "Please enter a second digit ", 0xA, 0xD
	len2 equ $- msg2

	msg3 db "The sum is: "
	len3 equ $- msg3

segment .bss
	num1 resb 2
	num2 resb 2
	res resb 1

section .text
	global _start	;must be declared for using gcc

_start:
	mov eax, 4
	mov ebx, 1
	mov ecx, msg1
	mov edx, len1
	int 0x80

	mov eax, 3
	mov ebx, 0
	mov ecx, num1
	mov edx, 2
	int 0x80

	mov eax, 4
	mov ebx, 1
	mov ecx, msg2
	mov edx, len2
	int 0x80

	mov eax, 3
	mov ebx, 0
	mov ecx, num2
	mov edx, 2
	int 0x80

	mov eax, 4
	mov ebx, 1
	mov ecx, msg3
	mov edx, len3
	int 0x80

	; moving the first number to eax register and second number to ebx
	; and subtracting ascii '0' to convert it into a decmial number

	mov eax, [num1]
	sub eax, '0'

	mov ebx, [num2]
	sub ebx, '0'

	; add eax and ebx
	add eax, ebx
	; add '0' to convert the sum from decimal to ASCII
	add eax, '0'

	; storing the sum inmemory res
	mov [res], eax
	
	; print the sum
	mov eax, 4
	mov ebx, 1
	mov ecx, res
	mov edx, 1
	int 0x80

exit:
	mov eax, 1
	xor ebx, ebx
	int 0x80
