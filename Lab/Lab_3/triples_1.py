
for x in range(10, 100):
    xexist = set(list(str(x)))
    for y in range(x + 1, 100):
        yexist = set(list(str(y)))
        if yexist & xexist == set():
            for z in range(y + 1, 100):
                zexist = set(list(str(z)))
                if zexist & yexist & xexist == set():
                    muti = set(list(str(x * y * z)))
                    if muti == zexist | yexist | xexist and len(muti) == 6:
                        print(f'{x} x {y} x {z} = {x * y * z}')
            else:
                zexist.clear()
                continue
        else:
            yexist.clear()
            continue
