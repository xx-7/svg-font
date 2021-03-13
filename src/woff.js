const {  series } = require('gulp');
const { join } = require('path');
const fs = require('fs-extra');

const fontName = 'xdfont';
const distDir = '../dist/xdfont'
const distPath = join(__dirname, `${distDir}`);


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

exports.default = series(encodeWoff2);