nums = [1,4,6,8]
prefix = [0]
for i in range(len(nums)):
    num = prefix[-1] + nums[i]
    prefix.append(num)
print(prefix)

#Commencer avec le numéro 0 dans le "prefix sum", nums[i] => nums[0] => 1
#num = Prefix_sum[-1] => La dernière chiffre dans l'array, => num = 0 + 1 = 1 => Prefix_sum = [0,1]
#Après, Prefix_sum[-1] = 1, parce que 1 est la dernière chiffre maintenant, => num = 1 + 4 = 5
#Après cette boucle, => Prefix_sum = [0, 1, 5, 11, 19]
#Pour calculer la somme de cet array, par example, l'index 0 et l'index 3
#=>
answer = prefix[4] - prefix[0]
#Plus généralement :
answer = prefix[right+1] - prefix[left]
#Notes:
#Ici, "left" et "right" représentent la distance. 
#Pourquoi right + 1 ? 
#Parce que vous devez calculer la somme de l'index 1 et l'index 3 dans (nums)
#=> l'index 3 dans (nums) est l'index 3 + 1 = 4 dans Prefix Sum
