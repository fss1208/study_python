sales_list = []     # 파일로부터 읽어온 일별 판매량 데이터 (합계와 평균 추가)
sum_index = -2      # sales_list의 sum index
avg_index = -1      # sales_list의 avg index
sum_list = []       # 상품별 판매량 합계
coffe_kind = 4      # 커피 종류
total_count = 0     # 판매량 데이터 개수 카운팅
# 데이터 읽어오기
path_file_list = __file__.split("\\")
read_file = __file__.replace(path_file_list[-1], "coffeeShopSales.txt")
with open(read_file, "rt") as f:
    for line in f:
        cell_list = line.split()
        if (len(sum_list) == 0):
            sum_list = [0 for i in range(len(cell_list) + 2)]
        day_sum, day_avg = 0, 0
        for i in range(len(cell_list)):
            if (cell_list[i].isdigit()):
                cell = int(cell_list[i])
                day_sum += cell; 
                sum_list[i] += cell
                sum_list[sum_index] += cell
                total_count += 1
        if (len(sales_list) == 0):
            cell_list.append("sum")
            cell_list.append("avg")
        else:
            cell_list.append(str(day_sum))
            cell_list.append(str(day_sum / coffe_kind))
        sales_list.append(cell_list)
# 데이터 출력하기
cell_width = 10
line_width = cell_width * len(sum_list)
print("-" * line_width)
for cell_list in sales_list:
    for cell in cell_list:
        print(cell.center(cell_width), end="")
    print()
    if (cell.isalpha()):
        print("-" * line_width)
sum_list[0] = "total"
sum_list[avg_index] = sum_list[sum_index] / total_count
print("-" * line_width)
for sum in sum_list:
    print(str(sum).center(cell_width), end="")
print()
print("-" * line_width)
