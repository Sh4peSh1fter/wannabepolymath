# Tables

to use this add the following to the mkdocs.yaml:

```
markdown_extensions:
  - tables
```

## Basic Table

```markdown
| Title | Description |
| ----- | ----------- |
| `hey` | hello       |
| `yo`  | sup         |
```

<div class="result" markdown>

| Title | Description |
| ----- | ----------- |
| `hey` | hello       |
| `yo`  | sup         |

</div>

## Column alignment

=== "Left"

    ``` markdown
    | Title | Description |
    | :----- | :----------- |
    | `hey` | hello |
    | `yo` | sup |
    ```

    <div class="result" markdown>

    | Title | Description |
    | :----- | :----------- |
    | `hey` | hello |
    | `yo` | sup |

    </div>

=== "Center"

    ``` markdown
    | Title | Description |
    | :-----: | :-----------: |
    | `hey` | hello |
    | `yo` | sup |
    ```

    <div class="result" markdown>

    | Title | Description |
    | :-----: | :-----------: |
    | `hey` | hello |
    | `yo` | sup |

    </div>

=== "Right"

    ``` markdown
    | Title | Description |
    | -----: | -----------: |
    | `hey` | hello |
    | `yo` | sup |
    ```

    <div class="result" markdown>

    | Title | Description |
    | -----: | -----------: |
    | `hey` | hello |
    | `yo` | sup |

    </div>

## Sortable Columns

=== ":octicons-file-code-16: `docs/javascripts/tablesort.js`"

    ``` js
    document$.subscribe(function() {
      var tables = document.querySelectorAll("article table:not([class])")
      tables.forEach(function(table) {
        new Tablesort(table)
      })
    })
    ```

=== ":octicons-file-code-16: `mkdocs.yml`"

    ``` yaml
    extra_javascript:
      - https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js
      - javascripts/tablesort.js
    ```

After applying the customization, data tables can be sorted by clicking on a
column:

```markdown title="Data table, columns sortable"
| Method   | Description                          |
| -------- | ------------------------------------ |
| `GET`    | :material-check: Fetch resource      |
| `PUT`    | :material-check-all: Update resource |
| `DELETE` | :material-close: Delete resource     |
```

<div class="result" markdown>

| Method   | Description                          |
| -------- | ------------------------------------ |
| `GET`    | :material-check: Fetch resource      |
| `PUT`    | :material-check-all: Update resource |
| `DELETE` | :material-close: Delete resource     |

</div>
