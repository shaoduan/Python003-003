```
1. SELECT * FROM data;
df2

2. SELECT * FROM data LIMIT 10;
df2.iloc[:10]

3. SELECT id FROM data;  //id 是 data 表的特定一列
df2['id']  # 取自定义的id列
df2.index  # 类似于mysql的特殊列: row_id

4. SELECT COUNT(id) FROM data;
df2['id'].count()

5. SELECT * FROM data WHERE id<1000 AND age>30;
df2[(df2['year'] < 1000) & (df2['age'] > 30) ]

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# axis: 0:index, 1:column
df.loc[:, ['id', 'order_id']].groupby(['id'], axis=0)['order_id'].nunique()

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(t1, t2, on='id')

8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2]).drop_duplicates()

9. DELETE FROM table1 WHERE id=10;
df2.drop(index=[10], inplace=True)

10. ALTER TABLE table1 DROP COLUMN column_name;
df2.drop(columns=[column_name], inplace=True)
```