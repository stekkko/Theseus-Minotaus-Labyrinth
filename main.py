class Cave(object):
 
    def __init__(self, toCave, wasMinotaur, wasTeseus):
        self.wasMinotaur = wasMinotaur
        self.hasLight = False
        self.toCave = toCave
        self.wasTeseus = wasTeseus

labirint = {}
minPath = 1

def compute(tesSt, tesNx, minSt, minNx):
    global minPath
    while(True):
        # Если минотавр и Тезей встретились в проходе, то
        # Тезей умирает от минотавра
        if ((tesSt == minSt and tesNx == minNx) or (tesSt == minNx and tesNx == minSt)):
            print("Theseus is killed between", tesSt, "and", tesNx)
            return
        
        # Если минотавр и Тезей встретились в пещере, то
        # Тезей убивает минотавра
        if (tesNx == minNx):
            print("Minotaur is slain in", tesNx)
            return
        
        ## Ход Тезея.
        
        # Если Тезей не нашел минотавра то он двигается против
        # часовой стрелки пока не найдет непомеченный им проход
        ind = 0 # индекс пещеры, куда пойдет Тезей
        arr = labirint[tesNx].toCave
        for i in range(len(arr)):
            if (arr[i] == tesSt):
                p = 0
                while (True):
                    if (i + p == len(arr) - 1):
                        p = -i
                    else:
                        p += 1
                    if (not labirint[tesNx].wasTeseus[i + p]):
                        ind = i + p
                        break
                break

        # Если Тезей нашел след минотавра, то он направляется
        # по самому свежему следу за ним
        mx = 0
        wasMin = False
        for i in range(len(arr)):
            if (labirint[tesNx].wasMinotaur[i] > mx):
                mx = labirint[tesNx].wasMinotaur[i]
                wasMin = True
                ind = i
        
        # Тезей пометил выход, что он там был 
        labirint[tesNx].wasTeseus[ind] = True
        
        # Тезей зажег свечу, если идет за минотавром
        if (wasMin):
            labirint[tesNx].hasLight = True
        tesSt = tesNx
        tesNx = arr[ind]
        
        ## Ход минотавра.
        
        # Минотавр идет по часовой стрелке по пещере, пока
        # не найдет еще не помеченный им проход.
        ind = 0
        arr = labirint[minNx].toCave
        for i in range(len(arr)):
            if (arr[i] == minSt):
                p = 0
                while (True):
                    if (i + p == 0):
                        p = len(arr) - i - 1
                    else:
                        p -= 1
                    if (labirint[minNx].wasMinotaur[i + p] == 0):
                        ind = i + p
                        break
                break

        # Минотавр помечает проход, в который пройдет
        labirint[minNx].wasMinotaur[ind] = minPath
        minPath += 1
        
        minSt = minNx
        minNx = arr[ind]
        
        # Если минотавр увидит в следующей пещере заженную
        # свечу, то развернется в обратную сторону
        if (labirint[minNx].hasLight):
            temp = minSt
            minSt = minNx
            minNx = temp

## код начинается здесь
if __name__ == "__main__":
    while (True):
        s = input()
        
        # Если был введен символ #, то программа завершается
        if (s[0] == '#'):
            break
        
        # Если введен символ @, то запускается моделирование
        # текущего лабиринта с начальными координатами Тезея
        # и минотавра идущими после символа @
        elif (s[0] == '@'):
            tesSt = s[1]
            tesNx = s[2]
            minSt = s[3]
            minNx = s[4]
            compute(tesSt, tesNx, minSt, minNx)
        
        # Инача считывается строка с данными о пещере
        else:
            labirint.update({s[0] : Cave(s[2:], [0] * len(s[2:]), [False] * len(s[2:]))})








