Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # Python for Engineers, Part 2
>>> # Copyright (c) 2017 Raymond Hettinger
>>> 
>>> file
<type 'file'>
>>> help(file)
Help on class file in module __builtin__:

class file(object)
 |  file(name[, mode[, buffering]]) -> file object
 |  
 |  Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
 |  writing or appending.  The file will be created if it doesn't exist
 |  when opened for writing or appending; it will be truncated when
 |  opened for writing.  Add a 'b' to the mode for binary files.
 |  Add a '+' to the mode to allow simultaneous reading and writing.
 |  If the buffering argument is given, 0 means unbuffered, 1 means line
 |  buffered, and larger numbers specify the buffer size.  The preferred way
 |  to open a file is with the builtin open() function.
 |  Add a 'U' to mode to open the file for input with universal newline
 |  support.  Any line ending in the input file will be seen as a '\n'
 |  in Python.  Also, a file so opened gains the attribute 'newlines';
 |  the value for this attribute is one of None (no newline read yet),
 |  '\r', '\n', '\r\n' or a tuple containing all the newline types seen.
 |  
 |  'U' cannot be combined with 'w' or '+' mode.
 |  
 |  Methods defined here:
 |  
 |  __delattr__(...)
 |      x.__delattr__('name') <==> del x.name
 |  
 |  __enter__(...)
 |      __enter__() -> self.
 |  
 |  __exit__(...)
 |      __exit__(*excinfo) -> None.  Closes the file.
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __setattr__(...)
 |      x.__setattr__('name', value) <==> x.name = value
 |  
 |  close(...)
 |      close() -> None or (perhaps) an integer.  Close the file.
 |      
 |      Sets data attribute .closed to True.  A closed file cannot be used for
 |      further I/O operations.  close() may be called more than once without
 |      error.  Some kinds of file objects (for example, opened by popen())
 |      may return an exit status upon closing.
 |  
 |  fileno(...)
 |      fileno() -> integer "file descriptor".
 |      
 |      This is needed for lower-level file interfaces, such os.read().
 |  
 |  flush(...)
 |      flush() -> None.  Flush the internal I/O buffer.
 |  
 |  isatty(...)
 |      isatty() -> true or false.  True if the file is connected to a tty device.
 |  
 |  next(...)
 |      x.next() -> the next value, or raise StopIteration
 |  
 |  read(...)
 |      read([size]) -> read at most size bytes, returned as a string.
 |      
 |      If the size argument is negative or omitted, read until EOF is reached.
 |      Notice that when in non-blocking mode, less data than what was requested
 |      may be returned, even if no size parameter was given.
 |  
 |  readinto(...)
 |      readinto() -> Undocumented.  Don't use this; it may go away.
 |  
 |  readline(...)
 |      readline([size]) -> next line from the file, as a string.
 |      
 |      Retain newline.  A non-negative size argument limits the maximum
 |      number of bytes to return (an incomplete line may be returned then).
 |      Return an empty string at EOF.
 |  
 |  readlines(...)
 |      readlines([size]) -> list of strings, each a line from the file.
 |      
 |      Call readline() repeatedly and return a list of the lines so read.
 |      The optional size argument, if given, is an approximate bound on the
 |      total number of bytes in the lines returned.
 |  
 |  seek(...)
 |      seek(offset[, whence]) -> None.  Move to new file position.
 |      
 |      Argument offset is a byte count.  Optional argument whence defaults to
 |      0 (offset from start of file, offset should be >= 0); other values are 1
 |      (move relative to current position, positive or negative), and 2 (move
 |      relative to end of file, usually negative, although many platforms allow
 |      seeking beyond the end of a file).  If the file is opened in text mode,
 |      only offsets returned by tell() are legal.  Use of other offsets causes
 |      undefined behavior.
 |      Note that not all file objects are seekable.
 |  
 |  tell(...)
 |      tell() -> current file position, an integer (may be a long integer).
 |  
 |  truncate(...)
 |      truncate([size]) -> None.  Truncate the file to at most size bytes.
 |      
 |      Size defaults to the current file position, as returned by tell().
 |  
 |  write(...)
 |      write(str) -> None.  Write string str to file.
 |      
 |      Note that due to buffering, flush() or close() may be needed before
 |      the file on disk reflects the data written.
 |  
 |  writelines(...)
 |      writelines(sequence_of_strings) -> None.  Write the strings to the file.
 |      
 |      Note that newlines are not added.  The sequence can be any iterable object
 |      producing strings. This is equivalent to calling write() for each string.
 |  
 |  xreadlines(...)
 |      xreadlines() -> returns self.
 |      
 |      For backward compatibility. File objects now include the performance
 |      optimizations previously implemented in the xreadlines module.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  closed
 |      True if the file is closed
 |  
 |  encoding
 |      file encoding
 |  
 |  errors
 |      Unicode error handler
 |  
 |  mode
 |      file mode ('r', 'U', 'w', 'a', possibly with 'b' or '+' added)
 |  
 |  name
 |      file name
 |  
 |  newlines
 |      end-of-line convention used in this file
 |  
 |  softspace
 |      flag indicating that a space needs to be printed; used by print
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> 
>>> type(open)
<type 'builtin_function_or_method'>
>>> dir(open)
['__call__', '__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
>>> help(open)
Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object
    
    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

>>> 
>>> f = open('data/dialogue.txt')
>>> with f as f:
	print f.closed

	
False
>>> f.closed
True
>>> dir(file)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> 
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 17, in <module>
    print check_password('admin', 'cisco123')
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 12, in check_password
    return password[username] == password
TypeError: string indices must be integers, not str
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': 'cisco123'}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': 'pvfpb123'}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': 362038773434605591}
>>> 
>>> 2 ** 64
18446744073709551616L
>>> 
>>> 2 ** 32
4294967296
>>> 2 ** 31 - 1
2147483647
>>> 
>>> 
>>> 2 ** 32
4294967296
>>> 
>>> 2 ** 32 / (1e9)
4.294967296
>>> 
>>> 2 ** 64 / (1e9)
18446744073.709553
>>> 2 ** 64 / (1e9 * 60)
307445734.5618259
>>> 2 ** 64 / (1e9 * 60 * 60)
5124095.576030431
>>> 2 ** 64 / (1e9 * 60 * 60 * 24)
213503.98233460129
>>> 2 ** 64 / (1e9 * 60 * 60 * 24 * 365)
584.942417355072
>>> 2 ** 64 / (1e9 * 60 * 60 * 24 * 365 * 36)
16.248400482085334
>>> n_cpus = (64 + 16 * 2496)
>>> n_cpus
40000
>>> cores = n_cpus
>>> 2 ** 64 / (1e9 * 60 * 60 * 24 * 365 * cores)
0.014623560433876802
>>> 2 ** 64 / (1e9 * 60 * 60 * 24 * cores)
5.337599558365032
>>> 
>>> 
>>> hash('abc')
1453079729188098211
>>> hash('abd')
1453079729188098212
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 49, in <module>
    print check_password('admin', 'cisco123')
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 43, in check_password
    return passwords[username] == md5.hash(password).hexdigest()
