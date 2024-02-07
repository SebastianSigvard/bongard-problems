import pdfkit


def generate_pdf_from_html(html_content, pdf_path):
    try:
        # Configure PDF options if needed
        pdf_options = {
            'page-size': 'A5',
            'margin-top': '20mm',
            'margin-right': '2mm',
            'margin-bottom': '2mm',
            'margin-left': '2mm',
        }

        # Generate PDF from HTML content
        pdfkit.from_string(html_content, pdf_path, options=pdf_options)

        print(f"PDF successfully generated at: {pdf_path}")

    except Exception as e:
        print(f"Error generating PDF: {e}")


# Example usage:
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
        </style>
    </head>
    <body>
        <center>
        <div class="page">
            <h1>BP1</h1>
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgMAAAFGAQMAAADNaA5WAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEGElEQVR4nO3aQavUOhQA4JMXsA8cpy4HLLf3J1QEKTjM+A/8Cxf8A3WlC/Fl558SjLgV/ANvkbfRnRRXXQx3bNJ2evIuj3knZ3AuegIDE+h896ZNTtKcABwpT49dcLT8LoLao+JKVLmehRxfBLjS9gLmLu+jyh+z8Cf+k2BQ7b4IIoggggj/KeR8wXKFgiloWJGF/Q4Lpa2ogh5msUnY0oXS5AYJFV3YgLZIaBxZaAAcEq7cQ6rQBuQgOLKg+uvrSHhiaIK/CUXUigdUof8skNBY6rjI+s8dlrAclUmoycJibMkkFLY0PCG3LyxNWHnBIMG0ji6oSci7fqDZhibUkXDdC6amC2BHYZ3bZehgFKHCQq3dMjzgZKGB3ToEa4aw7UIHSxZcGGiaJfjCEewgGK6gaALuUepMQgHzyGIIMAomRcDxQQ8C8WniKJcmZKOCBGKv1jeEJXFk+V8VkdCHGfKctY6EbEeced088473oaXP3W0sAFFYzysQlSaUkBmekH3fA68Val4NhubQBSjNJKhEYSinEUAEPONwhCu2cCgiiCCCCCKI8PMEdhbmWHl6/BIRfiFB8noiiCCCCKcTDFcY9gw4ghYhfM0cV7jDFhbN+YWiOr9Q1+cXqoIrNJGgqYLu10yxYIhCv2Jz+RckZC21Fa+e2X5JNwv5jir43e4tEhYh+00RSv/lNRIyRxR8RhW6WSg8RxJCCsxhYUsUlBuUSViFp0HqUd3QkkOmGFRH3reHCyT0A3VLFPqfv4qF3NKE5Zx98KUJkxhJKIYt4tMJjpxb9Ik9hwR7EoH4LKr4DEaKoLDgFxPEnBo0uamQYOhCW1okjEk6kuD+autYWBAF2zEF9dGt0VkUn6wknhxQn+0GCf5QyYoYo95DjgSf6iSef9BryD7Ngk/7VsQsbQvqG1eA61nwDWqI0d6GsDYJqwQBIsF3DUcTFhDF6g2E4Ul9v0DngjKbJMAs6JYr9M3wA5wj5EYzBd364cl6U3vNFvK3XEF/5Qrwhi0UbAFEEEEEEUT4SYLk9UQ4qSB5PRFEEOG2CMpyBe3YQsUWLnlCxW7FzqcXg6CmWZ8o+K2gQch2XGG5TBO6g7DSaUKFBJMkwEGoprPqycIlW7hKELobgt47kjB1gHTh0w0hM1ck4e9IqLTfqaUJTSTUGcBdonAoQbi4oP8PsZC/4wo+LcUTfBFhFIh98qaQEcfFqYSCPfNu2MJjluDDM0/wu+RrlrCwIWPAFIDdCp4wTnRnX8udUlixhYItbG6B8IYtvGQLzw1X+IcrqA+WKxjHFMJkwRKycUlCEC7+LdRUYRsL+b6jCo9CLZ+EMlUoZ2GX0IrMeGcQxvBAvJP37CxMhfY0+3BfnlsY3oxuUawWQQQRRBDhfwuS17stwg8tZFl1dQNqTQAAAABJRU5ErkJggg==" />
            <h1>BP2</h1>
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgMAAAFGAQMAAADNaA5WAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEGElEQVR4nO3aQavUOhQA4JMXsA8cpy4HLLf3J1QEKTjM+A/8Cxf8A3WlC/Fl558SjLgV/ANvkbfRnRRXXQx3bNJ2evIuj3knZ3AuegIDE+h896ZNTtKcABwpT49dcLT8LoLao+JKVLmehRxfBLjS9gLmLu+jyh+z8Cf+k2BQ7b4IIoggggj/KeR8wXKFgiloWJGF/Q4Lpa2ogh5msUnY0oXS5AYJFV3YgLZIaBxZaAAcEq7cQ6rQBuQgOLKg+uvrSHhiaIK/CUXUigdUof8skNBY6rjI+s8dlrAclUmoycJibMkkFLY0PCG3LyxNWHnBIMG0ji6oSci7fqDZhibUkXDdC6amC2BHYZ3bZehgFKHCQq3dMjzgZKGB3ToEa4aw7UIHSxZcGGiaJfjCEewgGK6gaALuUepMQgHzyGIIMAomRcDxQQ8C8WniKJcmZKOCBGKv1jeEJXFk+V8VkdCHGfKctY6EbEeced088473oaXP3W0sAFFYzysQlSaUkBmekH3fA68Val4NhubQBSjNJKhEYSinEUAEPONwhCu2cCgiiCCCCCKI8PMEdhbmWHl6/BIRfiFB8noiiCCCCKcTDFcY9gw4ghYhfM0cV7jDFhbN+YWiOr9Q1+cXqoIrNJGgqYLu10yxYIhCv2Jz+RckZC21Fa+e2X5JNwv5jir43e4tEhYh+00RSv/lNRIyRxR8RhW6WSg8RxJCCsxhYUsUlBuUSViFp0HqUd3QkkOmGFRH3reHCyT0A3VLFPqfv4qF3NKE5Zx98KUJkxhJKIYt4tMJjpxb9Ik9hwR7EoH4LKr4DEaKoLDgFxPEnBo0uamQYOhCW1okjEk6kuD+autYWBAF2zEF9dGt0VkUn6wknhxQn+0GCf5QyYoYo95DjgSf6iSef9BryD7Ngk/7VsQsbQvqG1eA61nwDWqI0d6GsDYJqwQBIsF3DUcTFhDF6g2E4Ul9v0DngjKbJMAs6JYr9M3wA5wj5EYzBd364cl6U3vNFvK3XEF/5Qrwhi0UbAFEEEEEEUT4SYLk9UQ4qSB5PRFEEOG2CMpyBe3YQsUWLnlCxW7FzqcXg6CmWZ8o+K2gQch2XGG5TBO6g7DSaUKFBJMkwEGoprPqycIlW7hKELobgt47kjB1gHTh0w0hM1ck4e9IqLTfqaUJTSTUGcBdonAoQbi4oP8PsZC/4wo+LcUTfBFhFIh98qaQEcfFqYSCPfNu2MJjluDDM0/wu+RrlrCwIWPAFIDdCp4wTnRnX8udUlixhYItbG6B8IYtvGQLzw1X+IcrqA+WKxjHFMJkwRKycUlCEC7+LdRUYRsL+b6jCo9CLZ+EMlUoZ2GX0IrMeGcQxvBAvJP37CxMhfY0+3BfnlsY3oxuUawWQQQRRBDhfwuS17stwg8tZFl1dQNqTQAAAABJRU5ErkJggg==" />
        </div>
        <div class="page-break"></div>
        <div class="page">
            <h1>BP1</h1>
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgMAAAFGAQMAAADNaA5WAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEGElEQVR4nO3aQavUOhQA4JMXsA8cpy4HLLf3J1QEKTjM+A/8Cxf8A3WlC/Fl558SjLgV/ANvkbfRnRRXXQx3bNJ2evIuj3knZ3AuegIDE+h896ZNTtKcABwpT49dcLT8LoLao+JKVLmehRxfBLjS9gLmLu+jyh+z8Cf+k2BQ7b4IIoggggj/KeR8wXKFgiloWJGF/Q4Lpa2ogh5msUnY0oXS5AYJFV3YgLZIaBxZaAAcEq7cQ6rQBuQgOLKg+uvrSHhiaIK/CUXUigdUof8skNBY6rjI+s8dlrAclUmoycJibMkkFLY0PCG3LyxNWHnBIMG0ji6oSci7fqDZhibUkXDdC6amC2BHYZ3bZehgFKHCQq3dMjzgZKGB3ToEa4aw7UIHSxZcGGiaJfjCEewgGK6gaALuUepMQgHzyGIIMAomRcDxQQ8C8WniKJcmZKOCBGKv1jeEJXFk+V8VkdCHGfKctY6EbEeced088473oaXP3W0sAFFYzysQlSaUkBmekH3fA68Val4NhubQBSjNJKhEYSinEUAEPONwhCu2cCgiiCCCCCKI8PMEdhbmWHl6/BIRfiFB8noiiCCCCKcTDFcY9gw4ghYhfM0cV7jDFhbN+YWiOr9Q1+cXqoIrNJGgqYLu10yxYIhCv2Jz+RckZC21Fa+e2X5JNwv5jir43e4tEhYh+00RSv/lNRIyRxR8RhW6WSg8RxJCCsxhYUsUlBuUSViFp0HqUd3QkkOmGFRH3reHCyT0A3VLFPqfv4qF3NKE5Zx98KUJkxhJKIYt4tMJjpxb9Ik9hwR7EoH4LKr4DEaKoLDgFxPEnBo0uamQYOhCW1okjEk6kuD+autYWBAF2zEF9dGt0VkUn6wknhxQn+0GCf5QyYoYo95DjgSf6iSef9BryD7Ngk/7VsQsbQvqG1eA61nwDWqI0d6GsDYJqwQBIsF3DUcTFhDF6g2E4Ul9v0DngjKbJMAs6JYr9M3wA5wj5EYzBd364cl6U3vNFvK3XEF/5Qrwhi0UbAFEEEEEEUT4SYLk9UQ4qSB5PRFEEOG2CMpyBe3YQsUWLnlCxW7FzqcXg6CmWZ8o+K2gQch2XGG5TBO6g7DSaUKFBJMkwEGoprPqycIlW7hKELobgt47kjB1gHTh0w0hM1ck4e9IqLTfqaUJTSTUGcBdonAoQbi4oP8PsZC/4wo+LcUTfBFhFIh98qaQEcfFqYSCPfNu2MJjluDDM0/wu+RrlrCwIWPAFIDdCp4wTnRnX8udUlixhYItbG6B8IYtvGQLzw1X+IcrqA+WKxjHFMJkwRKycUlCEC7+LdRUYRsL+b6jCo9CLZ+EMlUoZ2GX0IrMeGcQxvBAvJP37CxMhfY0+3BfnlsY3oxuUawWQQQRRBDhfwuS17stwg8tZFl1dQNqTQAAAABJRU5ErkJggg==" />
            <h1>BP2</h1>
            <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgMAAAFGAQMAAADNaA5WAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEGElEQVR4nO3aQavUOhQA4JMXsA8cpy4HLLf3J1QEKTjM+A/8Cxf8A3WlC/Fl558SjLgV/ANvkbfRnRRXXQx3bNJ2evIuj3knZ3AuegIDE+h896ZNTtKcABwpT49dcLT8LoLao+JKVLmehRxfBLjS9gLmLu+jyh+z8Cf+k2BQ7b4IIoggggj/KeR8wXKFgiloWJGF/Q4Lpa2ogh5msUnY0oXS5AYJFV3YgLZIaBxZaAAcEq7cQ6rQBuQgOLKg+uvrSHhiaIK/CUXUigdUof8skNBY6rjI+s8dlrAclUmoycJibMkkFLY0PCG3LyxNWHnBIMG0ji6oSci7fqDZhibUkXDdC6amC2BHYZ3bZehgFKHCQq3dMjzgZKGB3ToEa4aw7UIHSxZcGGiaJfjCEewgGK6gaALuUepMQgHzyGIIMAomRcDxQQ8C8WniKJcmZKOCBGKv1jeEJXFk+V8VkdCHGfKctY6EbEeced088473oaXP3W0sAFFYzysQlSaUkBmekH3fA68Val4NhubQBSjNJKhEYSinEUAEPONwhCu2cCgiiCCCCCKI8PMEdhbmWHl6/BIRfiFB8noiiCCCCKcTDFcY9gw4ghYhfM0cV7jDFhbN+YWiOr9Q1+cXqoIrNJGgqYLu10yxYIhCv2Jz+RckZC21Fa+e2X5JNwv5jir43e4tEhYh+00RSv/lNRIyRxR8RhW6WSg8RxJCCsxhYUsUlBuUSViFp0HqUd3QkkOmGFRH3reHCyT0A3VLFPqfv4qF3NKE5Zx98KUJkxhJKIYt4tMJjpxb9Ik9hwR7EoH4LKr4DEaKoLDgFxPEnBo0uamQYOhCW1okjEk6kuD+autYWBAF2zEF9dGt0VkUn6wknhxQn+0GCf5QyYoYo95DjgSf6iSef9BryD7Ngk/7VsQsbQvqG1eA61nwDWqI0d6GsDYJqwQBIsF3DUcTFhDF6g2E4Ul9v0DngjKbJMAs6JYr9M3wA5wj5EYzBd364cl6U3vNFvK3XEF/5Qrwhi0UbAFEEEEEEUT4SYLk9UQ4qSB5PRFEEOG2CMpyBe3YQsUWLnlCxW7FzqcXg6CmWZ8o+K2gQch2XGG5TBO6g7DSaUKFBJMkwEGoprPqycIlW7hKELobgt47kjB1gHTh0w0hM1ck4e9IqLTfqaUJTSTUGcBdonAoQbi4oP8PsZC/4wo+LcUTfBFhFIh98qaQEcfFqYSCPfNu2MJjluDDM0/wu+RrlrCwIWPAFIDdCp4wTnRnX8udUlixhYItbG6B8IYtvGQLzw1X+IcrqA+WKxjHFMJkwRKycUlCEC7+LdRUYRsL+b6jCo9CLZ+EMlUoZ2GX0IrMeGcQxvBAvJP37CxMhfY0+3BfnlsY3oxuUawWQQQRRBDhfwuS17stwg8tZFl1dQNqTQAAAABJRU5ErkJggg==" />
        </div>
        <center>
    </body>
</html>
'''
pdf_path = "output.pdf"

generate_pdf_from_html(html_content, pdf_path)
