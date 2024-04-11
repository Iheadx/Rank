class Player:
    def __init__(self,id,name,score) -> None:
        self.id = id
        self.name = name
        self.score_list = score
        self.tot = sum([num if num != -1 else 0 for num in self.score_list])
        
    def get_L1(self):
        # 计算从score_list[0]到score_list[7]的和
        L1 = 0
        for i in range(8):
            L1 += self.score_list[i] if self.score_list[i]!= -1 else 0
        return L1
    def get_L2(self):
        # 计算从score_list[8]到score_list[11]的和
        L2 = 0
        for i in range(8,12):
            L2 += self.score_list[i] if self.score_list[i]!= -1 else 0
        return L2
    def get_L3(self):
        # 计算从score_list[12]到score_list[14]的和
        L3 = 0
        for i in range(12,15):
            L3 += self.score_list[i] if self.score_list[i]!= -1 else 0
        return L3
    
    def get_score(self):
        L1 = self.get_L1()
        L2 = self.get_L2()
        L3 = self.get_L3()
        L2_istrue = False
        L3_istrue = False
        if L1 >= 50:
            L2_istrue = True
        if L2 >= 25:
            L3_istrue = True
        
        tot = L1 + L2 * L2_istrue + L3 * L3_istrue
        return L1,L2,L3,L2_istrue,L3_istrue,tot
    
    
