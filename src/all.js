const path = require('path');
const fs = require('fs');

let names = '';

async function getall(src) {
  const dir = await fs.promises.opendir(src);
  for await (const dirent of dir) {
    const name = path.parse(dirent.name).name;
    names += `'${name}', `
  }
  console.info(`[${names}]`);
}

getall(path.join('./assets', 'svg'));



