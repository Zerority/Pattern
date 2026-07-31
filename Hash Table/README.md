# Hash Table (Hash Map & Hash Set)

## Définition

Une **Hash Table** est une structure pour données permettant de stocker et de retrouver rapidement des informations.

En Python, une **Hash Table** est représentée principalement par deux structures :

- **Dictionary (`dict`)**, appelé **Hash Map** ;
- **Set (`set`)**, appelé **Hash Set**.

Grâce à une fonction de hachage (*hash function*), les opérations de recherche, d'insertion et de suppression s'effectuent en moyenne en **O(1)**.

Cette structure est très utilisée pour remplacer une recherche linéaire **O(n)** par un accès quasi instantané.

> **Remarque**
>
> La **Hash Table** est l'un des patterns les plus utilisés et les plus utilisés en algorithmique.
>
> De nombreux problèmes LeetCode peuvent être résolus ou considérablement simplifiés grâce à une **Hash Map** ou un **Hash Set**. Maîtriser cette structure de données est donc indispensable avant d'aborder des techniques plus avancées.

---

## Quand utiliser ce pattern ?

Une Hash Table est particulièrement utile lorsque le problème demande :

- vérifier rapidement si un élément existe ;
- compter la fréquence d'apparition d'éléments ;
- associer une clé à une valeur ;
- regrouper des éléments partageant une même caractéristique ;
- éliminer les doublons ;
- créer une section pour enregistrer les données. 

---

## Hash Map (Dictionary)

Une **Hash Map** associe une **clé (key)** à une **valeur (value)**.

Exemple :

```python
character = {
    "Little Knight": 18,
    "Hornet": 20
}
```

On peut accéder directement à une valeur grâce à sa clé.

```python
character["Hornet"]
```

Cette opération est réalisée en moyenne en **O(1)**.

---

### Cas d'utilisation

#### Vérifier l'existence d'une valeur

```python
seen = {}

for num in nums:

    if num in seen:
        ...

    seen[num] = True
```

---

#### Compter une fréquence

```python
freq = {}

for num in nums:

    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1
```

---

#### Grouper des éléments

```python
groups = {}

for word in strs:

    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)
```

---

## Hash Set

Un **Hash Set** stocke uniquement des valeurs uniques.

Contrairement à un dictionnaire, il ne contient pas de paires **clé → valeur**.

```python
visited = set()
```

---

### Cas d'utilisation

#### Éliminer les doublons

```python
unique = set(nums)
```

---

#### Vérifier rapidement l'existence d'un élément

```python
visited = set()

for num in nums:

    if num in visited:
        ...

    visited.add(num)
```

---

## Complexité

| Opération | Hash Map | Hash Set |
|-----------|----------|----------|
| Recherche | O(1) | O(1) |
| Insertion | O(1) | O(1) |
| Suppression | O(1) | O(1) |

---

## Comment reconnaître ce pattern ?

Pensez immédiatement à une **Hash Table** lorsque le problème demande :

- vérifier rapidement si un élément existe ;
- compter des occurrences ;
- retrouver une valeur à partir d'une clé ;
- regrouper des éléments similaires ;
- supprimer les doublons.

Les mots-clés sont souvent :

- frequency
- duplicate
- anagram
- lookup
- group
- contains

---

## Exercices

### Easy

- Two Sum
- Contains Duplicate
- Valid Anagram

### Medium

- Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence

### Hard

- Minimum Window Substring
