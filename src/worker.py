/*
 *
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

import gc
import utime
def task(g):
   def job(pm):
       return g(pm)
   return job
class MT:
   def __init__(my, n=20):
      my.s = WS(n); my.x=''
   def worker(my, f, p):
      if repr(f).find('closure')>=0:
         if K.tail<K.size:
            try:
               g=f(p)
               next(g)
            except Exception as x:
               my.x=str(x)
            else:
               K.A[K.tail]=g; K.tail+=1
               return K.tail
      # all else
      return 0
   def purge(my):
      for i in range(0,K.tail): K.A[i]=nop
      K.tail=0; gc.collect()
   def start(my):
      i=0
      while K.tail>0:
         C=K.A[i]
         try:
            w=C.send(my.s)
         except StopIteration:
            w=True # Done
         except Exception as x:
            w=False # Error
            my.x=str(C).split()[2]+' '+str(x)
         if w!=None:
            C.close();del C
            #gc.collect()
            K.tail-=1
            if i==K.tail: i=0
            else: K.A[i]=K.A[K.tail]
            K.A[K.tail]=nop
         else:
            i+=1
         if i>=K.tail:i=0
      return
   def log(my):
      return my.x
class K:
   A=[];tail=0;size=0;M={};L={}
def nop():pass
class WS:
   class V: pass
   def __init__(my,s):
      K.A=[nop]*s; K.size=s
      my.v=WS.V()
      gc.enable()
   def lock(my,l,w=''):
      if l in K.L: return False
      else: K.L[l]=w; return True
   def unlock(my,l,w=''):
      if l in K.L and w==K.L[l]: K.L.pop(l); return True
      else: return False
   def mbox(my,w,t=0):
      K.M[w]=None
      if t==0:
         def d():
            return K.M[w]==None
      else:
         n=utime.ticks_ms()
         def d():
            return K.M[w]==None and utime.ticks_diff(utime.ticks_ms(),n)<t
      return d
   def get(my,w,k=False):
      v=K.M[w] if w in K.M else None
      if not k: K.M[w]=None
      return v
   def put(my,w,v):
      if w in K.M: K.M[w]=v
   def delay(my,t=0):
      if t<=0:
         def d(): return False
      else:
         n=utime.ticks_ms()
         def d():
             return utime.ticks_diff(utime.ticks_ms(),n)<t
      return d

