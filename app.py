# task1
# def kvadrat_ededleri_tap(mylist):
#     kvadratlar = [x for x in mylist if x >= 0 and (x**0.5) % 1 == 0]
#     print("Listdəki kvadrat ədədlər:")
#     for eded in kvadratlar:
#         print(eded)

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# kvadrat_ededleri_tap(mylist)





# task2

# def tekrarlanmayan_elementleri_tap(input_list):
#     tekrarlanmayanlar = []
#     for element in input_list:
#         if input_list.count(element) == 1:
#             tekrarlanmayanlar.append(element)
#     return tekrarlanmayanlar

# input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']
# print("Tekrarlanmayan elementlər:", tekrarlanmayan_elementleri_tap(input_list))







# # task4

# def bolunenleri_tap(number):
#     return [x for x in range(1, number + 1) if number % x == 0]


# number = 24
# print(f"{number} ədədin bölənləri: {bolunenleri_tap(number)}")




# task5
# mylist = ['may', 'iyun', 'iyul']
# month_lengths = {month: len(month) for month in mylist}

# print(month_lengths)


# task6


# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# def adlari_tap(names):
#     adlar = [name.split()[0].lower() for name in names]
#     return adlar

# print(adlari_tap(names))



# task7



nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

def ortalama(nums1, nums2):
    results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
    return results

print(ortalama(nums1, nums2))
