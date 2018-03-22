# This module is used to analysing the questioner that is collected from the land spots.
import re


# data input and output interface.
# Todo: Modifying the function use the input file URLs.
def dataProgramming():
    filename = "D:\workDir\客服部调查问卷分析报告\云南5A风景区电信网络质量调查问卷清单.csv"
    outputUrl = "D:\workDir\客服部调查问卷分析报告\landspotResult.txt"
    countingDict = {}
    suggesstionDick = {}
    totalCustomer = []
    uselessConsumer = []
    distributeConsumerDict = {}
    # Todo: Add userDict in the future, which is used to analysing user information.
    fr = open(filename, encoding='gb18030', errors='ignore')
    for line in fr:
        reason = processingLine(line, outputUrl)
        if reason:
            statistics = analysingProcess(reason, countingDict, suggesstionDick, totalCustomer,
                                          uselessConsumer, distributeConsumerDict)
    fr.close()
    return statistics


# Data cleaning function.
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


# Analysing function is used to collect different kinds of consumers' number and suggestions.
def analysingProcess(reason, countingDict, suggesstionDick, totalCustomer, uselessConsumer, distributeConsumerDict):
    if ("---" in reason[0]) or ("上述一个都没去过" in reason[0]):
        uselessConsumer.append("1")
        totalCustomer.append("1")
    else:
        totalCustomer.append("1")
        if ("满意" in reason[1]) or ("惊喜" in reason[1]):
            if reason[0] in distributeConsumerDict:
                distributeConsumerDict[reason[0]] += 1
            else:
                distributeConsumerDict[reason[0]] = 1
        else:
            if reason[0] in distributeConsumerDict:
                distributeConsumerDict[reason[0]] += 1
            else:
                distributeConsumerDict[reason[0]] = 1
            if reason[0] in countingDict:
                countingDict[reason[0]] += 1
            else:
                countingDict[reason[0]] = 1
        suggesstion = "满意度调查--"+"通话：" + reason[2] + ",即时信息:" + reason[3] \
                      + ",网络速度:" + reason[4] + ",个人意见:" + reason[5] + ",调研景区：" + reason[0]
        if reason[6] in suggesstionDick and reason[0] in countingDict:
            # There are more than one report under the same person in one spot.
            uselessConsumer.append("1")
        else:
            suggesstionDick[reason[6]] = suggesstion
    statistics = statisticsProcess(totalCustomer, uselessConsumer, countingDict, distributeConsumerDict)
    return statistics


# This function is used to deal with the statistics exhibition.
def statisticsProcess(total, useless, countingDict, distributeConsumerDict):
    statistics = {}
    if total != 0:
        uselessStatistics = len(useless)/len(total)
    else:
        uselessStatistics = 0
    statistics['无效数据比率：'] = uselessStatistics
    for (key, value) in distributeConsumerDict.items():
        if key in countingDict:
            oneSpotStatistics = countingDict[key]/value
        else:
            oneSpotStatistics = 1.0
        statistics[key] = oneSpotStatistics
    return statistics


# @Test
# data = dataProgramming()
# print(data)

