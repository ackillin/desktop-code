bits 64

section .text
	global _start

_start:
	mov rdx, len	;message length
	mov rcx, msg	;message to write to ecx
	mov rbx, 1	;file descriptior
	mov rax, 4	; sys call number
	int 0x80	; call kernel (maybe try syscall instead?)

; Second message ?
	mov rdx, 10	
	mov rcx, s2	; Save current stuff to s2
	mov rbx, 1	; file descriptior
	mov rax, 4	; write previous (sys_write)
	int 0x80	; call kernel (again, try syscall)

	mov rax, 1 
	int 0x80

section .data
msg db 'Displaying 9 stars', 0xa ;First message
len equ $ - msg	; length of message
s2 times 11 db '*'

