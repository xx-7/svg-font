/* stylelint-disable selector-pseudo-element-colon-notation */
/* stylelint-disable font-family-no-missing-generic-family-keyword */
@font-face {
  font-family: "<%= fontName %>";
  src: url("./<%= fontName %>.woff2") format("woff2"), url("./<%= fontName %>.woff") format("woff"),
    url("./<%= fontName %>.ttf") format("truetype"),
    url("./<%= fontName %>.svg?#<%= fontName %>") format("svg");
  font-weight: normal;
  font-style: normal;
}

.<%= cssClass%> {
  position: relative;
  display: inline-block;
  font: normal normal normal 14px/1 '<%= fontName %>';
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;

  &::before {
    display: inline-block;
  }
}

<% _.each(glyphs, function(glyph) { %>.<%= cssClass%>.<%= glyph.fileName %>::before {
  content: '\<%= glyph.codePoint %>';
}

<% }); %>