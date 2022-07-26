// Scrapes the site to make sure the span element is loading and returning a visitor count

const puppeteer = require('puppeteer');

(async () => {

    let url = 'https://jhtresume.com';

    let browser = await puppeteer.launch();
    let page = await browser.newPage();

    await page.goto(url);
    await page.waitForTimeout(3000);
    
    let data = await page.evaluate(() => {

        let counter = document.querySelector('span').innerText;
        console.log(counter)
        return {
            counter
        }
    })

    console.log(data);

    let count = data['counter']
    if (!count) {
        throw new Error("FAIL: No count value")
    } else {
        console.log('PASS')
    }

    await browser.close();
})(); 