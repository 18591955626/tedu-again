total_second = int(input("Please input second:"))

second = total_second % 60
minute = (total_second // 60) % 60
hour = total_second // 3600

print(hour, 'h', minute, 'm', second, 's')
