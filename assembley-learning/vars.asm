bits 64

section .data
multiple equ 10
stars times multiple dw 'blah '
len equ $-stars
second dw 'hello ', 0xa
len_2 equ $-second


section .text
	global _start

_start:
	mov edx, len
	mov ecx, stars
	mov ebx, 1
	mov eax, 4
	int 0x80

	mov ecx, second
	mov edx, len_2
	mov ebx, 1
	mov eax, 4
	int 0x80

	mov eax, 1
	int 0x80
