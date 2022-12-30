"""
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
"""

class Pipe():
    def __init__(my, s=100):
       my.a=bytearray([0]*s);my.s=s
       my.h=my.t=my.n=0
    def put(my, w):
       if my.n>=my.s:
          return 0
       else:
          m=my.n
          for v in list(w):
             my.a[my.t]=v;my.t+=1;my.n+=1
             if my.t==my.s:my.t=0
             if my.n>=my.s or my.t==my.h: return my.n-m
          return my.n-m
    def get(my, c=0):
       if my.n==0 or c<0:
          return ''
       else:
          if c>my.n or c==0: c=my.n
          if my.h+c<=my.s:
             w=my.a[my.h:my.h+c]
             my.h=(my.h+c)%my.s
          else:
             w=my.a[my.h:]+my.a[0:c-(my.s-my.h)]
             my.h=c-(my.s-my.h)
          my.n-=c
          if my.n==0:
             my.t=my.h
          return w

