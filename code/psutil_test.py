import psutil

dict_level_a = {}


#获取节点的编号value
def  key_value(node):
    if(dict_level_a.keys(node)):
        return dict_level_a.get(node)
    else:
        return None

def  get_node_index():
    values_list = dict_level_a.values()
    for i in values_list:
        pass


def process_list():
    lists = psutil.pids()
    print( lists )
    file_lists = []
    for i in lists:
        if(i>=150):
            p = psutil.Process(i)
            file_lists.append(str(p.exe())+'['+str(i)+']')
    # print(file_lists)
    files = {}
    for i in file_lists:
        #分解单个文件
        temp_str = i.split('\\')
        print( temp_str )
        #ii代表节点级别
        for ii in range(len(temp_str)):
            a=0
            #查询是否有node
            
            #节点字典没有node
            if(key_value(temp_str[ii])==None):
                values_list=dict_level_a.values()
                #第一级都没有，后面的节点都不会有，哪一级节点没有，后面的都要登记上
                if(ii==0):
                    max = 0
                    index=1
                    #查编号
                    for i in values_list:
                        if(len(ii)==1):
                           if(int(i)>=max):
                               max=i+1
                        if(len(ii)==2):
                            if(int(i)>=max):
                                max=i+1
                        if(len(ii)==3):
                            dict_level_a['temp_str[ii']=str(ii)

        print('*'*50)
    print(files)
            





if __name__=='__main__':
    process_list()
