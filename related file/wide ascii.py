WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F)) 
WIDE_MAP.update( dict((WIDE_MAP[k], k) for k in WIDE_MAP) )
WIDE_MAP[0x20] = 0x3000
#store in dict as dec
#สิ่งที่ต้องการ คือ ข้อความ ออกมาเป็น wide ascii acho --> 

def widen(s):

    #ไปดูตารางเเมพทีละตัว ส่งกลับมา

    return s.translate(WIDE_MAP)
inpuit = input("abbababab :")
damn=""
for i in widen(inpuit):
        hexnord = hex(ord(i))
        #binord = binord[2:]
        damn = damn+hexnord
print(damn)

#base10 char ==> hex
#print(0x21 + 0xFEE0) #==>FF01HEX(65281dec)==>21HEX(33dec)


