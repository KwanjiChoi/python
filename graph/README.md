## ネットワークグラフ

![graph](https://user-images.githubusercontent.com/55664594/112824146-2219b800-90c5-11eb-908f-ec2cdc2f0132.png)


### 有向グラフ 無向グラフ
辺が向きを持つグラフを有向グラフ
向きを持たないグラフを無向グラフ


## 隣接行列 隣接リスト
グラフ構造をプログラムで保持する方法

### 隣接行列
 - 拡張点間の辺の情報を行列で表したもの
 - 頂点数が多いグラフはメモリ不足にな、保存する情報が頂点の2乗


```

graph = [
  [False, True,  True, False],
  [True,  False, True, False],
  [True,  True,  False, True],
  [False, False, True, False]
]
```

の場合

頂点sが頂点tに辺を持っているかどうかはgraph[s][t]を見れば良い


### 隣接リスト
- 頂点ごとに辺の情報をまとめた配列
- 保存する情報は辺の数に比例

```
graph = [
  [1,2],
  [0,2],
  [0,1,3],
  [2]
]
```

頂点sから出る辺の行き先をgraph[s]で参照




