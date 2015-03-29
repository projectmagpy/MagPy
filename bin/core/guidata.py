tabHeadings = ["File Management", "Page Navigation", "Selection", "Constraints", "Export"]
btns = [
    ["Text", "Images", "Videos", "PDF", "HTML"],
    ["Search Engine", "Single URL", "URL list", "Iterative", "Recursive"],
    ["HTML attributes", "Whole HTML", "Whole Text", "From Text", "Regular Expressions"],
    ["Size", "Count", "Consists of", "Not Consists of"],
    ["Doc", "Text file", "Voice"]
]


inputs = [
    [
        ["Enter Keyword or URL containing the file *"],
        ["Enter Keyword or URL containing the file *"],
        ["Enter Keyword or URL containing the file *"],
        ["Enter Keyword or URL containing the file *"],
        ["Enter Keyword or URL containing the file *"]
    ],
    [
        ["Keyword *", "Number of Pages", "Type"],
        ["URL *"],
        ["URL " + str(i) for i in range(1, 6)],
        ["Base URL *", "Type(text/num) *", "Starting character *", "Ending Character *"],
        ["Base URL *", "Depth", "Excluded domains", "Included domains"],
    ],
    [
        ["Tag", "Class", "ID"],
        [],
        [],
        ["URL 1 *", "Text 1 *", "URL 2 *", "Text 2 *", "URL 3", "Text 3"],
        ["Pattern *"]
    ],
    [
        ["Size", "Type"],
        ["Pattern *"],
        ["Words *"],
        ["Words *"]
    ],
    [
        ["filename"],
        ["filename"],
        [],
        ["If not Based on Search results, enter Keyword/URL"],
        ["If not Based on Search results, enter Keyword/URL"],
        ["If not Based on Search results, enter Keyword/URL"],
        ["If not Based on Search results, enter Keyword/URL"]

    ]
]
