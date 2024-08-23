from PyPDF2 import PdfReader


def get_lines(filename):
    reader = PdfReader(filename)
    all_page_lines = []
    for page in reader.pages:
        page_text = page.extract_text()
        page_lines = page_text.split("\n")
        all_page_lines += page_lines[2:]
    return all_page_lines


def format_desc_to_abbrv(full_defs):
    resp = {}
    for row in full_defs:
        desc, abbrv = row.split(" ")
        resp[desc] = abbrv
    return resp


def format_abbrv_to_desc(full_defs):
    resp = {}
    for row in full_defs:
        desc, abbrv = row.split(" ")
        resp[abbrv] = desc
    return resp


definitions = get_lines("XML_Tags.pdf")


counts = {}
for key, value in format_desc_to_abbrv(definitions).items():
    if value in counts:
        counts[value] += [key]
    else:
        counts[value] = [key]

for abbrv, counted in counts.items():
    if len(counted) > 1:
        print(abbrv, counted)
