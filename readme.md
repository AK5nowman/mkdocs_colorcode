# Summary
Mkdocs plugin to generate a color swatch when a color code is used.

# How To Use
Every instance of `<AARRGGBB>` and `<RRGGBB>`, if a valid color, will be replaced with a color swatch.

## Custom Style Sheet
A custom style sheet needs to be added to the mkdocs configuration
``` yml
extra_css:
  - path/to/style.css
```

Style sheet contents:
``` css
.color-block {
  display:inline-block;
  border-radius: .25rem;
  padding-left: .5em;
  background-color: var(--md-code-bg-color);
}
.color-swatch {
  display:inline-block; 
  line-height:1;
  margin-left:4px; 
  vertical-align: middle; 
  border-radius: .25rem;
  width: 2em;
  height: 2em; 
  background: #fff;
  background-image: 
    linear-gradient(135deg, #dcdcde 25%, transparent 0%, transparent 75%, #dcdcde 0%),
    linear-gradient(135deg, #dcdcde 25%, transparent 0%, transparent 75%, #dcdcde 0%);
  background-size: 1em 1em;
  background-position: 0 0, .5em .5em;
}

.tooltip > span,
.color-swatch > span {
  display: inline-block;
  width: 100%;
  height: 100%;
  border-radius: .25rem;
  border-width: 1px;
  border-style: solid;
  border-color: rgba(5, 5, 6, 0.24)
}

.tooltip-container {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.color-swatch .tooltip { 
  visibility: hidden;
  width: 8em; /* Size of the popup, adjust as needed*/
  height: 8em;
  color: #fff;
  position: absolute;
  z-index: 1;
  bottom: 125%;
  left: 50%;
  margin-left: -4em; /* Half of the width to center it */
  opacity: 0; 
  transition: opacity 0.3s;
  background-image: 
    linear-gradient(135deg, #dcdcde 25%, transparent 0%, transparent 75%, #dcdcde 0%),
    linear-gradient(135deg, #dcdcde 25%, transparent 0%, transparent 75%, #dcdcde 0%);
  background-size: 4em 4em;
  background-position: 0 0, 2em 2em;
}

.color-swatch .tooltip-container:hover .tooltip {
  visibility: visible;
  opacity: 1;
}
```

Inject Html:
``` html
<span class="color-block">
    {original}
    <span class="color-swatch">
        <span class="tooltip-container" style="background-color:#{rgbCode}{alphaCode};">
            <span class="tooltip">
                <span style="background-color:#{rgbCode}{alphaCode};"></span>
            </span>
        </span>
    </span>
</span>
```