AttributeError: 'module' object has no attribute 'hash'
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '07982c55db2b9985d3391f02e639db9c'}
>>> len('07982c55db2b9985d3391f02e639db9c')
32
>>> 16 ** 32
340282366920938463463374607431768211456L
>>> 16 ** 32 / (1e9 * 60 * 60 * 24 * cores)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    16 ** 32 / (1e9 * 60 * 60 * 24 * cores)
NameError: name 'cores' is not defined
>>> cores = (64 + 16 * 2496)
>>> 16 ** 32 / (1e9 * 60 * 60 * 24 * cores)
9.846133302110488e+19
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
>>> len('2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d')
128
>>> 16 ** 128
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096L
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> passwords
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
>>> len(rainbow)
10000
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
>>> passwords
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d', 'User010': '4e5206018e0e23a10771cae6ffcf563c5db89dfe996518a9f0255b41f1e56bf2fa64e6fe2e19d18849e5e7bf0f9a75d77fe204474da022f154b5d8882ab78f57', 'User011': '9c3d9dfcc101a3329288a6f76ce9e5b4426ca311f805e320fb434d5c13a2c9fcf9a00d2e4cbac2cc0946ef7659d1048f88b3ed470fb2551554f920d4aedab08b', 'User008': '11abd6f73130666a1e2356fad75c2a3ff3109c808786573c84b34751f4fb540b4cf6a66b01ce94eca68803a11199ac2ff01bf0e731d3f72ebb74a0376017787e', 'User009': '35fddd95911c6e8ced55b83b4dddcb9a06a2af8471d412ad7427878369d3d18bb7ac00ec561a41d819596540d2edf600df56376c906f49ff5c93d04c0c42546d', 'User004': 'ac853632a12ae128158fab24ce3a5472962826b026f1f43564a89d92af549ca77be6587381b637237387294dcbee069f8b3868fb2d2eae16c2f12a3412240fe5', 'User005': '1613d85b9cba61b0b468a580b0b1a42c555710e854f80f8d71b28d1d2d9ef6d8fd8fea2e483dbf905826868e93f3a2334e5c623f4996cbcbbb426bdb02009b09', 'User006': 'bc547750b92797f955b36112cc9bdd5cddf7d0862151d03a167ada8995aa24a9ad24610b36a68bc02da24141ee51670aea13ed6469099a4453f335cb239db5da', 'User007': 'e6c83b282aeb2e022844595721cc00bbda47cb24537c1779f9bb84f04039e1676e6ba8573e588da1052510e3aa0a32a9e55879ae22b0c2d62136fc0a3e85f8bb', 'User000': 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec', 'User001': '99adc231b045331e514a516b4b7680f588e3823213abe901738bc3ad67b2f6fcb3c64efb93d18002588d3ccc1a49efbae1ce20cb43df36b38651f11fa75678e8', 'User002': '9ad0d01d1766bb60025ba3403e851d1493a1ce2f14bdcf14d198f4a49e083f4547a6e5f9908444aad02d8d2383fbc74af021c7ee797ea13254c6603de76291b8', 'User003': 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86'}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
Gotcha! User004: cisco
Gotcha! User005: snoopy
Gotcha! User006: password1
Gotcha! User000: admin
Gotcha! User001: root
Gotcha! User002: superman
Gotcha! User003: password
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
Gotcha! User000: admin
Gotcha! User001: root
Gotcha! User002: superman
Gotcha! User003: password
Gotcha! User004: cisco
Gotcha! User005: snoopy
Gotcha! User006: password1
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '2fd8205b5e8f5463e6fe80bf132f4802045578ca04bd5357bf80c376c1968ba2871cf28417769c105c6db5f75c9ef14120c882de73e12ec615426bf402d3e31d'}
Gotcha! User000: admin
Gotcha! User001: root
Gotcha! User002: superman
Gotcha! User003: password
Gotcha! User004: cisco
Gotcha! User005: snoopy
Gotcha! User006: password1
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 67, in <module>
    salt = good_password()
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 65, in good_password
    return ''.join(random.choice(alphabet) for i in range(n))
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 65, in <genexpr>
    return ''.join(random.choice(alphabet) for i in range(n))
