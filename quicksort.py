
def getchindx(ch):
    return ch[1]

def get_str_list():
    num = int(input("Enter the number of strings to be entered: "))

    while(num <= 0):
        print("Please enter a positive number.")
        num = int(input("Enter the number of strings to be entered: "))

    string_lst = []
    for i in range(num):
        str = input(f"Enter string {i + 1}: ")
        string_lst.append(str)
    return string_lst

if __name__ == "__main__":
    key = input("Enter key: ")

    result_list = get_str_list()

    print("Entered list of strings: " , result_list)
    print(f"Entered key is {key}")

    #for i in range(len(result_list)):
    #   print(result_list[i][1])
    key_dict = {}
    result_list_dict = []

    for index, element in enumerate(key):
        key_dict[element] = index

    for i in range(len(result_list)):
        result_list_dict.append((result_list[i],key_dict[result_list[i][0]]))

    sorted_result_list_dict = sorted(result_list_dict, key=getchindx)
    for i in range(len(sorted_result_list_dict)):
        print(sorted_result_list_dict[i][0])