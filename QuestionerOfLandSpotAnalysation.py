# This module is used to analysing the questioner that is collected from the land spots.
import re


# data input and output interface.
def dataProgramming(cf, rf):
    filename = "D:\workDir\客服部调查问卷分析报告\云南5A风景区电信网络质量调查问卷清单.csv"
    outputUrl = "D:\workDir\客服部调查问卷分析报告\landspotResult.txt"
    countingDict = {}
    suggesstionDick = {}
    totalCustomer = 0
    distributeConsumerDict = {}
    # Todo: Add userDict in the future, which is used to analysing user information.
    fr = open(filename, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line, outputUrl)
        if reason:
            analysingProcess(reason, countingDict, suggesstionDick, totalCustomer, distributeConsumerDict)
    fr.close()


#analysding function
def analysingProcess(reason, countingDict, suggesstionDick, totalCustomer):
    uselessCount = 0
    if reason[0] != "---" and reason[0] != "上述一个都没去过":
        totalCustomer += 1
        if reason[1].find("满意") or reason[1].find("惊喜"):
            uselessCount += 1
        else:
            if reason[0] in countingDict:
                countingDict[reason[0]] += 1
            else:
                countingDict += {reason[0] : 1}
        suggesstion = "满意度调查--"+"通话："+ reason[2] + ",即时信息:" + reason[3] \
                      + ",网络速度:" + reason[4] + ",个人意见:" + reason[5] + ",调研景区：" + reason[0]
        if reason[6] in suggesstionDick:
            uselessCount += 1
        else:
            suggesstionDick += {reason[6]: suggesstion}
    statisticsProcess(totalCustomer, uselessCount, countingDict)
    return uselessCount


# This function is used to deal with the statistics exhibition.
def statisticsProcess(total, useless, countingDict):
    print("under desinging")


#data cleaning function.
def processingLine(value, outputUrl):
    involvingNumber = re.findall(r"\d{11}", value)
    if not involvingNumber:
        return
    valueSet = value.split(",")
    valueList = []
    markSet = [7, 8, 19, 20, 23, 24, 30]
    for i in range(0, 7):
        if len(valueSet) < 30:
            continue
        if valueSet[markSet[i] - 1] == "":
            valueSet[markSet[i] - 1] = "---"
        valueList.append(valueSet[markSet[i] - 1])
    reasonItem = ''.join(valueList)
    with open(outputUrl, "a") as destiny:
        destiny.write(reasonItem)
    return valueList


# @Test
# dataProgramming(" ", " ")