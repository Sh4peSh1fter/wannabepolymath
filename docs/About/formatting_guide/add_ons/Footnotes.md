# Footnotes

```
markdown_extensions:
  - footnotes
```

```
theme:
  features:
    - content.footnote.tooltips
```

## Basic Footnote references

```
Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
```

<div class="result" markdown>

Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

</div>

## Basic Footnote Content

=== "single line"

    ``` markdown
    [^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    ```

=== "multiple lines"

    ```
    [^2]:
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.
    ```

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus
    auctor massa, nec semper lorem quam in massa.
