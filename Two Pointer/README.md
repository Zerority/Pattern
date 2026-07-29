# Two Pointers

## Définition

Le **Two Pointers** est un pattern qui utilise deux indices pour parcourir un tableau ou une chaîne de caractères.

Selon le problème, les deux pointeurs peuvent être placés de différentes manières : aux deux extrémités du tableau, au même point de départ ou encore avancer à des vitesses différentes.

Cette technique permet souvent de remplacer une solution utilisant deux boucles imbriquées **O(n²)** par une solution linéaire en **O(n)**.

---

## Quand utiliser ce pattern ?

Le Two Pointers est particulièrement utile lorsque le problème demande :

- rechercher une paire d'éléments ;
- parcourir un tableau trié ;
- supprimer ou déplacer des éléments ;
- comparer deux parties d'un tableau ou d'une chaîne ;
- optimiser une solution utilisant deux boucles.

---

## Principe

Le placement des pointeurs dépend du problème à résoudre.

Les deux approches les plus courantes sont :

- deux pointeurs aux extrémités du tableau ;
- deux pointeurs **Fast & Slow**.

---

# Two Pointers (Left & Right)

Les pointeurs sont placés aux deux extrémités du tableau.

```python
left = 0
right = len(nums) - 1
```

Ils se rapprochent progressivement jusqu'à se rencontrer.

Exemple : trouver deux nombres dont la somme est égale à une valeur cible.

```python
left = 0
right = len(nums) - 1

while left < right:

    total = nums[left] + nums[right]

    if total == target:
        return [left, right]

    elif total > target:
        right -= 1

    else:
        left += 1
```

### Complexité

- Temps : **O(n)**
- Mémoire : **O(1)**

---

# Fast & Slow Pointers

Dans cette variante, les deux pointeurs commencent généralement au début du tableau.

```python
slow = 0

for fast in range(len(nums)):
    ...
```

Le comportement du pointeur `slow` dépend entièrement du problème.

Quelques exemples :

- supprimer les doublons ;
- déplacer les zéros ;
- compresser un tableau ;
- partitionner un tableau.

Le pointeur `fast` parcourt tous les éléments tandis que `slow` ne se déplace que lorsqu'une condition est satisfaite.

---

## Template

### Left & Right

```python
left = 0
right = len(nums) - 1

while left < right:

    if condition:
        ...

    elif ...:
        right -= 1

    else:
        left += 1
```

### Fast & Slow

```python
slow = 0

for fast in range(len(nums)):

    if condition:
        ...
        slow += 1
```

---

## Complexité

| Approche | Temps | Mémoire |
|----------|--------|----------|
| Left & Right | O(n) | O(1) |
| Fast & Slow | O(n) | O(1) |

---

## Comment reconnaître ce pattern ?

Pensez immédiatement au **Two Pointers** lorsque le problème demande :

- trouver une paire de valeurs ;
- parcourir un tableau trié ;
- supprimer des éléments sans créer un nouveau tableau ;
- déplacer des éléments vers une extrémité ;
- comparer deux parties d'un tableau ;
- optimiser une solution utilisant deux boucles imbriquées.

Les mots-clés sont souvent :

- **pair**
- **sorted array**
- **remove**
- **move**
- **palindrome**
- **two pointers**

---

## Exercices

### Easy

- Valid Palindrome
- Two Sum II - Input Array Is Sorted
- Merge Strings Alternately
- Remove Duplicates from Sorted Array
- Move Zeroes

### Medium

- 3Sum
- Container With Most Water
- Sort Colors

### Hard

- Trapping Rain Water
