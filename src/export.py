import fontforge
import os


font = fontforge.open('./assets/test.woff2')
uinName = "uni%X" % (0xe801)
glyphs = font.glyphs()
for glyph in glyphs:
    glyph.export("./dist/svg/%s.svg" % (glyph.glyphname))
    print("export %s " % (glyph.glyphname))