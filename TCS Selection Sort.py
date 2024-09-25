def Selection_Sort(List):
    for i in range(len(List)-1):
        MinPosition=i
        for j in range(i+1,len(List)):
            if List[j]<List[MinPosition]:
                MinPosition=j
        List[i],List[MinPosition] = List[MinPosition],List[i]
                print(List)
    print("Final Result:-")
    return List
List1=[5,3,8,6,7,2]
print(Selection_Sort(List1))    
