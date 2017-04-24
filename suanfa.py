# -*-coding:CP936 -*-

def narc(n):
    pows = [_i**int(n) for _i in range(10)]
    res = pows[1:]
    for _i in range(int(n)-1):
        res = [s +pows[d] for s in res for d in range(10)]
    lower=10**(int(n)-1)
    return[k+lower for k,v in enumerate(res) if k+lower == v]
def yong():
       zppo = []
       while True:
            a = raw_input("请输入一个任意个位数以计算水仙数（最高支持到7），exit退出。")
            chong=[]
            if a == "exit":
                 input("\n\t按任意键以退出！")
            if len(a) > 1:
                 print"位数错误，请重新输入！"
                 continue
            for b in a:
                if b not in chong :
                     chong.append(b)
                if len(chong) == 1:
                     s = narc(a)
            if len(s) == 0:
                print "没有水仙花数"
            if len(s) > 0:
                print s,"是水仙花数"
                break
           
def for_1():
    for i in range(1,10):
        for j in range(0,10):
            for k in range(0,10):
                if i*100+j*10+k == i**3+j**3+k**3:
                    print i*100+j*10+k
def zifu_1():
   while True:
         p = raw_input("输入一个数范围定义水仙花数位数，输入e退出主程序！。")
         if p == "e":
             input("任意键退出！")
         try:
            temp = p.strip().split()
            m = min(int(temp[0]),int(temp[1]))
            n = max(int(temp[0]),int(temp[1]))
         except:
             print "出错了，请重试！"
             continue
         if n > 1000:
             print("超出范围，请重试！")
         number = range(m,n)
         c = []   
         for a in number:
             z = str(a)
             x = 0
             for b in z:
                k = int(b) **3
                x = x + k
                if x == a:
                    if x not in c:
                        c.append(x)
         if len(c) != 0:
              for d in c:
                  print d,"是水仙花数"
def zifu_2():
   while True:
         p = raw_input("输入一个数范围定义水仙花数位数。输入e退出主程序！")
         if p == "e":
             input("任意键退出！")
         try:
             temp = p.strip().split()
             m = min(int(temp[0]),int(temp[1]))
             n = max(int(temp[0]),int(temp[1]))
         except:
                 print "出错了，请重试！"
         number = range(m,n)
         c = []   
         for a in number:
               z = str(a)
               x = 0
               for b in z:
                    k = int(b) ** len(z)
                    x = x + k
                    if x == a:
                       if x not in c:
                            c.append(x)     
         if len(c) != 0:
               for d in c:
                    print d,"是水仙花数"
def main():
   while True:
          a = input("输入一个数决定算法\n1,按位数计算（最高支持到7）\n2，按公式计算。\n\t")
          if a == 1:
              yong()
              while True:
                   b = raw_input( "计算完成,继续一次按1\n结束按2\n什么都不输入有惊喜\n\t")
                   if len(b) == 0:
                         print "调皮"
                         c = 1
                         break
                   if int(b) == 1:
                        yong()
                        continue
                   elif int(b) == 2:
                         input("结束了，按任意键退出！")
                   else:
                        print"重输！！！好气啊！！！！"
                        continue
              if c == 1:
                   continue
          elif a == 2:
              b = input("1,for语句\n2，字符串\n\t")
              if b == 1:
                  for_1()
                  while True:
                      c = raw_input( "计算完成,继续一次按1\n结束按2\n什么都不输入有惊喜\n\t")
                      if len(c) == 0:
                          print "调皮"
                          d = 1
                          break
                      if int(c) == 1:
                            for_1()
                            continue
                      elif int(c) == 2:
                          input("结束了，按任意键退出！")
                      else:
                             print "调皮"
                             continue
                  if d == 1:
                      continue
              elif b == 2:
                  cc = input("1,普通计算（1-1000以内）\n2,高级（无限制）\n\t")
                  if cc == 1:
                      zifu_1()
                  elif cc == 2:
                      zifu_2()
                  else:
                      print "输入错误，请重试！"
                      continue
              else:
                  print "输入错误，请重试！"
                  continue
          else:
               print "输入错误，请重试！"
               continue
    
                      

main()



