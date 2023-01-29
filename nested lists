if __name__ == '__main__':
    empty_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        empty_list.append([name,score]) 
    result=sorted(set(score for name,score in empty_list))
    x=result[1]
    y=list(sorted(name for name,score in empty_list if score==x))
    for x in y:
        print(x)
        