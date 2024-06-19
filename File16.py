#Count the frequency of each character in the string
str1 = input("Enter the string: ")
i=0
count_sp =count_a =count_b = count_c = count_d = count_e = count_f = count_g = count_h = 0
count_i =count_j =count_k = count_l = count_m = count_n = count_o = count_p = count_q = 0
count_r =count_s =count_t = count_u = count_v = count_w = count_x = count_y = count_z = 0
while (i<len(str1)):
    for a in range(0,len(str1)):
        if (str1[a]=='a' or str1[a]=='A'):
            count_a += 1
        elif (str1[a]=='b' or str1[a]=='B'):
            count_b +=1
        elif (str1[a]=='c' or str1[a]=='C'):
            count_c += 1
        elif (str1[a]=='d' or str1[a]=='D'):
            count_d += 1
        elif (str1[a] == 'e' or str1[a]== 'E'):
            count_e += 1
        elif (str1[a]=='f' or str1[a]=='F'):
            count_f += 1
        elif (str1[a]=='g' or str1[a]=='G'):
            count_g += 1
        elif (str1[a]=='h' or str1[a]=='H'):
            count_h += 1
        elif (str1[a]=='i' or str1[a]=='I'):
            count_i += 1
        elif (str1[a]=='j' or str1[a]=='J'):
            count_j += 1
        elif (str1[a]=='k' or str1[a]=='K'):
            count_k += 1
        elif (str1[a]=='l' or str1[a]=='L'):
            count_l += 1
        elif (str1[a]=='m' or str1[a]=='M'):
            count_m += 1
        elif (str1[a]=='n' or str1[a]=='N'):
            count_n += 1
        elif (str1[a]=='o' or str1[a]=='O'):
            count_o += 1
        elif (str1[a]=='p' or str1[a]=='P'):
            count_p += 1
        elif (str1[a]=='r' or str1[a]=='R'):
            count_r += 1
        elif (str1[a]=='s' or str1[a]=='S'):
            count_s += 1
        elif (str1[a] == 't' or str1[a]== 'T'):
            count_t += 1
        elif (str1[a]=='u' or str1[a]=='U'):
            count_u += 1
        elif (str1[a]=='v' or str1[a]=='V'):
            count_v += 1
        elif (str1[a]=='w' or str1[a]=='W'):
            count_w += 1
        elif (str1[a]=='x' or str1[a]=='X'):
            count_x += 1
        elif (str1[a]=='y' or str1[a]=='Y'):
            count_y += 1
        elif (str1[a]=='z' or str1[a]=='Z'):
            count_z += 1
        else:
            count_sp += 1
        i = i+1
print("Frequency A/a: ",count_a)
print("Frequency B/b: ",count_b)
print("Frequency C/c: ",count_c)
print("Frequency D/d: ",count_d)
print("Frequency E/e: ",count_e)
print("Frequency F/f: ",count_f)
print("Frequency G/g: ",count_g)
print("Frequency H/h: ",count_h)
print("Frequency I/i: ",count_i)
print("Frequency J/j: ",count_j)
print("Frequency K/k: ",count_k)
print("Frequency L/l: ",count_l)
print("Frequency M/m: ",count_m)
print("Frequency N/n: ",count_n)
print("Frequency O/o: ",count_o)
print("Frequency P/p: ",count_p)
print("Frequency Q/q: ",count_q)
print("Frequency R/r: ",count_r)
print("Frequency S/s: ",count_s)
print("Frequency T/t: ",count_t)
print("Frequency U/u: ",count_u)
print("Frequency V/v: ",count_v)
print("Frequency W/w: ",count_w)
print("Frequency X/x: ",count_x)
print("Frequency Y/y: ",count_y)
print("Frequency Z/z: ",count_z)
#print("Frequency of Special characters: ",count_sp)
