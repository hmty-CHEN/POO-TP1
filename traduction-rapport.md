# 中文报告：问题与回答

## 练习 1：识别兔子的特征

### 问题 1

> 哪些元素应当表示为属性？

属性为 `x`、`y`、`energie`、`age` 和 `vitesse`。

### 问题 2

> 兔子可以执行哪些动作？请至少提出三个方法。

方法为 `se_deplacer()`、`vieillir()` 和 `est_vivant()`。

### 问题 3

> 用 UML 表示你的类。

```mermaid
classDiagram
    class Lapin {
        +int x
        +int y
        +int energie
        +int age
        +int vitesse
    }
```

## 练习 6：多个对象

### 问题

> 为什么在这里使用对象列表比使用五个独立变量更有意义？

用对象列表可以通过循环遍历所有兔子，并把种群作为一个整体处理；如果用五个独立变量，相同代码就要为每只兔子重复一遍。

## 练习 7：识别重复

### 问题

> 哪种面向对象概念可以对这些共同特征进行因子化？

能够提取共同特征的概念是继承。

## 练习 10：特定行为

### UML 问题

> 补全 UML 图，并添加主要的属性和方法。

`Animal` 是父类。`Lapin` 增加 `fuir()`，`Loup` 增加 `chasser()`。

```mermaid
classDiagram
    class Animal {
        <<abstract>>
        +int x
        +int y
        +int energie
        +int age
        +int vitesse
        +se_deplacer()*
        +vieillir()
        +est_vivant() bool
    }
    class Lapin {
        +se_deplacer()
        +fuir()
    }
    class Loup {
        +se_deplacer()
        +chasser()
    }
    Animal <|-- Lapin
    Animal <|-- Loup
```

## 练习 12：多态

### 问题

> 为什么我们不需要写 `if isinstance(animal, Lapin)`？请用你自己的话解释什么是多态。

每个动物都有自己的 `se_deplacer()` 方法。遍历动物列表时，Python 会自动调用与对象实际类型对应的那个方法。因此，多态就是：同一条指令（例如 `animal.se_deplacer()`）根据对象的类产生不同的行为，而不需要判断对象类型。

## 练习 14：测试抽象

### 问题

> 尝试 `animal = Animal(10, 10)`。会发生什么？解释原因。

该语句会报错：

```text
TypeError: Can't instantiate abstract class Animal with abstract methods reproduire, se_deplacer
```

`Animal` 含有抽象方法（`se_deplacer()` 和 `reproduire()`），因此它是抽象类。Python 不允许直接创建 `Animal` 对象，只有实现了这些方法的 `Lapin` 和 `Loup` 这些具体类才能被实例化。

## 练习 15：封装能量

### 问题

> 思考如何保证能量不会变得不一致。

能量保存在受保护属性 `_energie` 中，只能通过只读属性 `energie` 读取，并且只能由对象自己的方法修改。`perdre_energie()` 使用 `max(0, ...)`，因此能量不会变成负数。像 `lapin.energie = -500` 这样的直接修改会被拒绝：

```text
AttributeError: can't set attribute
```

## 练习 17：距离

### 设计问题

> 这个功能应当属于 `Animal`、`Environnement`，还是一个独立函数？请论证你的选择。

它属于 `Animal`。距离只取决于两只动物的位置，把它放在 `Animal` 中可以让数据和用到它的行为保持在一起，并且可以直接写 `animal.distance_avec(autre)`，而无需让对象知道环境的存在。

## 练习 20：添加动物

### 问题

> “一个环境包含若干动物”体现了哪种面向对象概念？

组合（composition）。`Environnement` 拥有一个动物集合：它负责并管理这些动物（添加、删除、演化），但并不是继承它们。

## 练习 23：繁殖

### 设计问题

> `reproduire()` 方法应当定义在 `Animal`、`Proie`、`Lapin` 还是另一个类中？请论证你的选择。

繁殖条件是共通的，通过 `peut_se_reproduire()`（年龄 ≥ 5 且能量 ≥ 60）放在 `Animal` 中。但新个体的创建取决于物种：因此 `reproduire()` 在 `Animal` 中是抽象的，由 `Lapin` 和 `Loup` 各自实现，返回自身类的对象。

