a, b, c = map(int, input().split())

mb = float(a*b*c/8/1024/1024)
print("%.2f MB" %mb)