def every15minutes():
    for hr in range(24):
        for min in range(0, 60, 15):
            if hr == 0:
                yield f"12:{min:02} AM"
            elif hr < 12:
                yield f"{hr}:{min:02} AM"
            elif hr == 12:
                yield f"12:{min:02} PM"
            else:
                yield f"{hr-12}:{min:02} PM"

for t in every15minutes():
    print(t)

    