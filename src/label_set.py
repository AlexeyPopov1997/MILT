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

    @staticmethod
    def getString12(index):
        label_set = []
        file = open('.temp/text.txt', 'r')
        for line in file:
            label_set.append(line)
        return label_set[index]
    