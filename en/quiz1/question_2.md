
--- question ---

---
legend: Question 2 of 3
---

Your project used data loaded from a file to let you chart hundreds of pieces of information. Which of these pieces of code would correctly load `data.csv` into a variable as a text string?

--- choices ---

- (x) 
```python
with open('data.csv') as f:
  info = f.read()
```
  --- feedback ---

  That's correct! This will load `data.csv` as `f` and then `read()` it into `info` as a text string.

  --- /feedback ---

- ( ) 
```python
open('data.csv') as f:
  info = f.read()
```

  --- feedback ---

  Not quite, this is very close, but it's missing something important at the start.

  --- /feedback ---

- ( ) 
```python
with open('data.csv') as f:
info = f.read()
```

  --- feedback ---
  
  Very close! This is all the correct code, but the indentation is wrong.

  --- /feedback ---

- ( ) 
```python
with open('data.csv') as f:
  info = read(f)
```

  --- feedback ---
  
  Not exactly — the `read()` function belongs to the file stored in `f`, so you have to call it with `.` instead of by passing `f` to it.

  --- /feedback ---

--- /choices ---

--- /question ---
