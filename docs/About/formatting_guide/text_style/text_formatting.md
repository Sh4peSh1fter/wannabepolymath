# Text Formatting

## Text Styles & Emphasis

=== "markdown"

    ```markdown
    - basic
    - ==highlight==
    - ^^underline^^
    - ~~strike through~~
    - *Italic*
    - **bold** or __bold__
    - ***bold italic***
    - subscript - H~2~O
    - superscript - 10^32-1
    - `dont kno`
    ```

    <div class="result" markdown>

    - basic
    - ==highlight==
    - ^^underline^^
    - ~~strike through~~
    - *Italic*
    - **bold** or __bold__
    - ***bold italic***
    - subscript - H~2~O
    - superscript - 10^32-1
    - `dont kno`

    </div>

=== "HTML"

    ```html
    - basic
    - <mark>highlight</mark>
    - <u>underline</u>
    - <del>strike through</del>
    - <em>Italic</em>
    - <strong>bold</strong>
    - <em><strong>bold italic</em></strong>
    - subscript - H<sub>2</sub>O
    - superscript - 10<sup>32-1</sup>
    - `dont kno`
    ```

    <div class="result" markdown>

    - basic
    - <mark>highlight</mark>
    - <u>underline</u>
    - <del>strike through</del>
    - <em>Italic</em>
    - <strong>bold</strong>
    - <em><strong>bold italic</em></strong>
    - subscript - H<sub>2</sub>O
    - superscript - 10<sup>32-1</sup>
    - `dont kno`

    </div>

## Marker Highlighting With HTML

```
we can <del class="critic">delete</del> and <ins class="critic">add</ins> text.
we can also <mark class="critic">mark</mark> or <span class="critic comment">comment out</span> text.

<div>
  <mark class="critic block">
    <p>
      this can also be applied on blocks.
    </p>
  </mark>
</div>
```

<div class="result" markdown>

we can <del class="critic">delete</del> and <ins class="critic">add</ins> text.
we can also <mark class="critic">mark</mark> or <span class="critic comment">comment out</span> text.

<div>
  <mark class="critic block">
    <p>
      this can also be applied on blocks.
    </p>
  </mark>
</div>

</div>
