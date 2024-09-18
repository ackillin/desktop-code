#!/bin/sh

nasm -f elf64 -o hello-linux.o -l hello-linux.lst adder.asm 
ld -static -o hello-linux hello-linux.o

echo "Run via ./hello-linux"
