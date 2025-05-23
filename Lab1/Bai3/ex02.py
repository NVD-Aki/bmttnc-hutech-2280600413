def dao_nguoc_list(lst):
    """
    Hàm đảo ngược danh sách
    :param lst: Danh sách cần đảo ngược
    :return: Danh sách đã được đảo ngược
    """
    return lst[::-1]
input_list = input("Nhập danh sách số (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách đã được đảo ngược là:", list_dao_nguoc)