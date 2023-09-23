s = 'aababcabc'
k = 3
s_list = list(s)
window_str = s[:k]
n = len(s)
ans = []
for i in range(n - k):
    window_str = window_str.replace(window_str[i], '') + s[i + k]
    if window_str not in ans:
        ans.append(window_str)
print(len(ans))

