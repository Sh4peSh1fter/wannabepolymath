# Images

## Image Alignment

=== "Left"

    ``` markdown
    ![Image title](https://dummyimage.com/600x400/eee/aaa){ align=left }

    yo
    ```

    <div class="result" markdown>

    ![Image title](https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–){ align=left width=300 }

    yo

    </div>

=== "Right"

    ``` markdown
    ![Image title](https://dummyimage.com/600x400/eee/aaa){ align=right }

    yo
    ```

    <div class="result" markdown>

    ![Image title](https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–){ align=right width=300 }

    yo

    </div>

=== "Center"

## Image Captions

```html title="Image with caption"
<figure markdown="span">
  ![Image title](https://dummyimage.com/600x400/){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>
```

<div class="result">
  <figure>
    <img src="https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–" width="300" />
    <figcaption>Image caption</figcaption>
  </figure>
</div>
