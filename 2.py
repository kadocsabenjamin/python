

months = ["jan", "feb", "mar", "apr", "maj", "jun", "jul", "aug", "szept", "okt", "nov", "dec"]

num = int(input("add meg a honap szamat amit akarsz(1-12): "))



if num == 5:
    print("a legjobb hónapot választottad")
elif 1 <= num <= 12:
    print("A ", num, ". Hónap az a", months[num - 1])
else:
    print("rosszat választottál")