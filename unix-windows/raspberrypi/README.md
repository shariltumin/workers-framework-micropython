# MicroPython for Raspberrypi

```
$ uname -a
Linux raspberrypi 4.19.97-v7l+ #1294 SMP Thu Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux

$ ldd -v micropython
	linux-vdso.so.1 (0xbeb4c000)
	/usr/lib/arm-linux-gnueabihf/libarmmem-${PLATFORM}.so => /usr/lib/arm-linux-gnueabihf/libarmmem-v7l.so (0xb6ef6000)
	libm.so.6 => /lib/arm-linux-gnueabihf/libm.so.6 (0xb6e5d000)
	libpthread.so.0 => /lib/arm-linux-gnueabihf/libpthread.so.0 (0xb6e33000)
	libffi.so.6 => /usr/lib/arm-linux-gnueabihf/libffi.so.6 (0xb6e1b000)
	libdl.so.2 => /lib/arm-linux-gnueabihf/libdl.so.2 (0xb6e08000)
	libc.so.6 => /lib/arm-linux-gnueabihf/libc.so.6 (0xb6cba000)
	/lib/ld-linux-armhf.so.3 (0xb6f0b000)
	libgcc_s.so.1 => /lib/arm-linux-gnueabihf/libgcc_s.so.1 (0xb6c8d000)

	Version information:
	./micropython:
		libdl.so.2 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libdl.so.2
		libc.so.6 (GLIBC_2.28) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.25) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.17) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6
		libm.so.6 (GLIBC_2.23) => /lib/arm-linux-gnueabihf/libm.so.6
		libm.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libm.so.6
		libpthread.so.0 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libpthread.so.0
	/usr/lib/arm-linux-gnueabihf/libarmmem-v7l.so:
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6
	/lib/arm-linux-gnueabihf/libm.so.6:
		ld-linux-armhf.so.3 (GLIBC_2.4) => /lib/ld-linux-armhf.so.3
		libc.so.6 (GLIBC_PRIVATE) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6
	/lib/arm-linux-gnueabihf/libpthread.so.0:
		ld-linux-armhf.so.3 (GLIBC_PRIVATE) => /lib/ld-linux-armhf.so.3
		ld-linux-armhf.so.3 (GLIBC_2.4) => /lib/ld-linux-armhf.so.3
		libc.so.6 (GLIBC_PRIVATE) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6
	/usr/lib/arm-linux-gnueabihf/libffi.so.6:
		ld-linux-armhf.so.3 (GLIBC_2.4) => /lib/ld-linux-armhf.so.3
		libgcc_s.so.1 (GCC_3.5) => /lib/arm-linux-gnueabihf/libgcc_s.so.1
		libc.so.6 (GLIBC_2.7) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6
	/lib/arm-linux-gnueabihf/libdl.so.2:
		ld-linux-armhf.so.3 (GLIBC_PRIVATE) => /lib/ld-linux-armhf.so.3
		ld-linux-armhf.so.3 (GLIBC_2.4) => /lib/ld-linux-armhf.so.3
		libc.so.6 (GLIBC_PRIVATE) => /lib/arm-linux-gnueabihf/libc.so.6
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6
	/lib/arm-linux-gnueabihf/libc.so.6:
		ld-linux-armhf.so.3 (GLIBC_2.4) => /lib/ld-linux-armhf.so.3
		ld-linux-armhf.so.3 (GLIBC_PRIVATE) => /lib/ld-linux-armhf.so.3
	/lib/arm-linux-gnueabihf/libgcc_s.so.1:
		libc.so.6 (GLIBC_2.4) => /lib/arm-linux-gnueabihf/libc.so.6

$ ./micropython
MicroPython v1.19.1-782-g699477d12-KaKi5 on 2022-12-23; linux [GCC 8.3.0] version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> from worker import task, MT
>>> 
