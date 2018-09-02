class Byesian:
    def __init__(self):
        self.length=-1;
        self.label=dict()
        self.vector=dict()
    def fit(self,trainDataSet:list,labels:list):
        if(len(trainDataSet)!=len(labels)):
            raise ValueError("测试集和类别不对应")
        # 测试数据集特征值的长度，
        self.length=len(trainDataSet[0])
        # 类别的长度
        labelsNum=len(labels)
        noRepeatLabel=set(labels)
        for item in noRepeatLabel:
            pass