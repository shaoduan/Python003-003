学习笔记

- Series
  - 创建
    ```
    # 不指定索引，则默认由0开始
    obj = Series([1,2,3,4])
    
    # 自定义索引
    obj2 = Series([1,2,3,4], index=['a', 'b', 'c', 'd'])

    # 使用字典创建
    sdata = {'a': 1, 'b': 2, 'c':3 }
    obj3 = Series(sdata)

    # 使用字典和列表创建, 存在于字典的key值，但是不存在于指定的index里的话，则该键值对被抛弃；
    # 存在于指定的index的值，但是不在字典的键中的话，该索引对应的值则为NaN
    sdata = {'a': 1, 'b': 2, 'c':3 }
    sindex = ['b', 'c', 'e']
    obj4 = Series(sdata, index=sindex)
    > out
    b    2.0
    c    3.0
    e    NaN
    dtype: float64
    ```
  
  - 访问
    ```
    sdata = {'a': 1, 'b': 2, 'c':3 }
    obj = Series(sdata)

    # 访问索引
    obj.index

    # 访问值
    obj.values

    # 通过索引访问值
    obj['a']

    # 指定多个索引
    obj[['a', 'b']]

    # 范围取, 此时index里的值应该属于同一类型
    obj['b':'d']
    ```
  
  - 修改
    ```
    sdata = {'a': 1, 'b': 2, 'c':3 }
    obj = Series(sdata)
    
    # 就地修改索引
    obj.index = [0, 1, 2, 3]

    # 修改值
    obj[0] = 4
    ```

  - 属性
    ```
    sdata = {'a': 1, 'b': 2, 'c':3 }
    obj = Series(sdata)

    # name属性
    obj.name = 'SomeName'

    # index的name属性
    obj.index.name = 'IndexName'
    ```

  - 运算
    ```
    sdata = {'a': 1, 'b': 2, 'c':3 }
    obj = Series(sdata)
    sdata2 = {'b': 2, 'c': 3, 'd': 4, 'e': 5 }
    obj2 = Series(sdata2)
    # in运算符, 判断值是否在index中
    'a' in obj # return True
    1 in obj   # return False

    # 乘法
    obj * 2   # 返回新对象
    obj + obj # 返回新对象
    obj[obj > 2] # 这里是使用obj的values来做判断
    obj + obj2 # 自动对其数据
    ```

- DataFrame
  - 创建
    ```
    # 每列数据要等长, 可以是列表或numpy数组
    data = {'city': ['a', 'a', 'a', 'b', 'b', 'b'], 
            'year': [2000, 2010, 2020, 2000, 2010, 2020], 
            'pop': [1.5, 1.7, 1.8, 1.4, 1.7, 2.0]}
    df = DataFrame(data)

    # 按照指定的顺序生成, debt列不存在直接补NaN
    df2 = DataFrame(data, columns=['year', 'city', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
    ```

  - 访问
    ```
    # 访问列
    df2.year
    df2['year']
    
    # 访问多列
    df2.loc[:, ['year', 'pop']]

    # 访问行
    df2.loc['two']

    # 访问多行
    df2.loc[['one','three'], :]

    # 访问单个数据
    df2.loc['two'].at['pop']
    ```

  - 修改
    ```
    # 修改行
    df2.loc['two'] = Series([2010, 'a', 1.8], index=['year', 'city', 'pop'])

    # 修改列
    val = Series([3.3, 4.4, 5.5], index=['three', 'four', 'five'])
    df2.debt = val
    ```

  - 聚合, 并联
    ```
    # union
    pd.concat([table1, table2]).drop_duplicates()

    # union all
    pd.concat([table1, table2]).drop_duplicates()

    # select id, count(DISTINCT order_id) from table group by id;
    df.loc[:, ['id', 'order_id']].groupby(['id'], axis=0)['order_id'].nunique()
    ```