from LinkedList.linked_list import LinkedList

if __name__ == '__main__':
    my_list = LinkedList(20)
    print(my_list)

    my_list.append(5)
    my_list.append(7)
    my_list.append(100)
    my_list.insert(2, 100)
    my_list.insert(20, 80)
    print(my_list)

    my_list[1] = 16
    print(my_list)
    my_list[-1] = 30
    print(my_list)

    my_list.delete(-1)
    print(my_list)
    my_list.delete(0)
    print(my_list)