NameError: global name 'random' is not defined
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': '5a1f315b43496662c7ee2ded0df995fab7083410bfe7b33b70030469ce01a08f32ef5239d016c9d0b03b97e721437f2069c19a1834d7d0bcaec1bd2105a3641a'}
>>> salt
"P3n#,d'I^UoLR]!f8}':"
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': ('fb8fe057eaf89a84dccd0bd9751089a5aa5ac4f0eeb90cdc59758eb8698c948e4cf3ec415ff85c2a3c878a6b3ddeb8301b50f51e89d2cd023736a280c08c9f3a', 'ml?N?$^9CFyjlNc#@/)x')}
>>> passwords
{'admin': ('fb8fe057eaf89a84dccd0bd9751089a5aa5ac4f0eeb90cdc59758eb8698c948e4cf3ec415ff85c2a3c878a6b3ddeb8301b50f51e89d2cd023736a280c08c9f3a', 'ml?N?$^9CFyjlNc#@/)x'), 'User010': ('42f74a826dd62a6e0b9a84bd0869c0cc7057ce394c281c7cad523a6607e2df07a3e76e77d497ed6596df1d08f1e1dda2036b5817e69447024d3d3c865c35a91c', 'XpKcXQYs?wcoZbNSP_!m'), 'User011': ('caedb716ba7b19460d8614130a0755a2a5bba682e944edbdb97c9e588495d5aff6ddfad5fa4ed5a88521c5872eec08434d02118835ac0d9f2768e9379a23b857', 'cupoJ=pC(x&a*|x{?6|"'), 'User008': ('d9338addc54ef17faf142e6ab94902efc59a41554097321a1346e656f37cb8657fe26c1afc1f1b9dd27e0b22700bd1e0db6a8bf9934af3433bc6ebe451453559', 'VR&bF}z=1tp2AO5z?+"!'), 'User009': ('b691e3e91a76e53051a7cb16a367f4d3232db38950ea2deb8150c2edf149f8decace99aeded2dee14ce1538e837e189d5f2e576fa5dbf3758e23432bb49e5974', "N`[-[G||A?_r}!GH{'(."), 'User004': ('68a6b4d56249a3504b1bb2f9b6fddfd37db40e87e859552aea0c8357de1971f594ac3a7d0f21f60a87eb7151007e38b2299f6bd7ec0874707d248dbee7d7353a', 'gv{M}Wbh-Ay5hKb%+U[S'), 'User005': ('32394be0babd16af6d39d34eb25b8ac643576bffd6e20abf38db34ee4ac1c4d728f141e47f5392a853f00b350fbdabcacfefcf0a67b7713a65bf3a9ea61aff5b', ']9ywp3i}t{]X^S5NeXk1'), 'User006': ('d517d75a15066da84c0cf851fb24bb0cda976bd25b56fb10ab14f9b3dd59d9dc4fd12a4ff1e43e260ab4e9deca079a279aafd33fa002314076965028c2847f44', 'J9!q>!=xAmBLvQer[Rvh'), 'User007': ('27ac4e5115b0075b464caf647d90465df0a7dd8424333e11e170308110c97cf8d6fd9e2ec85a77fa6992846ccb7f60fd5c91f4fe35792073a91adbd0622f3975', ']q<G:7l^2`#a:)bJGan$'), 'User000': ('05f10b556b3bba6c14ac59313f0daddb2b2d3ab96b5bcf4276ae0550c47a5ae9f9baa3055ffbade9102c52c9d807d56fa41e2d0557b3b3ad40f376a05da8fffd', '{B6ao{TmG1V@Q/gE/3S,'), 'User001': ('62c7eb365d0467b1ce584041e2fa7cb997a8d917d77f604928d1a7d15cf0ec11a298987542aeb0e4d9f19bd0496f506fb4d004e5fdcc69529223399de238dfdb', 'P`EpXBipZ.{l}.g"Q;lp'), 'User002': ('bff79262ff48cf500d22c7250968113c63f2903afee3c1347c738d33c1c3bc409d7464b4854940e8af09b75c8b8cfb56b73801bb5e094e37a2af8193bf01f13d', 'aD{Fw)$3m%u"Lf3W+64!'), 'User003': ('263ca4d2a7f66cadc48ba1a6ab6b40275681e1698dc385fa7e3c3c411123aa164a0c743ebe3845720fc09acadbaf6b27975a9fb2709720ba899dd3078a61198f', '[S7%vw%FLTV8o6+]2nB5')}
>>> passwords['admin']
('fb8fe057eaf89a84dccd0bd9751089a5aa5ac4f0eeb90cdc59758eb8698c948e4cf3ec415ff85c2a3c878a6b3ddeb8301b50f51e89d2cd023736a280c08c9f3a', 'ml?N?$^9CFyjlNc#@/)x')
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': ('9032c7194c9ee233066ec9ab68f67aa3b629d58eac0903bca7ba14a37455d230a03df3e487e3f51103437c6ff5e661ee6610b956932040d1803de913034a8506', '-nH)]u5tErFsr#O\\JPk[')}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 93, in <module>
    print check_password('admin', 'cisco123')
  File "/Users/mike/teaching/2017-04-24/authentication.py", line 78, in check_password
    hashcode, salt = passwords[username]
