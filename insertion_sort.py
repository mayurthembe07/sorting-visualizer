import time

def insertion(data, drawData, timer):
    n = len(data)

    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
            time.sleep(timer)
        data[j + 1] = key
        drawData(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
        time.sleep(timer)

    drawData(data, ['Green' for x in range(len(data))])
