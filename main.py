#The GPLv3 License (GPLv3)
#
#Copyright (c) 2023 Tushar Maharana
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Find the numbers made with the 3 digits each whose difference is minimal.
def digitdiffone(digits, bignum, tinynum):
    digits.sort()
    length = len(digits)
    for i in range(length):
        if i%2 == 0:
            tinynum.append(digits[i])
        else:
            bignum.append(digits[i])

def brute(digits):
    digits.sort()
    length = len(digits)
    permutations = []
    num = []
    i = 0
    while i < length:
        if i > length:
            num = digits[(i+length//2):-i]
        else:
            num = digits[i:i+length//2]
        permutations.append([num.copy()])
        i += 1
    return permutations
def digitdiffneg(bignum, tinynum, length):
    for i in range(1,length//2):
        if bignum[i] > tinynum[i]:
            big = bignum[i]
            bignum[i] = tinynum[i]
            tinynum[i] = big

def incrementneg(num):
    slicednum = num.copy()[1:]
    newnum = [num[0]]
    slicednum.reverse()
    newnum += slicednum
    num = newnum
    return num


def getnumbers(digits):
    length = len(digits)
    bignum = []
    tinynum = []

    digitdiffone(digits,bignum,tinynum)

    digitdiffneg(bignum,tinynum,length)

    tinynum = incrementneg(tinynum)

    digitdiffneg(bignum,tinynum,length)

    return (bignum,tinynum)

def list2int(number_list):
    number_str = ""
    for digit in number_list:
        number_str += digit
    return int(number_str)

def find_min_diff(digits):
    numbers = getnumbers(digits)
    bignum, tinynum = numbers[0], numbers[1]
    bignum = list2int(bignum)
    tinynum = list2int(tinynum)
    diff = bignum - tinynum
    return (diff , bignum, tinynum)

digits = list("234678")

print(brute(digits))
ans = find_min_diff(digits)
print(f"{ans[1]} - {ans[2]} = {ans[0]}")