ValueError: too many values to unpack
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': ('a97281834382b60f55c326a23b5801e53e85f6c83ceb3115632c32e7e734bde4d1e5359f93519291d4731b91e05b6c217e1d0746d33716ea0091ed53ab732968', '1-`fuAo\\dq=\\s(ciwN)t')}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': ('a4b116f0298a71c54ac1621001d0b7e2accc92fa354e131dfd978a9e72cad768026c5de28aefa887b26a41631adc0fb8bdba8927870d7535bfaabb0d127a7049', '.SL_jT;FenqG%R)!rIC(')}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': ('7de11cda4cde1149e624fffe06b3b36a541da919c7e24dc532083f21f4207a4468ae1ef0d5c38aa6db323ff75e7b2e161cdf320135b35e053aee8530ca8aa071', "7I1}4~'Th<,{|e[/TTs^")}
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/authentication.py =========
True
False
{'admin': ('9fd414088bf134544c7b8f7572fd8ac29544a026339990dfa5693e866da162db03daa1fea374fe07dfa2f2acad7cad5feff63937418db5cb046b79edb9a815a0', 'o",H!*7sms0E2`dxVOQm')}
>>> N

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    N
NameError: name 'N' is not defined
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> 5 == identity(5)
True
>>> 
>>> 
>>> 
>>> map(None, [1, 2, 3])
[1, 2, 3]
>>> 
>>> 
>>> map(identity, [1, 2, 3])
[1, 2, 3]
>>> 
>>> 
>>> 
>>> a = [10, 20]
>>> hex(id(a))
'0x10029d8c0'
>>> 
>>> b = identity(a)
>>> 
>>> hex(id(b))
'0x10029d8c0'
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> square
<function square at 0x1004fad70>
>>> square.__name__
'square'
>>> 
>>> sq = square
>>> square(5)
25
>>> sq(5)
25
>>> 
>>> map(square, [1, 2, 3])
[1, 4, 9]
>>> 
>>> identity(square)
<function square at 0x1004fad70>
>>> 
>>> square == identity(square)
True
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> map(square, [2, 4, 5])
[4, 16, 25]
>>> 
>>> sorted(['hello', 'mike'], key=len)
['mike', 'hello']
>>> 
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> identity(square)
<function square at 0x1004fad70>
>>> register(square)
<function square at 0x1004fad70>
>>> registry
{'square': <function square at 0x1004fad70>}
>>> 
>>> registry['square']
<function square at 0x1004fad70>
>>> registry['square'] == square
True
>>> registry['square'](5)
25
>>> square
<function square at 0x1004fad70>
>>> 
>>> 
>>> 
>>> registry
{'square': <function square at 0x1004fad70>}
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> 
>>> collatz(5)
16
>>> collatz(16)
8
>>> collatz(8)
4
>>> collatz(4)
2
>>> collatz(2)
1
>>> collatz(1)
4
>>> collatz(4)
2
>>> collatz(2)
1
>>> collatz(1)
4
>>> collatz(4)
2
>>> collatz(2)
1
>>> collatz(6)
3
>>> collatz(3)
10
>>> collatz(10)
5
>>> collatz(5)
16
>>> collatz(16)
8
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> conjecture(5)
True
>>> conjecture(6)
True
>>> all(conjecture(i) for i in xrange(100))

Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    all(conjecture(i) for i in xrange(100))
  File "<pyshell#139>", line 1, in <genexpr>
    all(conjecture(i) for i in xrange(100))
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture

