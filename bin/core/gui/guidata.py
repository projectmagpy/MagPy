tabHeadings = ["File Management", "Page Navigation", "Selection", "Constraints", "Export"]
btns = [
    ["Text", "Images", "Videos", "Files", "HTML"],
    ["Search Engine", "Single URL", "URL list", "Iterative", "Recursive", "Keyword"],
    ["HTML attributes", "Whole HTML", "Whole Text", "From Text", "Regular Expressions"],
    ["Size", "Count", "Consists of", "Not Consists of"],
    ["Doc", "PDF", "Text file", "Image", "Videos", "XML", "JSON"]
]

inputs = [
    [
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"]
    ],
    [
        ["Keyword", "Number of Results"],
        ["URL"],
        ["URL " + str(i) for i in range(1, 10)],
        ["Base URL", "Type(text/num)", "Starting character", "Ending Character"],
        ["Base URL", "Depth", "Excluded domains", "Included domains"],
        ["Keyword"]
    ],
    [
        ["Tag", "Class", "Name", "ID"],
        [],
        [],
        ["URL 1", "Text 1", "URL 2", "Text 2", "URL 3", "Text 3"],
        ["Pattern"]
    ],
    [
        ["Size", "Type"],
        ["Regular Expression"],
        ["Words"],
        ["Words"]
    ],
    [
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"],
        ["If not Based on Previous Keyword, enter Keyword", "URL"]
    ]
]
