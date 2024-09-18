bits 64

section .data
name db 'Zara Ali \n'

section .text
	global _start

_start:
	;writing the name 'Zara Ali'
	mov edx,9	;message length
	mov ecx, name	;message to write
	mov ebx, 1	;file descriptor (stdout)
	mov eax, 4
	int 0x80

	mov [name], dword 'Nuha'

	mov edx, 8	;change message length
	mov ecx, name	;message to write
	mov ebx, 1	
	mov eax, 4
	int 0x80


	mov eax, 1
	int 0x80

