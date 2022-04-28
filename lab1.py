from statistics import median, mean

def average_am(text):
    words_in_senten = []
    temp_str = ""
    for i in range(len(text)):
        if(text[i] == '.' or text[i] == '!' or text[i] == '?' or text[i] == ';' or i == len(text) -1 ):
            temp_str = Clear_text(temp_str)
            words_in_senten.append(len(temp_str.split()))
            temp_str = ""
            continue
        else:
            temp_str += text[i]

    return int(mean(words_in_senten))

def median_am(text):
    words_in_senten = []
    temp_str = ""
    for i in range(len(text)):
        if(text[i] == '.' or text[i] == '!' or text[i] == '?' or text[i] == ';' or i == len(text) -1 ):
            temp_str = Clear_text(temp_str)
            words_in_senten.append(len(temp_str.split()))
            temp_str = ""
            continue
        else:
            temp_str += text[i]
    
    return int(median(words_in_senten))


def Clear_text(text):
    rez = Clear_signs(text)
    rez = rez.lower()
    return rez

def Clear_signs(text):
    clear_text = ""
    for i in range(0,len(text)):
        if (text[i] == ',' or text[i] == '.' or text[i] == ':' or text[i] == '!' or text[i] == '?' or text[i] == '-' or text[i] == ';'):
            continue
        else:
            clear_text += text[i]
    return clear_text


def word_counter(text):
    words = Clear_text(text).split()
    temp_d = {}
    for word in words:
        count = temp_d.get(word, 0)
        temp_d[word] = count + 1

    for word in temp_d:
        print(word, ":", temp_d[word])
    return temp_d


def N_gramm(text, n, k):
    words = Clear_text(text).split()
    line = ""
    for word in words:
        line += word

    count = {}
    for i in range(len(line) - n + 1):
        temp = line[0 + i:i + n]
        if temp in count:
            count[temp] += 1
        else:
            count[temp] = 1

    d = {k: count[k] for k in sorted(count, key=count.get, reverse=True)}

    i = 1
    for key, value in d.items():
        if i > k:
            break
        print(f"{key}: {value}", end=" ")
        i += 1
    print("\n")
    



text2 =  '''Taxi dispatcher yes to the client: Get out in 5 minutes. 
                    Mazda is  yes waiting for you, metallic blue. 
                    Further, accor.ding to the driver: 
                    A woman come yes s out of the ent.rance. 
                    She walked around the car. 2 times, 
                    approached the ajar window and asked 
                    Are you blue Vitalik? ban ban ban ban'''
text3 = ''' Появился, значит, в Зоне Чёрный сталкер. К лагерю ночью повадился ходить 
            и там сует руку в палатку и говорит: Водички попить! А если не дашь 
            хлебнуть из фляжки или наружу полезешь - быстро пришибет! А раз мужик один решил пошутить: 
            вылез тихо из палатки, надел кожаную перчатку и полез к соседям в палатку. 
            Полез, значит, и попрошайничает жалостно: Водички, водички попить. 
            А тут из палатки навстречу высовывается рука и за горло его - цап! 
            И сиплый голосок отзывается тихонько: А тебе моя водичка зачем нужна?'''
text = "computerscienceandartific ialintelligence"

N_gramm(text3,2, 10)
word_counter(text3)
print(median_am(text3))
print(average_am(text3))
