time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_min = 0
new_time = time.split(',')

for i in new_time:
    final_time = i.split()
    for t in final_time:
        if 'm' in t:
            total_min += int(t.replace('m', ''))
        elif 'h' in t:
            total_min += int(t.replace('h', '')) * 60
        elif 's' in t:
            total_min += int(t.replace('s', '')) // 60
print(total_min)