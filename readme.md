# Toolbox

There are some small tools here.  

---

## Content

- [**readme**](#rename): Rename files.

---

## Rename.py

[Link](./sources/rename.py)  
A simple tool to rename files in a directory matching regular expression.  

#### **Language:**  
Python.  

#### **Usage:**  
`rename.py dir file_exp startpos endpos [test]`  
The matching files will rename into `filename[startpos: endpos]`.(Remember the `filename` is the prefix of file.  
If use 'test', it will just print the matching file and changes.  

（批量把 `dir` 目录下 的 `file_exp` 正则匹配的 文件 重命名，新的文件名是 `原文件名[startpos: endpos]`，文件名不含后缀，切片是跟 Python 的一致的，可以用 `[-3: -1]` 这样的格式）

#### **Example:**

1. `rename.py ./folder1 [0-9]{3}.mp4 -3 100 test` will show:
    ```
    mv011.mp4 --> 011.mp4
    mv022.mp4 --> 022.mp4
    ```

2. `rename.py ./folder1 [0-9]{3}.mp4 1 -1 test` will show:
    ```
    mv011.mp4 --> v01.mp4
    mv022.mp4 --> v02.mp4
    ```


---

## jj.py
[Link](./sources/jj.py)  
从 bilibili 搜索新番，再到 bilibilijj 得到 MP3/MP4/ASS 地址。  

#### **Language:**  
Python.  

#### **Usage:**  

`jj.py [search_name] page_num`  
用 `search_name` 搜索，共搜索 `page_num` 页，对里面的链接放到 bilibilijj 里解析到 MP3/MP4/ASS 地址。  
生成结果到 `res.md` Mardown 文件。

#### **Example:**

爬前 bilibili 新番搜索 2 页的「来自风平浪静的明天」。  
```
jj.py 来自风平浪静的明天 2
```

---