=============================== RESTART: Shell ===============================
>>> all(conjecture(i) for i in xrange(10))

Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    all(conjecture(i) for i in xrange(10))
  File "<pyshell#140>", line 1, in <genexpr>
    all(conjecture(i) for i in xrange(10))
NameError: global name 'conjecture' is not defined
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> all(conjecture(i) for i in xrange(10))

Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    all(conjecture(i) for i in xrange(10))
  File "<pyshell#141>", line 1, in <genexpr>
    all(conjecture(i) for i in xrange(10))
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 45, in conjecture
    return conjecture(x)

=============================== RESTART: Shell ===============================
>>> all(conjecture(i) for i in xrange(1, 10))

Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    all(conjecture(i) for i in xrange(1, 10))
  File "<pyshell#142>", line 1, in <genexpr>
    all(conjecture(i) for i in xrange(1, 10))
NameError: global name 'conjecture' is not defined
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> all(conjecture(i) for i in xrange(1, 10))
True
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> all(conjecture(i) for i in xrange(1, 10))
True
>>> all(conjecture(i) for i in xrange(1, 100))
True
>>> all(conjecture(i) for i in xrange(1, 1000))
True
>>> all(conjecture(i) for i in xrange(1, 10000))
True
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> hardwork(5)
doing hard work!

Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    hardwork(5)
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 51, in hardwork
    time.sleep(1)
