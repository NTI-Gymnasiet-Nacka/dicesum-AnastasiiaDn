# Dice sum probability calculator
# Författare: Anastasiia
# Datum: 2024-08-21

# d4_1=[1,2,3,4]
# d4_2 =[1,2,3,4]
# for i in d4_1:
#  for j in d4_2:  
#     print (i,j)  



def main():

    user_input = input().split(" ")

    dice_sums = []

    for i in range(1, int(user_input[0])+1):
        for j in range(1, int(user_input[1])+1):
            dice_sums.append(i+j)
        print(max(set(dice_sums), key =dice_sums.count ))
      
      


if __name__ == "__main__":
    main() 