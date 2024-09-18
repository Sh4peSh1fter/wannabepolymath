# Code Blocks

## Language / Syntax

````
```py
print("yo")
```
````

<div class="result" markdown>

```py
print("yo")
```

</div>

## Title

````
```markdown title="title"
hello world
```
````

<div class="result" markdown>

```markdown title="title"
hello world
```

</div>

## line numbering

````
```py linenums="1"
def func():
    print("yo")
    return True
```
````

<div class="result" markdown>

```py linenums="1"
def func():
    print("yo")
    return True
```

</div>

## Annotations

doesnt work

```py
def func(): # (1)
    print("yo")
```

1.  yo comment

<div class="result" markdown>

```py
def func(): # (1)
    print("yo")
```

1.  yo comment

</div>
