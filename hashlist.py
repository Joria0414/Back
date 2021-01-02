# Data_Input=['25','34','45','07','26']
# class hashlist:
#     def __init__(self,data=-1):
#         self.data = data
#         self.list = [None,None,None,None,None,None,None,None,None,None]
#     def enlarge(self,index):
#         self.list[index] = hashlist()
#     def setdata(self,data):
#         self.data = data
# def Creat_Tree(Root,data,i=0):
#     if data[i:]:
#         index = int(data[0+i])
#         if not Root.list[index]:
#             Root.enlarge(index)
#         Root.list[index] = Creat_Tree(Root.list[index],data,i+1)
#         return Root#将得到的节点返回
#     else:
#         Root.setdata(data=data)
#         return Root
# def Inorder(Root):
#     if Root != None:
#         if Root.data==-1:
#             for i in Root.list:
#                 Inorder(i)
#         else:
#             print(Root.data)
#
# a=hashlist()
# for data in Data_Input:
#     a=Creat_Tree(a,data)
# code = input('code=')
# list = list(code)
# list = [int(i) for i in list]
# for i in list:
#     a=a.list[i]
# Inorder(a)

