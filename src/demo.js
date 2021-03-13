const path = require('path');
const fs = require('fs');



async function getall(src) {
    const dir = await fs.promises.opendir(src);
    let names = '';
    for await (const dirent of dir) {
        const name = path.parse(dirent.name).name;
        names += `<CopyButton
    text={this.getIconString("${name}")}
    onCopySuccess="${name} 已复制到剪贴板"
    >
    <div
        className="zi-grid-item"
        data-index="${name}"
    >
        <Icon type="${name}" />
        <span className="zi-grid-item-name">${name}</span>
    </div>
</CopyButton>\n`
    }

    fs.writeFileSync(
        path.join(__dirname, `../dist`, 'demo.js'),
        names
    );
}

getall(path.join('./assets', 'svg2'));