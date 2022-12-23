```
$ ldd -v micropython
	linux-vdso.so.1 (0x00007ffce9a35000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f3c4c9b4000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f3c4c991000)
	libffi.so.7 => /lib/x86_64-linux-gnu/libffi.so.7 (0x00007f3c4c985000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f3c4c97f000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3c4c78d000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f3c4cbfd000)

	Version information:
	./micropython:
		libdl.so.2 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libdl.so.2
		libffi.so.7 (LIBFFI_CLOSURE_7.0) => /lib/x86_64-linux-gnu/libffi.so.7
		libffi.so.7 (LIBFFI_BASE_7.0) => /lib/x86_64-linux-gnu/libffi.so.7
		libpthread.so.0 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libpthread.so.0
		libm.so.6 (GLIBC_2.23) => /lib/x86_64-linux-gnu/libm.so.6
		libm.so.6 (GLIBC_2.29) => /lib/x86_64-linux-gnu/libm.so.6
		libm.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libm.so.6
		libc.so.6 (GLIBC_2.25) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.17) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libm.so.6:
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_PRIVATE) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libpthread.so.0:
		ld-linux-x86-64.so.2 (GLIBC_2.2.5) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
		libc.so.6 (GLIBC_2.7) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.3.2) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_PRIVATE) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libffi.so.7:
		libc.so.6 (GLIBC_2.14) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.7) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libdl.so.2:
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
		libc.so.6 (GLIBC_PRIVATE) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/x86_64-linux-gnu/libc.so.6
		libc.so.6 (GLIBC_2.2.5) => /lib/x86_64-linux-gnu/libc.so.6
	/lib/x86_64-linux-gnu/libc.so.6:
		ld-linux-x86-64.so.2 (GLIBC_2.3) => /lib64/ld-linux-x86-64.so.2
		ld-linux-x86-64.so.2 (GLIBC_PRIVATE) => /lib64/ld-linux-x86-64.so.2
    
$ ./micropython 
MicroPython v1.19.1-740-gbf49a087b-kaki5 on 2022-12-11; linux [GCC 9.4.0] version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>>
```
