word = input()
bomb = input()

bomb_last = bomb[-1]
bomb_len = len(bomb)
stack = []

for w in word:
    stack.append(w)
    if w == bomb_last and ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len): stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")

