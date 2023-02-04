#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Mama' , 'Sistra' , 'Papa' , 'I' , 'Dedywka']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Luda' , 161],
    ['Kristina', 168],
    ['Vasya', 172],
    ['Vova', 183],
    ['Nikolay',186]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост:'+my_family[2]+' -', my_family_height[2][1],'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = 0
sum +=my_family_height[0][1]
sum +=my_family_height[1][1] 
sum +=my_family_height[2][1] 
sum +=my_family_height[3][1]  
sum +=my_family_height[4][1]
print('Общий рост моей семьи - ', sum ,'см') 