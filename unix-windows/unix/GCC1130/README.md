```
$ ldd -v micropython
	linux-vdso.so.1 (0x00007ffc5f9a8000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f2b0ee7a000)
	libffi.so.8 => /lib/x86_64-linux-gnu/libffi.so.8 (0x00007f2b0ee6d000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2b0ec45000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f2b0f044000)

	Version information:
	./micropython:
		libffi.so.8 (LIBFFI_CLOSURE_8.0) => /lib/x86_64-linux-gnu/libffi.so.8
		libffi.so.8 (LIBFFI_BASE_8.0) => /lib/x86_64-linux-gnu/libffi.so.8
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.33) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.25) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.17) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.34) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
		libm.so.6 (GLIBC_2.23) => /lib/x86_64-linux-gnu/libm.so.6
		libm.so.6 (GLIBC_2.29) => /lib/x86_64-linux-gnu/libm.so.6
		libm.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libm.so.6
	/lib/x86_64-linux-gnu/libm.so.6:
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_PRIVATE) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libffi.so.8:
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.7) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.27) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libc.so.6:
		ld-linux-x86-64.so.2 (GLIBC_2.2.5) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
    
$ ./micropython 
MicroPython v1.19.1-764-g9bec52a2f-kaki5 on 2022-12-14; linux [GCC 11.3.0] version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> 
```
