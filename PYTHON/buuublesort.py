def bubble_sort(items): 
    length = len(items)
    passes = 1
    while length > passes:
        for x in range(length-1):
            if items[x] > items[x+1]:
                y = items[x]
                items[x] = items[x+1]
                items[x+1] = y
        passes = passes + 1

    print(items)

itemlist = ["Flynn", "Callum", "Harrison", "Max"]
bubble_sort(itemlist)