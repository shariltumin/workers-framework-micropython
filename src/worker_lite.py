/*
 * The MIT License (MIT)
 *
 * Copyright (c) Sharil Tumin
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

from gc import enable, collect
from utime import ticks_ms, ticks_diff
def task(m,g,p):return m.worker(g(p))
class MT:
   def __init__(my,s=20):
      my.A=[b'0000']*s;my.size=s;my.tail=-1
      my.M={};my.x=''
      enable()
   def worker(my,g):
      if my.tail+1<my.size:
         next(g)
         my.tail+=1;my.A[my.tail]=g
         return True
      else:
         return False
   def mbox(my,w,t=0):
      my.M[w]=None
      if t==0:
         def d():
            return my.M[w]==None
      else:
         n=ticks_ms()
         def d():
             return my.M[w]==None and ticks_diff(ticks_ms(),n)<t
      return d
   def get(my,w,k=False):
      v=my.M[w] if w in my.M else None
      if not k: my.M[w]=None
      return v
   def put(my,w,v):
      if w in my.M: my.M[w]=v
   def delay(my,t=0):
      n=ticks_ms()
      def d():
          return ticks_diff(ticks_ms(),n)<t
      return d
   def start(my):
      i=0
      while True:
         C=my.A[i]
         try:
            w=C.send(my)
         except StopIteration:
            w=True # Done
         except Exception as x:
            w=False # Error
            my.x=str(C).split()[2]+' '+str(x)
         if w!=None: # worker done
            C.close();del C;collect()
            my.A[i]=my.A[my.tail];my.A[my.tail]=b'0000'
            my.tail-=1
            if my.tail<0:
               return
         i+=1
         if i>my.tail:i=0

