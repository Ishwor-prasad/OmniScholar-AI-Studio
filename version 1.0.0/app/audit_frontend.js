const fs = require("fs");
const path = require("path");

const htmlPath = path.join(__dirname, "static", "index.html");
const jsPath = path.join(__dirname, "static", "app.js");
const cssPath = path.join(__dirname, "static", "style.css");

const html = fs.readFileSync(htmlPath, "utf8");
const js = fs.readFileSync(jsPath, "utf8");
const css = fs.readFileSync(cssPath, "utf8");

const htmlIds = new Set();
const idRegex = /id=["']([^"']+)["']/g;
let m;
while ((m = idRegex.exec(html)) !== null) {
    htmlIds.add(m[1]);
}

const jsIdRegex = /getElementById\(['"]([^'"]+)['"]\)/g;
const jsIds = new Set();
while ((m = jsIdRegex.exec(js)) !== null) {
    jsIds.add(m[1]);
}

const missing = [];
for (const id of jsIds) {
    if (!htmlIds.has(id) && !js.includes(`id="${id}"`) && !js.includes(`id='${id}'`)) {
        missing.push(id);
    }
}

console.log(`Unique IDs in index.html: ${htmlIds.size}`);
console.log(`Unique getElementById calls in app.js: ${jsIds.size}`);
if (missing.length > 0) {
    console.error("Missing IDs in index.html:", missing);
    process.exit(1);
} else {
    console.log("SUCCESS: 100% of getElementById calls map to valid DOM elements!");
}

let openB = (css.match(/\{/g) || []).length;
let closeB = (css.match(/\}/g) || []).length;
console.log(`CSS Braces: ${openB} open, ${closeB} close`);
if (openB !== closeB) {
    console.error("CSS brace parity failure");
    process.exit(1);
} else {
    console.log("SUCCESS: CSS brace parity verified!");
}
