def konversi():
    list1 = [1, 2, 3, 4, 5]
    print("List sebelum konversi:", list1)
    listkeset = set(list1)
    print("List menjadi Set:", listkeset)
    
    set1 = {1, 2, 3, 4, 5}
    print("Set sebelum konversi:", set1)
    setkelist = list(set1)
    print("Set menjadi List:", setkelist)
    
    tuple1 = (1, 2, 3, 4, 5, 5, 4)
    print("Tuple sebelum konversi:", tuple1)
    tuplekeset = set(tuple1)
    print("Tuple menjadi Set:", tuplekeset)
    
    set2 = {1, 2, 3, 4, 5}
    print("Set sebelum konversi:", set2)
    setketuple = tuple(set2)
    print("Set menjadi Tuple:", setketuple)

konversi()
