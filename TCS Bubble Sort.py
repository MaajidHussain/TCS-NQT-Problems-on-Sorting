def Bubble_Sort(List):
    for i in range(len(List)-1,0,-1):
        for j in range(i):
            if List[j]>List[j+1]:
                List[j],List[j+1] = List[j+1],List[j]
                print(List)
        print("End of",i ,"iteration")
    print("Final Result:- ")
    return List
List=[64, 34, 25,90, 12, 22, 11]
print(Bubble_Sort(List))