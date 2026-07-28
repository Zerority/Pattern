# Prefix Sum

## Définition

La somme préfixe est une technique qui consiste à construire un tableau contenant la somme cumulée d'un tableau initial.

Grâce à cette structure, il est possible de sommer n'importe quel sous-tableau en temps constant (O(1)) après une phase de prétraitement en temps O(n)).

Cette technique permet souvent de transformer une solution en O(n²) en une solution en O(n).

---

## Quand utiliser ce pattern ?

Le Prefix Sum est particulièrement utile lorsque le problème demande :

- la somme d'un intervalle ;
- plusieurs requêtes de sommes sur un même tableau ;
- l'optimisation d'une solution utilisant deux boucles imbriquées.

---

## Principe

Soit le tableau suivant :

```text
nums = [3, 4, 6, 2, 5]
```

On construit un nouveau tableau `prefix`.

La première valeur est toujours égale à **0**.

```text
prefix = [0]
```

Ensuite, on ajoute progressivement les sommes cumulées.

```text
prefix = [0, 3, 7, 13, 15, 20]
```

Chaque élément représente la somme de tous les éléments précédents.

Par exemple :

```text
prefix[3] = 13

= 3 + 4 + 6
```

---

## Construction

```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)
```

### Complexité

- Temps : **O(n)**
- Mémoire : **O(n)**

---

## Calcul d'une somme

Pour calculer la somme entre les indices `left` et `right` (inclus) :

```text
Somme = prefix[right + 1] - prefix[left]
```

Exemple :

```text
nums = [3, 4, 6, 2, 5]

prefix = [0, 3, 7, 13, 15, 20]
```

Calcul de la somme de :

```text
[4, 6, 2]
```

c'est-à-dire des indices `1` à `3`.

```text
prefix[4] - prefix[1]

15 - 3 = 12
```

Résultat :

```text
4 + 6 + 2 = 12
```

Le calcul se fait en **O(1)**.

---

## Modèle

```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)

answer = prefix[right + 1] - prefix[left]
```

---

## Complexité

| Étape | Complexité |
|--------|------------|
| Construction | O(n) |
| Une requête | O(1) |

---

## Comment reconnaître ce pattern ?

Pensez au **Prefix Sum** lorsque le problème parle de :

- somme d'un intervalle ;
- plusieurs requêtes sur un même tableau ;
- optimisation d'une solution en O(n²) vers O(n).

Le mot-clé est souvent **"sum"**, **"range sum"**, **"subarray"** ou **"intervalle"**.

---

## Problèmes classiques

- Range Sum Query - Immutable
- Find Pivot Index
- Subarray Sum Equals K
- Continuous Subarray Sum
