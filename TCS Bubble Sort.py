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

# Best case Approach
def Bubble_Sort(List):
    for i in range(len(List)-1,0,-1):
        Swapped=False
        for j in range(i):
            if List[j]>List[j+1]:
                List[j],List[j+1] = List[j+1],List[j]
                Swapped=True
              
        if not Swapped:
            break
        
    print("Final Result:- ")
    return List

List1=[1,2,3,4,5]
print(Bubble_Sort(List1))
