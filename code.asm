section   .data
	G0 TIMES 3 DB 0
	P1 TIMES 1 DB 0


section .text
	global  _start


_start:
	mov    ecx, G0
	add    ecx, 2

	mov    ebx, 1
	and    ebx, 0
	mov    [ecx], ebx

	mov    ebx, 5
	add    ebx, 2
	mov    r8d, ebx

	mov    ecx, G0
	add    ecx, 1

	mov    edx, P1
	add    edx, 0

	mov    ebx, r8d
	add    ebx, [edx]
	mov    [ecx], ebx

_end:
	mov     ebx, 0
	mov     eax, 1
	int     80h
