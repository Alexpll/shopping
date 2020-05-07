class Shop:
    def save_changes(file_name):
        pass

    def load_data(file_name, rewrite=False):
        pass

    def user_buy(user_name, shop_name, product_name, count, save_check=False):
        pass

    def find_product(product_name, count=-1):
        pass

    def sort_shops_by_product_price(product):
        pass

    def sort_shops_by_product_count(product):
        pass


dict_lines = {}
text = open("shops.txt")
count = 0
for line in text:
    new_list = []
    lst = line.split(':')
    lst[1] = lst[1].strip('\n').split(', ')
    for i in lst[1]:
        i = i.split(',')
        new_i = []
        for x in i:
            if x.isdigit():
                x = int(x)
                new_i.append(x)
            else:
                new_i.append(x)
        new_list.append(new_i)
    dict_lines[lst[0]] = new_list
text.close()
print(dict_lines)