import MroAnalysing as callMro


def callMroAlys():
    waitingFileName = input("Please input candidate file's URL:")
    fileURL = waitingFileName
    destinyPath = input("Please input output file's URL:")
    resultURL = destinyPath
    callMro.dataProgramming(fileURL, resultURL)


# def callQuesAly():