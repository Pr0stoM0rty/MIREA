end = int(input())
end = end * 45 + (end // 2) * 5 + ((end + 1) // 2 - 1) * 15
print(end // 60 + 9, end % 60)