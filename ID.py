import pandas as pd
class Main:
    def __init__(self,s):
        self.df1=pd.read_excel(s)

    def getData(self):
        print(self.df1)


class getItem(Main):
    def __init__(self,s): #инициализация атрибутов класса родителя
        super().__init__(s)


    def get_item(self,a):
        def is_int():
            if isinstance(a,int)==False:
                raise ValueError("передать только целое число")
            i=0
            while i<100:
                if self.df1.left[i]<a<=self.df1.right[i]:
                    return self.df1.ID[i]
                if i==100-1:
                    return "нет совпадений"
                i+=1

        return is_int()


class getItem2(Main):
    def __init__(self,s):
        super().__init__(s)
    def get_item(self,a):
        def is_str():
            if isinstance(a,str)==False:
                raise ValueError("передать только строку")
            i=0
            while i<100:
                if self.df1.NAME[i]==a:
                    return self.df1.ID[i]
                    break
                if i==100-1 and self.df1.NAME[i]!=a:
                    return "нет совпадений"
                i += 1
        return is_str()


f1=getItem("datos.xlsx")
print(f1.get_item(20))
print(f1.get_item(0))

f2=getItem2("datos.xlsx")
print(f2.get_item('a59'))
print(f2.get_item(3))

