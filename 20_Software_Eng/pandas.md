## TextBook: Pandas Cookbook Third Edition 

### Introduction

`pd.Series` 1D Data

`pd.DataFramme` 2D Data

`pd.Index` `pd.RangeIndex`

`pd.Series(range(3), dtype="int8")`

`pd.Series(["apple", "banana", "orange"], name="fruit")`

```py
ser1 = pd.Series(range(3), dtype="int8", name="int8_col")
ser2 = pd.Series(range(3), dtype="int16", name="int16_col")
pd.DataFrame({ser1.name: ser1, ser2.name: ser2})

pd.DataFrame({
    "first_name": ["Jane", "John"],
    "last_name": ["Doe", "Smith"],
})

pd.DataFrame([
    [1, 2],
    [4, 8],
], columns=["col_a", "col_b"])
```

`pd.Series([4, 4, 2], index=["dog", "cat", "human"])`


```py
index = pd.Index(["dog", "cat", "human"], name="animal")
pd.Series([4, 4, 2], name="num_legs", index=index)

pd.DataFrame([
    [24, 180],
    [42, 166],
], columns=["age", "height_cm"], index=["Jack", "Jill"])
```

```py
index = pd.Index(["dog", "cat", "human"], name="animal")
ser = pd.Series([4, 4, 2], name="num_legs", index=index)
ser

ser.dtype
ser.name
ser.index
ser.index.name
ser.shape
ser.size
len(ser)
```

```py
index = pd.Index(["Jack", "Jill"], name="person")
df = pd.DataFrame([
    [24, 180, "red"],
    [42, 166, "blue"],
], columns=["age", "height_cm", "favorite_color"], index=index)
df

df.dtypes
df.index
df.columns
df.shape
df.size
len(df)
```

```py
ser = pd.Series(list("abc") * 3)
ser

ser[3]
ser[[3]]
ser[[0, 2]]
ser[:3]
ser[-4:]
ser[2:6]
ser[1:8:3]

ser = pd.Series(list("abc"), index=[2, 42, 21])
ser

ser[2]
ser[:2]

ser = pd.Series(["apple", "banana", "orange"], index=[0, 1, 1])
ser

ser[1]
```

```py
df = pd.DataFrame(np.arange(9).reshape(3, -1), columns=["a", "b", "c"])
df

df["a"]
df[["a"]]
df[["a", "b"]]

df[:2]
```


```py
ser = pd.Series(["apple", "banana", "orange"], index=[0, 1, 1])
ser

ser.iloc[1]
ser.iloc[[1]]
ser.iloc[[0, 2]]
ser.iloc[:2]
```

```py
df = pd.DataFrame(np.arange(20).reshape(5, -1), columns=list("abcd"))
df

df.iloc[2, 2]
df.iloc[:, 0]
df.iloc[0, :]

df.iloc[:, [0]]
df.iloc[[0], :]
df.iloc[[0, 1], [-1, -2]]

ser.iloc[:]
df.iloc[:, :]
```

```py
ser = pd.Series(["apple", "banana", "orange"], index=[0, 1, 1])
ser

ser = pd.Series([2, 2, 4], index=["dog", "cat", "human"], name="num_legs")
ser

ser.loc["dog"]
ser.loc[["dog", "cat"]]
ser.loc[:"cat"]


values = ["Jack", "Jill", "Jayne"]
ser = pd.Series(values)
ser

values[:2]
ser.iloc[:2]
ser.loc[:2]

repeats_2 = pd.Series(range(5), index=[0, 1, 2, 2, 0])
repeats_2.loc[:2] # loc, python does label based indexing

ser = pd.Series(range(4), index=["zzz", "xxx", "xxx", "yyy"])
ser.loc[:"xxx"] # stop until you find a different index

ser = pd.Series(range(4), index=["zzz", "xxx", "yyy", "xxx"])
ser.loc[:"xxx"] # raises error; no determinate ordering
```

```py
df = pd.DataFrame([
    [24, 180, "blue"],
    [42, 166, "brown"],
    [22, 160, "green"],
], columns=["age", "height_cm", "eye_color"], index=["Jack", "Jill", "Jayne"])
df

df.loc["Jayne", "eye_color"]
df.loc[:, "age"]
df.loc["Jack", :]
df.loc[:, ["age"]]
df.loc[["Jack"], :]
df.loc[["Jack", "Jill"], ["age", "eye_color"]]
```

```py
df = pd.DataFrame([
    [24, 180, "blue"],
    [42, 166, "brown"],
    [22, 160, "green"],
], columns=["age", "height_cm", "eye_color"])
df

col_idxer = df.columns.get_indexer(["age", "eye_color"]) # array([0, 2])
df.iloc[[0, 1], col_idxer]

df[["age", "eye_color"]].iloc[[0, 1]]

import timeit
def get_indexer_approach():
  col_idxer = df.columns.get_indexer(["age", "eye_color"])
  df.iloc[[0, 1], col_idxer]
timeit.timeit(get_indexer_approach, number=10_000) # fast

two_step_approach = lambda: df[["age", "eye_color"]].iloc[[0, 1]]
timeit.timeit(two_step_approach, number=10_000) # slow


```