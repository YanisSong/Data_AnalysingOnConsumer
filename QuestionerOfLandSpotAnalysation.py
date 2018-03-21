
def dataProgramming(cf, rf):
    filename = "D:\workDir\客服部调查问卷分析报告\云南5A风景区电信网络质量调查问卷清单.csv"
    dsename = "D:\workDir\客服部调查问卷分析报告\landspotResult.txt"
    # with open(rf, "a") as head:
    #     head.write("eNBId, objectId, LteScRSRP, LteNcRSRP, LteScRSRQ, LteNcRSRQ, LteScTadv, "
    #                "LteScAOA, LteScSinrUL, LteScEarfcn, LteScPci, Longitude, Latitude" + "\n")
    # head.close()
    fr = open(filename, encoding='gb18030', errors='ignore')
    for line in fr:
        # reason = processingLine(line)
        with open(dsename, "a") as destiny:
            destiny.write(line + '\n')
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

dataProgramming(" ", " ")