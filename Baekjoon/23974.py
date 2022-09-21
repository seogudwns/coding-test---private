N,K = map(int,input().split())
if N == 0 and K%6 == 1:
    print("HS")
elif N == 1 and K%6 in [0,5]:
    print("HS")
else:
    print("YG")

# ! 왜 틀린거나..?.. 거꾸로 출력...,,,ㄱ-

# N,K = map(int,input().split())
    
# even = [0 for _ in range(K+1)]
# odd = [0 for _ in range(K+1)]
# even[0] = even[2] = even[3] = even[4] = even[5] = 1
# odd[1] = odd[2] = odd[3] = odd[4] = 1

# for i in range(6,K+1):
#     if (odd[i - 4] and odd[i - 5]) and ((odd[i - 2] and odd[i - 3]) or (odd[i-6] and odd[i-7])):    
#         even[i] = 1
#     elif (even[i - 5] and even[i - 6]) and ((even[i - 3] and even[i - 4]) or (even[i - 7] and even[i - 8])):
#         even[i] = 1

#     if (even[i - 4] and even[i - 5]) and ((even[i - 2] and even[i - 3]) or (even[i - 6] and even[i - 7])):
#         odd[i] = 1
#     elif (odd[i - 5] and odd[i - 6]) and ((odd[i - 3] and odd[i - 4]) or (odd[i - 7] and odd[i - 8])):
#         odd[i] = 1

# print(even)
# print(odd)

'''


0 5(41) .. YG win
0 6((24X)141) .. YG win
0 7((1234X)11131) .. HS win
0 8(2141) .. YG win
0 9(414) .. YG win

1 5(131 or 311 or 23 or 41) .. HS win
1 6(141 or 24 or 321 or 42) .. HS win 
1 7(2131) .. YG win
1 8( 111(1234)(3311)(1X1X) ) .. YG win
1 9(3141) .. YG win 

even[:100] == [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

odd[:100] == [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


1 9 0
0 8 0 Y
0 7 0 H
0 5 0 Y
0 1 0 H .. HS


1 10 0 --> HS
0 9 0 Y
0 7 0 H
1 6 0 Y
1 5 0 H
0 2 0 Y.. HS

0 7 0 Y
0 5 0 H .. HS

1 8 0 Y
1 5 0 H
0 2 0 Y
0 1 0 H.. HS

1 15 0
0 14 0 Y
0 11 0 H
1 10 0

'''