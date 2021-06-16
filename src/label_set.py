class LabelSet:
    @staticmethod
    def addLabel(newLabel):
        file = open('.temp/text.txt', 'a')
        file.write(newLabel + '\n')
        file.close()

    @staticmethod
    def deleteFile():
        file = open('.temp/text.txt', 'w')
        file.write('')
        