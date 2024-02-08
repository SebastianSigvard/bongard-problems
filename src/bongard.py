import requests
import pdfkit
import re


def generate_pdf_from_html(html_content, pdf_path):
    try:
        # Configure PDF options if needed
        pdf_options = {
            'page-size': 'A5',
            'margin-top': '6mm',
            'margin-right': '2mm',
            'margin-bottom': '2mm',
            'margin-left': '2mm',
        }

        # Generate PDF from HTML content
        pdfkit.from_string(html_content, pdf_path, options=pdf_options)

        print(f"PDF successfully generated at: {pdf_path}")

    except Exception as e:
        print(f"Error generating PDF: {e}")


url = "https://www.oebp.org/solve.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8",
    "Sec-Ch-UA": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-UA-Mobile": "?0",
    "Sec-Ch-UA-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

html_content = '''
<html>
    <head>
        <style>
            body {
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
            }
            .page {
                text-align: center;
            }
            .page-break {
                page-break-before: always;
            }
            p {
                line-height: 1.2;
                font-size: large;
                font-family: "Lucida Handwriting", Cursive;
                -webkit-transform: rotate(-180deg); 
                -moz-transform: rotate(-180deg); 
            }
        </style>
    </head>
    <body>
        <center>
'''

num_pages = 222

pattern = r'<button type="submit" name="bp" value="(\d+)">Next</button>'
next = 1

for i in range(num_pages):
    html_content = html_content + '<div class="page">'
    for j in range(1, 3):
        params = {"bp": str(next), "referrer": "https://www.oebp.org/solve.php?bp=1246"}

        response = requests.get(url, headers=headers, params=params)

        page = response.text

        match = re.search(pattern, page)
        next = match.group(1)

        s_img_idx = page.find('<img src=') + 10
        e_img_idx = page.find('\" /><')

        s_sol_idx = page.find('"display: none;">') + 17
        e_sol_idx = page[s_sol_idx:].find('</p>')

        encoded_image = page[s_img_idx:e_img_idx]
        solution = page[s_sol_idx:e_sol_idx + s_sol_idx]

        html_content = html_content + f'''
            <h2>BP{2*i + j}</h2>
            <img src="{encoded_image}" width="515" height="326"/>
            <p>Solution: {solution}</p>
        '''

    html_content = html_content + '''</div>
        <div class="page-break"></div>
    '''

html_content = html_content + '''
        <center>
    </body>
</html>
'''

pdf_path = "output.pdf"

generate_pdf_from_html(html_content, pdf_path)
