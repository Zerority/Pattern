# Sliding Window

## Définition

Le **Sliding Window** (ou **Fenêtre Glissante**) est un pattern permettant de parcourir efficacement un tableau ou une chaîne de caractères en maintenant une **fenêtre** représentant une partie des données.

Au lieu de recalculer les informations pour chaque sous-tableau, la fenêtre se déplace progressivement en ajoutant un nouvel élément et en supprimant l'ancien lorsque cela est nécessaire.

Cette technique permet souvent de transformer une solution en **O(n²)** en une solution en **O(n)**.

---

## Quand utiliser ce pattern ?

Le Sliding Window est particulièrement utile lorsque le problème demande :

- un sous-tableau de taille fixe ;
- une sous-chaîne ;
- une somme maximale ou minimale ;
- une longueur maximale ou minimale ;
- un problème impliquant des éléments consécutifs.

> **Remarque**
>
> Le Sliding Window est l'un des patterns les plus utilisés sur LeetCode. Il permet d'optimiser de nombreux problèmes portant sur les tableaux et les chaînes de caractères en évitant de recalculer les mêmes informations.

---

# Principe

L'idée est de conserver une fenêtre représentant une partie du tableau.

Au lieu de repartir de zéro à chaque itération, on fait simplement glisser cette fenêtre vers la droite.

En pratique, il existe deux grandes catégories de Sliding Window.

---

# Les deux grandes catégories

## 1. Fenêtre de taille fixe

La taille de la fenêtre est connue à l'avance et ne change jamais.

Exemple :

Une fenêtre de taille **3**.

```text
[1 2 3] 4 5 6

↓

1 [2 3 4] 5 6

↓

1 2 [3 4 5] 6

↓

1 2 3 [4 5 6]
```

À chaque déplacement :

- un élément entre dans la fenêtre ;
- un élément en sort.

Cette approche est utilisée lorsque la taille du sous-tableau est imposée.

### Template

```python
window_sum = sum(nums[:k])

answer = window_sum

for right in range(k, len(nums)):

    window_sum += nums[right]
    window_sum -= nums[right - k]

    answer = max(answer, window_sum)
```

### Exemples

- Maximum Average Subarray I
- Sliding Window Maximum

---

## 2. Fenêtre de taille variable

La taille de la fenêtre change selon les contraintes du problème.

On utilise généralement deux pointeurs.

```python
left = 0

for right in range(len(nums)):
    ...
```

La fenêtre peut :

- s'agrandir ;
- se rétrécir.

Lorsque la condition n'est plus respectée, on déplace le pointeur `left` jusqu'à ce que la fenêtre redevienne valide.

### Template

```python
left = 0

for right in range(len(nums)):

    ...

    while condition_not_valid:

        ...

        left += 1

    ...
```

Cette version est la plus fréquente sur LeetCode.

### Exemples

- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum
- Longest Repeating Character Replacement
- Permutation in String

---

# Complexité

| Type | Temps | Mémoire |
|------|--------|----------|
| Fenêtre fixe | O(n) | O(1) |
| Fenêtre variable | O(n) | O(1) |

---

# Comment reconnaître ce pattern ?

Pensez immédiatement au Sliding Window lorsque le problème contient des expressions comme :

- longest
- shortest
- maximum
- minimum
- substring
- subarray
- contiguous
- consecutive

Si le problème demande un **segment continu**, le Sliding Window est souvent une bonne piste.

---

## 4. Confondre les deux catégories

Si la taille est imposée par l'énoncé :

➡️ Fenêtre fixe.

Si la taille dépend d'une condition :

➡️ Fenêtre variable.

---

# Exercices

## Fenêtre fixe

- Maximum Average Subarray I
- Sliding Window Maximum

## Fenêtre variable

- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Minimum Window Substring
- Minimum Size Subarray Sum
- Permutation in String

---

# Ce qu'il faut retenir

- Le Sliding Window permet de parcourir un segment continu efficacement.
- Il évite de recalculer les mêmes informations plusieurs fois.
- Il existe deux grandes catégories :
  - fenêtre de taille fixe ;
  - fenêtre de taille variable.
- Dans la plupart des cas, il permet de réduire une solution de **O(n²)** à **O(n)**.
