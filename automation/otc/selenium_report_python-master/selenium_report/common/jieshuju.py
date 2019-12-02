def noround(anum,x):
    #按指定的位数x进行anum的小数截取, 不四舍五入
    xx = int("1"+"0"*x)
    bnum = int(anum*xx)/xx
    #print(bnum)
    return(bnum)