from random import randint


def göster(tahta):
    for i in tahta:
        print(i)

def kasaSecim(tahta):
    for i in range(100):
        sayı =randint(0,2),randint(0,2) 
        if(tahta[sayı[0]][sayı[1]] == "-"):
            tahta[sayı[0]][sayı[1]] = "O"
            break
        else:
            sayac = 0
            for i in tahta:
                if "-" not in i:
                    sayac +=1
            if sayac == 3:
                break


def kontrol(tahta):
    for i in range(3):
        ##Çapraz
        if i == 0:
            if(tahta[i][i] == "X" and tahta[i+1][i+1] == "X" and tahta[i+2][i+2] == "X" ):
                return True
            if(tahta[i][i] == "O" and tahta[i+1][i+1] == "O" and tahta[i+2][i+2] == "O" ):
                return False
                
            if(tahta[i][-1] == "X" and tahta[i+1][-2] == "X" and tahta[i+2][-3] == "X" ):
                return True
            if(tahta[i][-1] == "O" and tahta[i+1][-2] == "O" and tahta[i+2][-3] == "O" ):
                return False    
        ##Yanlar
        if tahta[i][0] == "X" and tahta[i][1] == "X" and tahta[i][2] == "X":
            return True
        if tahta[i][0] == "O" and tahta[i][1] == "O" and tahta[i][2] == "O":
            return False
        
        ##Yukarıdan Assagılar
        if (tahta[0][i] == "X" and tahta[1][i] == "X" and tahta[2][i] == "X" ):
            return True
        if (tahta[0][i] == "O" and tahta[1][i] == "O" and tahta[2][i] == "O" ):
            return False

def oyuncuSecim(tahta):
    while True:
        oyuncu = input(" // O ///Kaçıncı satır kaçıncı sutun ? ornk:1,2: ")
        oyuncu = oyuncu.split(",")
        oyuncu[0] = int(oyuncu[0])
        oyuncu[1] = int(oyuncu[1])
        if (oyuncu[0] >= 1 and oyuncu[0] <= 3 and oyuncu[1] >= 1 and oyuncu[1] <= 3):
            if ((tahta[oyuncu[0]-1][oyuncu[1]-1]) == "-"):
                (tahta[oyuncu[0]-1][oyuncu[1]-1]) = "O"
                break
            else:
                print("Orası zaten kullanıldı !!!!")
                göster(tahta)
        else:
            print("Yanlış tuşlama yaptınız !!!!!! ".upper())
        

tahta = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]


sayac = 0
while True:
    göster(tahta)
    oyuncu = input(" // X ///Kaçıncı satır kaçıncı sutun ? ornk:1,2: ")
    oyuncu = oyuncu.split(",")
    oyuncu[0] = int(oyuncu[0])
    oyuncu[1] = int(oyuncu[1])

    if (oyuncu[0] >= 1 and oyuncu[0] <= 3 and oyuncu[1] >= 1 and oyuncu[1] <= 3):
        if ((tahta[oyuncu[0]-1][oyuncu[1]-1]) == "-"):
            sayac +=1
            (tahta[oyuncu[0]-1][oyuncu[1]-1]) = "X"
            if kontrol(tahta):
                göster(tahta)
                print("X Kazandı !!!!!!!!")
                break
            
            if kontrol(tahta) == False:
                göster(tahta)
                print("O kazandı !!!!!!!!!")
                break
            
            if sayac == 5:
                göster(tahta)
                print("Berabere !!!!!!!!!")
                break
            
            göster(tahta)
            oyuncuSecim(tahta)
        else:
            print("Orası zaten kullanıldı !!!!")
        



    else:
        print("Yanlış tuşlama yaptınız !!!!!! ".upper())



"""
kontroller 
[0][0]
[1][0] 
[2][0]

[0][1]
[1][1] -> Dik

[0][2]
[1][2]
[2][2]

//////////////
[0][0]
[0][1] 
[0][2] 

[1][0]
[1][1] -> YAN
[1][2]

[2][0]
[2][1]
[2][2]

/////////////
[0][0]
[1][1] 
[2][2]
        -> CAPRAZ
[0][2]
[1][1]
[2][0]
"""
