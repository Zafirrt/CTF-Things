

from z3 import *

d = [0xa9,0xee,0xd8,0xdc,0xda,0xe7,0xd8,0xec,0xa9,0xe5,0xef,0xde,0xd8,0xed,0xe1,0xe2,0xae,0xd8,0xde,0xda,0xae,0xe2,0xe5,0xf2,0xd8,0xee,0xec,0xe2,0xe7,0xb2,0xd8,0xd3,0xac,0x60,0xa5,0x8f,0x93,0x91,0x9e,0x8f,0xa3,0x60,0x9c,0xa6,0x95,0x8f,0xa4,0x98,0x99,0x65,0x8f,0x95,0x91,0x65,0x99,0x9c,0xa9,0x8f,0xa5,0xa3,0x99,0x9e,0x69,0x8f,0x8a,0x63,0xa5,0xea,0xd4,0xd8,0xd6,0xe3,0xd4,0xe8,0xa5,0xe1,0xeb,0xda,0xd4,0xe9,0xdd,0xde,0xaa,0xd4,0xda,0xd6,0xaa,0xde,0xe1,0xee,0xd4,0xea,0xe8,0xde,0xe3,0xae,0xd4,0xcf,0xa8,0x8f,0xd4,0xbe,0xc2,0xc0,0xcd,0xbe,0xd2,0x8f,0xcb,0xd5,0xc4,0xbe,0xd3,0xc7,0xc8,0x94,0xbe,0xc4,0xc0,0x94,0xc8,0xcb,0xd8,0xbe,0xd4,0xd2,0xc8,0xcd,0x98,0xbe,0xb9,0x92,0x93,0xd8,0xc2,0xc6,0xc4,0xd1,0xc2,0xd6,0x93,0xcf,0xd9,0xc8,0xc2,0xd7,0xcb,0xcc,0x98,0xc2,0xc8,0xc4,0x98,0xcc,0xcf,0xdc,0xc2,0xd8,0xd6,0xcc,0xd1,0x9c,0xc2,0xbd,0x96,0x91,0xd6,0xc0,0xc4,0xc2,0xcf,0xc0,0xd4,0x91,0xcd,0xd7,0xc6,0xc0,0xd5,0xc9,0xca,0x96,0xc0,0xc6,0xc2,0x96,0xca,0xcd,0xda,0xc0,0xd6,0xd4,0xca,0xcf,0x9a,0xc0,0xbb,0x94,0x9e,0xe3,0xcd,0xd1,0xcf,0xdc,0xcd,0xe1,0x9e,0xda,0xe4,0xd3,0xcd,0xe2,0xd6,0xd7,0xa3,0xcd,0xd3,0xcf,0xa3,0xd7,0xda,0xe7,0xcd,0xe3,0xe1,0xd7,0xdc,0xa7,0xcd,0xc8,0xa1,0x8f,0xd4,0xbe,0xc2,0xc0,0xcd,0xbe,0xd2,0x8f,0xcb,0xd5,0xc4,0xbe,0xd3,0xc7,0xc8,0x94,0xbe,0xc4,0xc0,0x94,0xc8,0xcb,0xd8,0xbe,0xd4,0xd2,0xc8,0xcd,0x98,0xbe,0xb9,0x92,0xa3,0xe8,0xd2,0xd6,0xd4,0xe1,0xd2,0xe6,0xa3,0xdf,0xe9,0xd8,0xd2,0xe7,0xdb,0xdc,0xa8,0xd2,0xd8,0xd4,0xa8,0xdc,0xdf,0xec,0xd2,0xe8,0xe6,0xdc,0xe1,0xac,0xd2,0xcd,0xa6,0x60,0xa5,0x8f,0x93,0x91,0x9e,0x8f,0xa3,0x60,0x9c,0xa6,0x95,0x8f,0xa4,0x98,0x99,0x65,0x8f,0x95,0x91,0x65,0x99,0x9c,0xa9,0x8f,0xa5,0xa3,0x99,0x9e,0x69,0x8f,0x8a,0x63,0x9c,0xe1,0xcb,0xcf,0xcd,0xda,0xcb,0xdf,0x9c,0xd8,0xe2,0xd1,0xcb,0xe0,0xd4,0xd5,0xa1,0xcb,0xd1,0xcd,0xa1,0xd5,0xd8,0xe5,0xcb,0xe1,0xdf,0xd5,0xda,0xa5,0xcb,0xc6,0x9f,0xa6,0xeb,0xd5,0xd9,0xd7,0xe4,0xd5,0xe9,0xa6,0xe2,0xec,0xdb,0xd5,0xea,0xde,0xdf,0xab,0xd5,0xdb,0xd7,0xab,0xdf,0xe2,0xef,0xd5,0xeb,0xe9,0xdf,0xe4,0xaf,0xd5,0xd0,0xa9,0x95,0xda,0xc4,0xc8,0xc6,0xd3,0xc4,0xd8,0x95,0xd1,0xdb,0xca,0xc4,0xd9,0xcd,0xce,0x9a,0xc4,0xca,0xc6,0x9a,0xce,0xd1,0xde,0xc4,0xda,0xd8,0xce,0xd3,0x9e,0xc4,0xbf,0x98,0x8f,0xd4,0xbe,0xc2,0xc0,0xcd,0xbe,0xd2,0x8f,0xcb,0xd5,0xc4,0xbe,0xd3,0xc7,0xc8,0x94,0xbe,0xc4,0xc0,0x94,0xc8,0xcb,0xd8,0xbe,0xd4,0xd2,0xc8,0xcd,0x98,0xbe,0xb9,0x92,0xa4,0xe9,0xd3,0xd7,0xd5,0xe2,0xd3,0xe7,0xa4,0xe0,0xea,0xd9,0xd3,0xe8,0xdc,0xdd,0xa9,0xd3,0xd9,0xd5,0xa9,0xdd,0xe0,0xed,0xd3,0xe9,0xe7,0xdd,0xe2,0xad,0xd3,0xce,0xa7,0x98,0xdd,0xc7,0xcb,0xc9,0xd6,0xc7,0xdb,0x98,0xd4,0xde,0xcd,0xc7,0xdc,0xd0,0xd1,0x9d,0xc7,0xcd,0xc9,0x9d,0xd1,0xd4,0xe1,0xc7,0xdd,0xdb,0xd1,0xd6,0xa1,0xc7,0xc2,0x9b,0x99,0xde,0xc8,0xcc,0xca,0xd7,0xc8,0xdc,0x99,0xd5,0xdf,0xce,0xc8,0xdd,0xd1,0xd2,0x9e,0xc8,0xce,0xca,0x9e,0xd2,0xd5,0xe2,0xc8,0xde,0xdc,0xd2,0xd7,0xa2,0xc8,0xc3,0x9c,0x65,0xaa,0x94,0x98,0x96,0xa3,0x94,0xa8,0x65,0xa1,0xab,0x9a,0x94,0xa9,0x9d,0x9e,0x6a,0x94,0x9a,0x96,0x6a,0x9e,0xa1,0xae,0x94,0xaa,0xa8,0x9e,0xa3,0x6e,0x94,0x8f,0x68,0x8f,0xd4,0xbe,0xc2,0xc0,0xcd,0xbe,0xd2,0x8f,0xcb,0xd5,0xc4,0xbe,0xd3,0xc7,0xc8,0x94,0xbe,0xc4,0xc0,0x94,0xc8,0xcb,0xd8,0xbe,0xd4,0xd2,0xc8,0xcd,0x98,0xbe,0xb9,0x92,0x95,0xda,0xc4,0xc8,0xc6,0xd3,0xc4,0xd8,0x95,0xd1,0xdb,0xca,0xc4,0xd9,0xcd,0xce,0x9a,0xc4,0xca,0xc6,0x9a,0xce,0xd1,0xde,0xc4,0xda,0xd8,0xce,0xd3,0x9e,0xc4,0xbf,0x98,0x91,0xd6,0xc0,0xc4,0xc2,0xcf,0xc0,0xd4,0x91,0xcd,0xd7,0xc6,0xc0,0xd5,0xc9,0xca,0x96,0xc0,0xc6,0xc2,0x96,0xca,0xcd,0xda,0xc0,0xd6,0xd4,0xca,0xcf,0x9a,0xc0,0xbb,0x94,0x65,0xaa,0x94,0x98,0x96,0xa3,0x94,0xa8,0x65,0xa1,0xab,0x9a,0x94,0xa9,0x9d,0x9e,0x6a,0x94,0x9a,0x96,0x6a,0x9e,0xa1,0xae,0x94,0xaa,0xa8,0x9e,0xa3,0x6e,0x94,0x8f,0x68,0x99,0xde,0xc8,0xcc,0xca,0xd7,0xc8,0xdc,0x99,0xd5,0xdf,0xce,0xc8,0xdd,0xd1,0xd2,0x9e,0xc8,0xce,0xca,0x9e,0xd2,0xd5,0xe2,0xc8,0xde,0xdc,0xd2,0xd7,0xa2,0xc8,0xc3,0x9c,0x9c,0xe1,0xcb,0xcf,0xcd,0xda,0xcb,0xdf,0x9c,0xd8,0xe2,0xd1,0xcb,0xe0,0xd4,0xd5,0xa1,0xcb,0xd1,0xcd,0xa1,0xd5,0xd8,0xe5,0xcb,0xe1,0xdf,0xd5,0xda,0xa5,0xcb,0xc6,0x9f,0xa9,0xee,0xd8,0xdc,0xda,0xe7,0xd8,0xec,0xa9,0xe5,0xef,0xde,0xd8,0xed,0xe1,0xe2,0xae,0xd8,0xde,0xda,0xae,0xe2,0xe5,0xf2,0xd8,0xee,0xec,0xe2,0xe7,0xb2,0xd8,0xd3,0xac,0x8f,0xd4,0xbe,0xc2,0xc0,0xcd,0xbe,0xd2,0x8f,0xcb,0xd5,0xc4,0xbe,0xd3,0xc7,0xc8,0x94,0xbe,0xc4,0xc0,0x94,0xc8,0xcb,0xd8,0xbe,0xd4,0xd2,0xc8,0xcd,0x98,0xbe,0xb9,0x92,0xa5,0xea,0xd4,0xd8,0xd6,0xe3,0xd4,0xe8,0xa5,0xe1,0xeb,0xda,0xd4,0xe9,0xdd,0xde,0xaa,0xd4,0xda,0xd6,0xaa,0xde,0xe1,0xee,0xd4,0xea,0xe8,0xde,0xe3,0xae,0xd4,0xcf,0xa8,0xa3,0xe8,0xd2,0xd6,0xd4,0xe1,0xd2,0xe6,0xa3,0xdf,0xe9,0xd8,0xd2,0xe7,0xdb,0xdc,0xa8,0xd2,0xd8,0xd4,0xa8,0xdc,0xdf,0xec,0xd2,0xe8,0xe6,0xdc,0xe1,0xac,0xd2,0xcd,0xa6,0x99,0xde,0xc8,0xcc,0xca,0xd7,0xc8,0xdc,0x99,0xd5,0xdf,0xce,0xc8,0xdd,0xd1,0xd2,0x9e,0xc8,0xce,0xca,0x9e,0xd2,0xd5,0xe2,0xc8,0xde,0xdc,0xd2,0xd7,0xa2,0xc8,0xc3,0x9c,0x9e,0xe3,0xcd,0xd1,0xcf,0xdc,0xcd,0xe1,0x9e,0xda,0xe4,0xd3,0xcd,0xe2,0xd6,0xd7,0xa3,0xcd,0xd3,0xcf,0xa3,0xd7,0xda,0xe7,0xcd,0xe3,0xe1,0xd7,0xdc,0xa7,0xcd,0xc8,0xa1,0x69,0xae,0x98,0x9c,0x9a,0xa7,0x98,0xac,0x69,0xa5,0xaf,0x9e,0x98,0xad,0xa1,0xa2,0x6e,0x98,0x9e,0x9a,0x6e,0xa2,0xa5,0xb2,0x98,0xae,0xac,0xa2,0xa7,0x72,0x98,0x93,0x6c,0x8f,0xd4,0xbe,0xc2,0xc0,0xcd,0xbe,0xd2,0x8f,0xcb,0xd5,0xc4,0xbe,0xd3,0xc7,0xc8,0x94,0xbe,0xc4,0xc0,0x94,0xc8,0xcb,0xd8,0xbe,0xd4,0xd2,0xc8,0xcd,0x98,0xbe,0xb9,0x92,0x8a,0xcf,0xb9,0xbd,0xbb,0xc8,0xb9,0xcd,0x8a,0xc6,0xd0,0xbf,0xb9,0xce,0xc2,0xc3,0x8f,0xb9,0xbf,0xbb,0x8f,0xc3,0xc6,0xd3,0xb9,0xcf,0xcd,0xc3,0xc8,0x93,0xb9,0xb4,0x8d]

print len(d)
counter = 0

s = Solver()
a = [Int("a[{}]".format(i)) for i in range(34)]

for i in range(0x21):
    for j in range(1, 0x22):
        s.add(a[i] + a[j] == d[counter])
        counter += 1


print s.check()
print s.model()

a = [0 for i in range(34)]

a[33] = 51
a[32] = 90
a[31] = 95
a[30] = 57
a[29] = 110
a[28] = 105
a[27] = 115
a[26] = 117
a[25] = 95
a[24] = 121
a[23] = 108
a[22] = 105
a[21] = 53
a[20] = 97
a[19] = 101
a[18] = 95
a[17] = 53
a[16] = 105
a[15] = 104
a[14] = 116
a[13] = 95
a[12] = 101
a[11] = 118
a[10] = 108
a[9] = 48
a[8] = 115
a[7] = 95
a[6] = 110
a[5] = 97
a[4] = 99
a[3] = 95
a[2] = 117
a[1] = 48
a[0] = 121


print ''.join([chr(i) for i in a])