NameError: global name 'time' is not defined
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> hardwork(5)
doing hard work!
6
>>> hardwork(10)
doing hard work!
11
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> 
>>> register(power)
<function power at 0x100734de8>
>>> register(collatz)
<function collatz at 0x102f511b8>
>>> register(conjecture)
<function conjecture at 0x102f51848>
>>> registry
{'collatz': <function collatz at 0x102f511b8>, 'conjecture': <function conjecture at 0x102f51848>, 'power': <function power at 0x100734de8>}
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> collatz(5)
16
>>> 
>>> 
>>> registry
{'collatz': <function collatz at 0x1038511b8>, 'power': <function power at 0x102834de8>}
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> len(registry)
3
>>> square(5)
25
>>> 
>>> registry['collatz']
<function collatz at 0x1038641b8>
>>> registry['collatz'] == collatz
True
>>> registry['collatz'] is collatz
True
>>> 
>>> collatz
<function collatz at 0x1038641b8>
>>> 
>>> globals()['collatz']
<function collatz at 0x1038641b8>
>>> 
>>> registry
{'collatz': <function collatz at 0x1038641b8>, 'square': <function square at 0x1004fad70>, 'power': <function power at 0x1004fade8>}
>>> 
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> add_docstring(square)
<function square at 0x102834de8>
>>> square.__doc__
'unknown documentation'
>>> help(square)
Help on function square in module __main__:

square(x)
    unknown documentation

>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> help(collatz)
Help on function collatz in module __main__:

collatz(x)
    half or triple plus one

>>> help(power)
Help on function power in module __main__:

power(base, exponent)
    unknown documentation

>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> 
>>> 
>>> math.sin(0)
0.0
>>> math.sin(1)
0.8414709848078965
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> logging_sin(0)
calling sin
with 0
result was 0.0
0.0
>>> logging_sin(1)
calling sin
with 1
result was 0.841470984808
0.8414709848078965
>>> logging_sin(2)
calling sin
with 2
result was 0.909297426826
0.9092974268256817
>>> 
>>> 
>>> math.sqrt(4)
2.0
>>> math.sqrt(10)
3.1622776601683795
>>> 
>>> 1j
1j
>>> 1j ** 2
(-1+0j)
>>> 
>>> 
>>> math.sqrt(1)
1.0
>>> math.sqrt(-1)

Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    math.sqrt(-1)
ValueError: math domain error
>>> 
>>> 
>>> import cmath
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
>>> better_sqrt(4)
2.0
>>> better_sqrt(-4)
2j
>>> 
============= RESTART: /Users/mike/teaching/2017-04-24/theirs.py =============
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5.0, 4.0]
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========

Traceback (most recent call last):
  File "/Users/mike/teaching/2017-04-24/decorators.py", line 42, in <module>
    print theirs.sqrts([4, 81, -25, 16])
  File "/Users/mike/teaching/2017-04-24/theirs.py", line 13, in sqrts
    return [math.sqrt(x) for x in numbers]
ValueError: math domain error
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> pow2(5)
25
>>> 
>>> 
>>> def foo():
	x = 5
	return x

>>> foo()
5
>>> def foo():
	x = 5
	import math
	return math

>>> foo()
<module 'math' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so'>
>>> 
>>> def foo():
	x = 5
	import math
	class Bar:
		pass
	return Bar

>>> foo()
<class __main__.Bar at 0x10045f390>
>>> 
>>> def foo():
	x = 5
	import math
	class Bar:
		pass
	def baz():
		pass
	return baz

