import png
import os
import time
colors = {
0:(123,207,246),
1:(169, 161, 19),
2:(228,3,86),
3:(50, 47, 145),
4:(131, 255, 82),
5:(0,0,0),
6:(50, 122, 253),
7:(149,149,149),
8:(98,57,19),
9:(45,167,86),
10:(248, 0, 252),
11:(97,122,115) }

# Size of my biggest one: 2000, 320
chunkSizeX = 320
chunkSizeY = 320
img = []
rows = [() for i in range(16)]

path = input("Please enter the path to the world download (With a / at the end)")

for chunkY in range(-int(chunkSizeY / 2), int(chunkSizeY / 2)):
    tic = time.perf_counter()
    for chunkX in range(-int(chunkSizeX / 2), int(chunkSizeX / 2)):
        s = path + str(chunkX) + "_" + str(chunkY) + "_1.chunk"
        if os.path.isfile(s):
            with open(s, "rb") as f:
                bytes_read = f.read()
                for y in range(16):
                    row = ()
                    for x in range(16):
                        row = row + colors[bytes_read[x + y * 16]]
                    rows[y] = rows[y] + row
        else:
            for y in range(16):
                row = ()
                for x in range(16):
                    row = row + (123, 207, 246)
                rows[y] = rows[y] + row

    for r in rows:
        img.append(r)
    rows = [() for i in range(16)]
    toc = time.perf_counter()
    print(f"Row {chunkY} finished in {toc - tic:0.4f} seconds")

with open('worldReaderTest.png', 'wb') as f:
    w = png.Writer(chunkSizeX*16, chunkSizeY*16, greyscale=False)
    w.write(f, img)