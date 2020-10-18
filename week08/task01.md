```
作业一：
区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

    list
    tuple
    str
    dict
    collections.deque
```

- 容器序列：可以存放不同类型的数据。即可以存放任意类型对象的引用。
    - list tuple collections.deque 

- 扁平序列：只能容纳一种类型。也就是说其存放的是值而不是引用。
    - str

- 可变序列: 长度可变，元素指向可变
    - list collections.deque

- 不可变序列：长度不可变，元素指向不可变
    - str tuple