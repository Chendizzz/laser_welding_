import numpy as np

def preprocessing(f):

    '1、文件头:一共14字节'
    bfType = f.read(2)  # 文件类型
    bfSize1 = f.read(4)  # 该bmp文件总大小
    f.seek(f.tell() + 4)  # 跳过保留字
    bfOffBits1 = f.read(4)  # 从文件开始到数据开始的偏移量，    偏移1078 加上256*256正好是文件的大小（单位：B）

    # struct.unpack('i',*) 也可以
    bfSize = int.from_bytes(bfSize1, byteorder='little', signed=True)
    bfOffBits = int.from_bytes(bfOffBits1, byteorder='little', signed=True)

    '2、信息头：40B'
    biSize = f.read(4)  # 这部分长度为40字节
    biWidth1 = f.read(4)
    biHeight1 = f.read(4)
    biPlanes = f.read(2)  # 1,位图的位面数
    biBitCount1 = f.read(2)
    compression = f.read(4)
    compression = int.from_bytes(compression, byteorder="little", signed=True)
    # struct.unpack('i',*) 也可以
    biWidth = int.from_bytes(biWidth1, byteorder='little', signed=True)
    biHeight = int.from_bytes(biHeight1, byteorder='little', signed=True)
    biBitCount = int.from_bytes(biBitCount1, byteorder='little', signed=True)
    f.read(20)
    print('文件类型{0},大小{1}，偏移量{2}，位图宽度（列）{3}，高度（行）{4}，每个像素所占位数{5},压缩方式{6}'.format(bfType, bfSize, bfOffBits, biWidth, biHeight,biBitCount,compression))
    return f

def twoBytes2_565(bits):
    bit_str = str(bits)
    l = len(bit_str)-2
    bit_str_eff = bit_str[2:]
    if l <= 5:
        bit_r = bit_str_eff
        bit_g = "0"
        bit_b = "0"
    elif l>5 and l<=11:
        bit_r = bit_str_eff[0:5]
        bit_g = bit_str_eff[5:11]
        bit_b = "0"
    else:
        bit_r = bit_str_eff[0:5]
        bit_g = bit_str_eff[5:11]
        bit_b = bit_str_eff[11:16]

    return int(bit_r,2), int(bit_g,2), int(bit_b,2)

def generateRGB_channel(f):
    r = np.zeros([400,4200])
    g = np.zeros([400,4200])
    b = np.zeros([400,4200])
    for x in range(4200):
        for y in range(400):
            pixel = f.read(2)
            bytes2 = bin(int.from_bytes(pixel, byteorder="little", signed=True))  # use little byteorder to identify
            r_, g_, b_ = twoBytes2_565(bytes2)

            r[y,x] = r_
            g[y,x] = g_
            b[y,x] = b_

            r[y,x] = r_
            g[y,x] = 255-g_
            b[y,x] = 255-b_

            # print("converted to bits: ", bytes2)
    return r,g,b