## 兔子的逃跑

### 采用的逃跑逻辑

探测半径定义在 `Animal` 中（默认 10）。`Lapin` 将其覆盖为 4，约为狼的 40%。超出该半径时，兔子不会做出反应，而是随机移动。

在探测范围内，兔子检查沿坐标轴可达的四个相邻格，选择与威胁之间**距离平方最大**的那一格，然后移动 1 格。这样每移动一格获得最大的距离增量。不使用对角移动，因为对角需要消耗 2 格行走量。

```python
def fuir(self, menace):
    meilleur = None
    meilleure_distance = -1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        distance = (menace.x - (self.x + dx)) ** 2 + (menace.y - (self.y + dy)) ** 2
        if distance > meilleure_distance:
            meilleure_distance = distance
            meilleur = (dx, dy)
    self.x += meilleur[0]
    self.y += meilleur[1]
```

逃跑是局部的：兔子不会预判狼的移动。由于狼每回合前进 2 格而兔子只有 1 格，在开阔地形中狼最终仍会追上。

## 整合 8：最终 UML 类图

### 问题

> 绘制一张表示你的设计的 UML 图。

```mermaid
classDiagram
    direction LR

    class Animal {
        <<abstract>>
        +int RAYON_DETECTION
        +int x
        +int y
        +int age
        +int vitesse
        +energie int
        +se_deplacer()*
        +reproduire()* Animal
        +agir(animaux)
        +vieillir()
        +perdre_energie(quantite)
        +gagner_energie(quantite)
        +est_vivant() bool
        +distance_avec(autre) float
        +detecter(autre) bool
        +peut_se_reproduire() bool
    }

    class Proie {
        <<abstract>>
        +se_deplacer()
        +fuir(menace)
        +se_nourrir()
        +agir(animaux)
    }

    class Predateur {
        <<abstract>>
        +se_deplacer()
        +rechercher_proies(animaux) list
        +se_deplacer_vers(cible)
        +chasser(proie)
        +agir(animaux)
    }

    class Lapin {
        +int RAYON_DETECTION = 4
        +reproduire() Lapin
    }

    class Loup {
        +int vitesse = 2
        +reproduire() Loup
    }

    class Environnement {
        +int largeur
        +int hauteur
        +list animaux
        +ajouter(animal)
        +supprimer_morts()
        +compter(espece) int
        +simuler_un_tour()
        +statistiques() dict
    }

    class Simulation {
        +int nombre_lapins
        +int nombre_loups
        +Environnement environnement
        +initialiser_populations()
        +executer(nombre_de_tours)
        +afficher_statistiques(tour)
    }

    Animal <|-- Proie
    Animal <|-- Predateur
    Proie <|-- Lapin
    Predateur <|-- Loup
    Environnement "1" *-- "0..*" Animal : contient
    Simulation "1" --> "1" Environnement : pilote

    note for Animal "Lecture du diagramme :<br/>1. nom de la classe<br/>2. attributs (donnees) : ex. +int x<br/>3. methodes (parametres) : ex. +fuir(menace)<br/>Signes : + public, * methode abstraite, <<abstract>> classe abstraite"
```

图中体现了继承（`Animal` → `Proie` / `Predateur` → `Lapin` / `Loup`）、`Environnement` 与动物之间的组合关系，以及驱动环境的 `Simulation`。抽象类用构造型 `<<abstract>>` 标出。

## 整合 9：单元测试

### 问题

> 至少创建题目要求的测试，并用 unittest 运行。

- 测试 1 — 创建：年龄 = 0，能量 = 100。
- 测试 2 — 变老：一个回合后年龄增加、能量减少。
- 测试 3 — 死亡：能量为 0 的动物视为死亡。
- 测试 4 — 移动：坐标按一格的位移改变。
- 测试 5 — 捕猎：兔子死亡，狼获得能量。
- 测试 6 — 环境：添加的动物数量正确。
- 测试 7 — 删除：死亡的动物被移除。

测试集中在 `test_animal.py` 和 `test_environnement.py` 中，运行：

```bash
python -m unittest
```

八个测试全部通过。
