def Dam_Levenstein(str1,str2):
    if str1 == '' and str2 == '':
        return True
        
    else:
        # Transposition = True? go into recursion
        if len(str1) >= 2 and len(str2) >=2:
            if str1[1] + str1[0] == str2[0] + str2[1]:
                str1=str1[2:]
                str2=str2[2:]
                Dam_Levenstein(str1,str2)
        # Deletion if deleting one char gives equals str2[0]
        if len(str1) > len(str2) and str1[1] == str2[0]:
            str1=str1[2:]
            str2=str2[1:]
            Dam_Levenstein(str1,str2)
        # Insertion
        if len(str1) < len(str2):
            str1= str2[0] + str1[0:]
            str2=str2[1:]
            str1=str1[1:]
            Dam_Levenstein(str1,str2)
    
        # Subsition
        if len(str1) == len(str2):
            str1= str2[0] + str1[0:]
            str2=str2[1:]
            str1=str1[1:]
            Dam_Levenstein(str1,str2)    

print(Dam_Levenstein('str','tsq'))
    