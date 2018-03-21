# from datetime import  datetime
# from elasticsearch import Elasticsearch


def dataProgramming():
    fr = open(r"C:\Users\Administrator\Desktop\mro数据_前100.sql", encoding='UTF-8')
    with open(r"C:\Users\Administrator\Desktop\destiny.txt", "a") as head:
        head.write("eNBId, objectId, LteScRSRP, LteNcRSRP, LteScRSRQ, LteNcRSRQ, LteScTadv, "
                   "LteScAOA, LteScSinrUL, LteScEarfcn, LteScPci, Longitude, Latitude" + "\n")
    head.close()
    for line in fr:
        strSet = line.split("VALUES")
        valueItem = strSet[1].lstrip(" (").replace(");", ",#@#")
        reason = processingLine(valueItem)
        with open(r"C:\Users\Administrator\Desktop\destiny.txt", "a") as destiny:
            destiny.write(reason + '\n')
    destiny.close()
    fr.close()


def processingLine(value):
    valueSet = value.split(",")
    valueList = []
    markSet = [31, 36, 4, 23, 5, 24, 6, 8, 9, 2, 3, 19, 20]
    for i in range(0, 13):
        if valueSet[markSet[i] - 1] == " ''":
            valueSet[markSet[i] - 1] = " '---'"
        valueList.append(valueSet[markSet[i] - 1])
    valueList.append(' --Ending;\n')
    reasonItem = ''.join(valueList)
    return reasonItem

dataProgramming()
