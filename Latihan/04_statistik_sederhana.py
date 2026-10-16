def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]

    for x in data:
        total += x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    rata = total / len(data)

    return minimum, maksimum, rata


nilai = [70, 80, 65, 90, 75]

mn, mx, rt = statistik(nilai)

print("Data nilai:", nilai)
print("Nilai minimum:", mn)
print("Nilai maksimum:", mx)
print("Rata-rata:", rt)