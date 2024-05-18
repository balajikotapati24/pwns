from pwn import *
r=process("./chall_09")
#xor the byte with 0x69
execution = xor(b'=\x01',0x69)+b'\x00'
print(execution)
r.sendline(execution)
r.interactive()
r.close()
