const { src, dest, series } = require('gulp');
const { join } = require('path');
const iconfont = require('gulp-iconfont');
const iconfontCss = require('gulp-iconfont-css');
const fs = require('fs-extra');




const svgDir = join(__dirname, '../assets/svg');
const template = join(__dirname, './template.tpl');

const formats = ['ttf', 'woff', 'woff2', 'svg'];

const distDir = '../dist'
const distPath = join(__dirname, `${distDir}`);

const fontName = 'xdfont';
const cssClass = 'xd-icon';

function genFont() {
    return src([`${svgDir}/*.svg`])
    .pipe(
      iconfontCss({
        fontName: fontName,
        cssClass: cssClass,
        path: template,
        targetPath: `${distDir}/${fontName}.scss`,
      })
    )
    .pipe(
      iconfont({
        fontName:fontName,
        formats,
      })
    )
    .pipe(dest(distPath));
}

function encodeWoff2(done) {
    const fontPath = `./${fontName}.woff2`;
    const srcFile = join(distPath, `${fontName}.scss`);
    const woff2Base64 = fs.readFileSync(join(distPath, `${fontName}.woff2`), 'base64');
    const woff2DataUrl = `data:font/ttf;base64,${woff2Base64}`;
  
    fs.writeFileSync(
      join(distPath, `en-${fontName}.scss`),
      fs.readFileSync(srcFile, 'utf-8').replace(fontPath, woff2DataUrl)
    );
  
    done();
  }

exports.default = series(genFont, encodeWoff2);