>>> foo()
<function baz at 0x1030e4c08>
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> 
>>> make_pow(3)
<function power at 0x102f51c80>
>>> pow3 = make_pow(3)
>>> pow3(5)
125
>>> pow4 = make_pow(4)
>>> pow4(2)
16
>>> make_pow
<function make_pow at 0x100634b18>
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> 
>>> powers[50]
<function power at 0x102858ed8>
>>> powers[50](2)
1125899906842624
>>> powers[16](2)
65536
>>> powers[8](2)
256
>>> 
>>> powers[8]
<function power at 0x102851aa0>
>>> 
>>> 
>>> pow8 = make_pow(8)
>>> pow8(2)
256
>>> 
>>> pow16 = make_pow(16)
>>> pow8.__closure__
(<cell at 0x10262ffd8: int object at 0x10030b7a0>,)
>>> pow8.__closure__[0].cell_contents
8
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> logging_cos(0)
calling cos
with 0
result was 1.0
1.0
>>> logging_cos(1)
calling cos
with 1
result was 0.540302305868
0.5403023058681398
>>> 
>>> 
>>> dir(math)
['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> logging_sqrt = make_logging(math.sqrt)
>>> logging_sqrt(3)
calling patch_sqrt
with 3
result was 1.73205080757
1.7320508075688772
>>> 
>>> power(5, 3)
125
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> power(5, 3)
125
>>> 
>>> logging_power = make_logging(power)
>>> logging_power(5, 3)
calling power
with (5, 3) {}
result was 125
125
>>> 
>>> 
>>> 
>>> power = make_logging(power)
>>> power(5, 3)
calling power
with (5, 3) {}
result was 125
125
>>> 
>>> 
>>> collatz(5)
16
>>> collatz = make_logging(collatz)
>>> collatz(5)
calling collatz
with (5,) {}
result was 16
16
>>> 
>>> conjecture(5)
calling collatz
with (5,) {}
result was 16
calling collatz
with (16,) {}
result was 8
calling collatz
with (8,) {}
result was 4
calling collatz
with (4,) {}
result was 2
calling collatz
with (2,) {}
result was 1
True
>>> 
>>> collatz.__closure__[0].cell_contents
<function collatz at 0x1038f1c08>
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> 
>>> collatz(5)
calling collatz
with (5,) {}
result was 16
16
>>> collatz
<function logging_wrapper at 0x103071c80>
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> collatz
<function collatz at 0x10285ec80>
>>> collatz.__closure__[0].cell_contents
<function collatz at 0x10285ec08>
>>> 
>>> 
>>> collatz(5)
calling collatz
with (5,) {}
result was 16
16
>>> collatz(5)
calling collatz
with (5,) {}
result was 16
16
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> 
>>> collatz(5)
calling collatz
with (5,) {}
result was 16
16
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
=========== RESTART: /Users/mike/teaching/2017-04-24/decorators.py ===========
[2.0, 9.0, 5j, 4.0]
>>> 
>>> 
>>> 
>>> make_logging(math.tan)(0)
calling tan
with (0,) {}
result was 0.0
0.0
>>> 
>>> math.tan = make_logging(math.tan)
>>> math.tan(0)
calling tan
with (0,) {}
result was 0.0
0.0
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> 
>>> 
>>> tick()

Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    tick()
  File "/Users/mike/teaching/2017-04-24/enlightenment.py", line 12, in tick
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> tick()
1
>>> tick()
2
>>> tick()
3
>>> tick()
4
>>> tick()
5
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> tick()

Traceback (most recent call last):
  File "<pyshell#311>", line 1, in <module>
    tick()
NameError: name 'tick' is not defined
>>> tick_a()
1
>>> tick_a()
2
>>> tick_a()
3
>>> tick_b()

Traceback (most recent call last):
  File "<pyshell#315>", line 1, in <module>
    tick_b()
  File "/Users/mike/teaching/2017-04-24/enlightenment.py", line 20, in tick_b
    count_a += 1
UnboundLocalError: local variable 'count_a' referenced before assignment
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> tick_b()
0
>>> tick_b()
0
>>> tick_b()
0
>>> tick_a()
1
>>> tick_a()
2
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> 
>>> a.tick()

Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    a.tick()
TypeError: tick() takes no arguments (1 given)
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> a.tick()
1
>>> a.tick()
2
>>> a.tick()
3
>>> b.tick()
1
>>> b.tick()
2
>>> 
========= RESTART: /Users/mike/teaching/2017-04-24/enlightenment.py =========
>>> tick_a()
1
>>> tick_a()
2
>>> tick_a()
3
>>> tick_b()
1
>>> tick_b()
2
>>> 
>>> 
>>> # lunch until 1:25pm
>>> 
