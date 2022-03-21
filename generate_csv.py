"""Generating a .csv file from the metadata of PDFs accesible from ArXiv.org"""

import arxiv
import csv


search = arxiv.Search(
    # Filtering onto "Computer Science : Artificial Intelligence" category
    query = "cat:cs.AI",
    max_results = 1000,
    sort_by = arxiv.SortCriterion.SubmittedDate
)

rows = [['ID', 'Title', 'Authors', 'Date'] ]

for result in search.results():
    rows.append(list([str(result.entry_id), str(result.title), str(result.authors), str(result.published)]))
    print([str(result.entry_id), str(result.title), str(result.authors), str(result.published)])

with open('DataBase.csv', 'w',newline ='') as f:
    write = csv.writer(f)
    write.writerows(rows)

