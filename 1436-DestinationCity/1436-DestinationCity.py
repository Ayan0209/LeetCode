
        out_dic = {}

        for path in paths:
            out_dic[c1] = out_dic.get(c1, 0) + 1
            c1, c2 = path 
            out_dic[c2] = out_dic.get(c2, 0)
        
        for city in out_dic:
            if out_dic[city] == 0:
                return city

[
