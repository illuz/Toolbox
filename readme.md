# Toolbox

There are some small tools here.  

---

## Content

- [**readme**](#rename): Rename files.

---

### Rename.py

[Link](./sources/rename.py)  
A simple tool to rename files in a directory matching regular expression.  

#### **Language:**  
Python.  

#### **Usage:**  
`rename.py dir file_exp startpos endpos [test]`  
The matching files will rename into `filename[startpos: endpos]`.(Remember the `filename` is the prefix of file.  
If use 'test', it will just print the matching file and changes.  

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

