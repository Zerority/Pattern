# Binary Search

## Définition

Le **Binary Search** (ou **Recherche Binaire**) est un algorithme permettant de rechercher rapidement une valeur dans un **tableau trié**.

Cette idée est très proche d'une situation de la vie quotidienne : lorsque l'on cherche un mot dans un dictionnaire, on ne commence jamais à la première page. On ouvre le dictionnaire approximativement au milieu, puis on décide de continuer vers la gauche ou vers la droite selon la position du mot recherché.

En réduisant l'espace de recherche de moitié à chaque étape, le Binary Search atteint une complexité de **O(log n)**.

---

## Quand utiliser ce pattern ?

Le Binary Search est particulièrement utile lorsque :

- le tableau est déjà trié ;
- il faut retrouver rapidement une valeur ;
- le problème demande de trouver une position, une limite ou une valeur optimale ;
- une recherche en **O(n)** est trop coûteuse.

> **Remarque**
>
> Le Binary Search est l'un des patterns fondamentaux en algorithmique. Il est très fréquent dans les problèmes LeetCode et constitue souvent la meilleure solution lorsqu'un tableau est trié ou lorsqu'une condition est monotone.

---

# Principe

On initialise deux pointeurs.

```python
left = 0
right = len(nums) - 1
```

À chaque itération, on calcule l'indice du milieu.

```python
mid = left + (right - left) // 2
```

Puis on compare `nums[mid]` avec la cible.

- Si la valeur est trouvée, on retourne son indice.
- Si la cible est plus grande, on continue dans la moitié droite.
- Si la cible est plus petite, on continue dans la moitié gauche.

À chaque comparaison, environ **50 %** des éléments sont éliminés.

---

# Les deux grandes catégories

En pratique, la plupart des problèmes utilisant le Binary Search appartiennent à l'une des deux catégories suivantes.

## 1. Binary Search traditionnel

L'objectif est de retrouver directement une valeur présente dans un tableau trié.

```python
if nums[mid] == target:
    return mid

elif nums[mid] < target:
    left = mid + 1

else:
    right = mid - 1
```

### Exemples

- Binary Search
- Search Insert Position
- Guess Number Higher or Lower

---

## 2. Binary Search sur une condition

Dans certains problèmes, la réponse n'est pas directement présente dans le tableau.

On cherche plutôt **la première valeur qui satisfait une condition**.

Au lieu de demander :

> « Est-ce que cette valeur est la réponse ? »

on demande :

> « Est-ce que cette valeur satisfait la condition ? »

La condition ressemble souvent à ceci :

```text
False False False False True True True True
```

Le Binary Search consiste alors à trouver :

- le premier **True** ;
- ou le dernier **False**.

Cette technique est également connue sous le nom de **Binary Search on Answer**.

### Exemple

Supposons que l'on cherche la vitesse minimale permettant de terminer un travail.

On ne connaît pas directement cette vitesse.

En revanche, on peut vérifier :

```text
10 est-elle suffisante ?

Oui.
```

ou

```text
5 est-elle suffisante ?

Non.
```

La réponse est donc trouvée en effectuant une recherche binaire sur les valeurs possibles.

### Exemples

- Koko Eating Bananas
- Capacity To Ship Packages Within D Days
- Minimize Maximum of Array

---

# Template

## Binary Search traditionnel

```python
left = 0
right = len(nums) - 1

while left <= right:

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

return -1
```

---

## Binary Search sur une condition

```python
left = minimum_possible_answer
right = maximum_possible_answer

while left < right:

    mid = left + (right - left) // 2

    if condition(mid):
        right = mid

    else:
        left = mid + 1

return left
```

---

# Pourquoi le Binary Search est-il si rapide ?

Une recherche classique examine les éléments un par un.

```text
1 → 2 → 3 → 4 → 5 → ...
```

Complexité :

```text
O(n)
```

Avec le Binary Search, le nombre d'éléments est divisé par deux à chaque étape.

```text
1024

↓

512

↓

256

↓

128

↓

64

↓

32

↓

16

↓

8

↓

4

↓

2

↓

1
```

Même pour un très grand tableau, quelques comparaisons suffisent.

C'est pourquoi sa complexité est :

```text
O(log n)
```

---

# Complexité

| Opération | Complexité |
|-----------|------------|
| Recherche | O(log n) |
| Mémoire | O(1) |

---

# Exercices

## Easy

- Binary Search
- Search Insert Position
- Guess Number Higher or Lower

## Medium

- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Koko Eating Bananas

## Hard

- Median of Two Sorted Arrays

# Ce qu'il faut retenir

- Le tableau doit être trié.
- À chaque comparaison, on élimine la moitié de l'espace de recherche.
- Le Binary Search n'est pas seulement utilisé pour rechercher une valeur, mais aussi pour rechercher une réponse satisfaisant une condition.
