# 문제
# 한 줄로 된 간단한 에디터를 구현하려고 한다. 
# 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 
# 최대 600,000글자까지 입력할 수 있다.

# 이 편집기에는 '커서'라는 것이 있는데,
# 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 
# 문장의 맨 뒤(마지막 문자의 오른쪽), 
# 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 
# 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

# 이 편집기가 지원하는 명령어는 다음과 같다.

# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함
# 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때,
# 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
# 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

# 입력
# 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다.
# 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 
# 길이는 100,000을 넘지 않는다. 
# 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 
# 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다.
# 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

# 출력
# 첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.

import sys 

# input = sys.stdin.readline

# string_list = list(input().rstrip())
# cursor = len(string_list)

# n = int(input())

# for _ in range(n):
#     cmd = list(input().split())
#     if cmd[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#     elif cmd[0] == "D":
#         if cursor < len(string_list):
#             cursor += 1
#     elif cmd[0] == "B":
#         if cursor > 0:
#             string_list.remove(string_list[cursor-1])
#     elif cmd[0] == "P":
#         string_list.insert(cursor,cmd[1])
#         cursor += 1

# print("".join(string_list)) 

#시간초과 됨 
#밑 코드는 스택을 써서 해결하 코드    

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == "L":
        if st1:
            st2.append(st1.pop())
    elif command[0] == "D":
        if st2:
            st1.append(st2.pop())
    elif command[0] == "B":
        if st1:
            st1.pop()
    else:
        st1.append(command[1])
st1.extend(reversed(st2))
print("".join(st1))               
