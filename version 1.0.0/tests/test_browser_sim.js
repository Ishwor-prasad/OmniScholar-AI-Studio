const fs = require('fs');
const path = require('path');

let jsdom = null;
try {
    jsdom = require('jsdom');
} catch (e) {
    // jsdom not installed
}

const htmlPath = path.join(__dirname, "static", "index.html");
const jsPath = path.join(__dirname, "static", "app.js");

const html = fs.readFileSync(htmlPath, "utf8");
const js = fs.readFileSync(jsPath, "utf8");

if (jsdom) {
    const dom = new jsdom.JSDOM(html, { runScripts: "dangerously", resources: "usable" });
    const { window } = dom;
    window.addEventListener("error", (e) => {
        console.error("DOM Window Error:", e.error);
    });
    console.log("DOM loaded successfully.");
} else {
    console.log("Auditing addEventListener calls in app.js...");
    const lines = js.split("\n");
    let errors = 0;
    lines.forEach((line, i) => {
        if (line.includes(".addEventListener(") && line.includes("document.getElementById(")) {
            const match = line.match(/document\.getElementById\(['"]([^'"]+)['"]\)/);
            if (match) {
                const id = match[1];
                if (!html.includes(`id="${id}"`) && !html.includes(`id='${id}'`) && !js.includes(`id="${id}"`)) {
                    console.error(`Line ${i + 1}: Element with id '${id}' not found in HTML or dynamic JS templates!`);
                    errors++;
                }
            }
        }
    });
    if (errors === 0) {
        console.log("SUCCESS: All addEventListener targets exist in HTML or dynamic templates!");
    }
}
