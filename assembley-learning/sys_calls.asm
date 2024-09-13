bits 64

section .data				;Data segment start
	userMsg db 'Enter a number: '	;Ask the user to enter a number
	lenUserMsg equ $-userMsg
	dispMsg db 'You have entered: '	;Print out final thing
	lenDispMsg equ $-dispMsg

section .bss		; Unitialized data
	num resb 5

section .text		; Actual code segment
	global _start

_start:
	mov rax, 4
	mov rbx, 1
	mov rcx, userMsg
	mov rdx, lenUserMsg
	int 80h

	;Read and store user input
	mov rax, 3
	mov rbx, 2
	mov rcx, num
	mov rdx, 5	; 5 bytes(numer, 1 for sign)
	int 80h

	;Output the message 'The entered number is: '
	mov rax, 4
	mov rbx, 1
	mov rcx, dispMsg
	mov rdx, lenDispMsg
	int 80h

	; Output the number entered
	mov rax, 4
	mov rbx, 1
	mov rcx, num
	mov rdx, 5
	int 80h	

	; Exit the code
	mov rax, 1
	mov rbx, 0
	int 80h
