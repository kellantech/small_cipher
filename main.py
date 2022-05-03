k=int(input("key? "))
k2 = int(input("key2? "))
k3 = int(input("key3? "))

import random
def shift_dict(dic, shift):
    dic_len = len(dic)
    shift = shift % dic_len
    list_dic = [(k,v) for k, v in dic.items()]
    shifted = {
        list_dic[x][0]: list_dic[ (x - shift) % dic_len ][1]
        for x in range(dic_len)
    }
    return shifted
swap = {'R': 'w', '5': '4', 'q': 'Z', 'J': 'o', 'v': 'q', 'K': 'K', 'I': 'Q', '1': 'A', ' ': 'i', 'm': 'D', 'p': 'd', 'T': '0', 'D': '!', 'h': 'h', 'L': 'u', 'X': 's', '7': 'M', 'l': '7', 'd': '3', 's': '5', 'b': 'r', '9': 'T', 'u': 'm', 'B': 'F', 'n': 'p', 'o': 'c', 'Z': 'a', 'G': 'y', 'k': 'O', '2': 'E', 'r': 'b', 'S': 'U', 'e': '1', '3': '8', 'Y': 'v', ',': '9', 'A': 'e', 't': 'V', 'W': '2', 'g': 'I', '6': 'X', 'P': 'z', 'M': 'L', '0': 'B', '.': 'G', 'a': 'S', '8': 'f', 'N': '6', 'O': 'n', 'i': 'J', 'y': 'H', 'H': 'x', 'c': ',', 'j': 'k', 'w': 'C', 'E': 'P', 'V': ' ', 'U': '.', 'Q': 'W', 'z': 'g', '!': 'R', 'f': 't', 'C': 'l', 'x': 'j', '4': 'N', 'F': 'Y'}

swap = shift_dict(swap,k)
swap2 = shift_dict(swap, k2)
swap3 = shift_dict(swap, k3)

inv_swap = {v: k for k, v in swap.items()}
inv_swap2 = {v: k for k, v in swap2.items()}
inv_swap3 = {v: k for k, v in swap3.items()}

def e(txt):
	out = random.choice([n for n in swap])
	for n in txt:
		out+=swap[n]
	out+=random.choice([n for n in swap])
	ls = [fz for fz in out]
	ls.append(ls.pop(0))
	for n in range(len(ls)):
		if n % 2 ==0:
			ls[n] = swap2[ls[n]]
	for n in range(len(ls)):
		if n % 4 ==0:
			ls[n] = swap3[ls[n]]
		
			
	out = ''.join(ls)
		
	return out	
def d(txt):
	txls = [z for z in txt]
	for n in range(len(txls)):
		if n % 4 ==0:
			txls[n] = inv_swap3[txls[n]]

	for n in range(len(txls)):
		if n % 2 ==0:
			txls[n] = inv_swap2[txls[n]]

	txls.insert(0,txls.pop())
	txt = ''.join(txls)
	txt = txt[1:-1]
	out=""
	for n in txt:
		out+=inv_swap[n]
	return out	

while True:
	print("e = encrypt, d=decrypt, q=quit")
	inp = input()
	if inp == "e":
		en = (e(input("message: ")))
		print(en)
	elif inp == 'd':
		print(d(input("message: ")))
	elif inp=="q":break
	else:print("comand not found")


