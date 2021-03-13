import fontforge
import os

def getSvgs(_path, maps):
    if os.path.exists(_path):
        files = os.listdir(_path)
        for fi in files:
            file = os.path.join(_path,fi)            
            if os.path.isdir(file):
                getSvgs(file, maps)                  
            else:
                key = os.path.splitext(fi)[0]
                if key in maps:
                    print("%s is more... " % (key))
                else :
                    maps.update({key: file})

def clearDir(_path):
    if os.path.exists(_path):
        files = os.listdir(_path)
        for fi in files:
            file = os.path.join(_path,fi)            
            if os.path.isdir(file):
                clearDir(file)
            else :
                os.remove(file)
        os.rmdir(_path)

def addSvgs(font, maps, startUnicode):
    unicode = startUnicode
    keys = maps.keys()
    for key in iter(keys):
        uinName = "uni%X" % (unicode)
        font.createChar(unicode,uinName)
        glyph = font.createMappedChar(uinName)
        glyph.importOutlines(maps[key])
        glyph.width = font.em
        glyph.autoHint()      
        maps.update({key: unicode})
        unicode = unicode + 1

def outStyles(font, maps, dst, clsPre):
    styles = '''
@font-face {
  font-family: "'''+ font.fontname + '''";
  src: url("./'''+ font.fontname + '''.woff2") format("woff2"), url("./'''+ font.fontname + '''.woff") format("woff"),
    url("./'''+ font.fontname + '''.ttf") format("truetype"),
    url("./'''+ font.fontname + '''.svg?#'''+ font.fontname + '''") format("svg");
  font-weight: normal;
  font-style: normal;
}
.'''+ clsPre + ''' {
  display: inline-block;
  font-family: "'''+ font.fontname + '''" !important;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  text-rendering: auto;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  vertical-align: middle;
}'''
    keys = maps.keys()
    for key in iter(keys):
        styles += '''
.'''+ clsPre + '''-'''+ key + ''':before {
  content: "'''+ "\\%X" % (maps[key])  + '''";
}'''
    file = open(dst, 'w')
    file.write(styles)
    file.flush()
    file.close()

def outputFont(font, dst, maps, clsPre):
    dstPath = "%s/%s" % (dst, font.fontname)
    clearDir(dstPath)
    os.makedirs(dstPath) 
    font.generate("%s/%s.svg" % (dstPath, font.fontname))
    font.generate("%s/%s.ttf" % (dstPath, font.fontname))
    font.generate("%s/%s.woff" % (dstPath, font.fontname))
    font.generate("%s/%s.woff2" % (dstPath, font.fontname))
    outStyles(font, maps, "%s/%s.scss" % (dstPath, font.fontname), clsPre)

def createFont(name):
    font = fontforge.font()
    font.familyname = fontName
    font.fontname = fontName
    font.fondname = fontName
    font.fullname = fontName
    font.copyright = ' '
    font.comment = ' '
    font.woffMetadata = ' '
    font.version = '1.0.1'
    font.encoding = "utf-8"
    font.uwidth = 0
    font.upos = 0
    font.ascent = 960
    font.descent = 64
    font.em = 1024
    return font

svgsList = {}
fontName = 'xdfont'
getSvgs('./assets/svg2', svgsList)
xdfont = createFont(fontName)
addSvgs(xdfont, svgsList, 0xea01)
outputFont(xdfont, './dist', svgsList, 'xd-icon')


