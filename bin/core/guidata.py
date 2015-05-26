tabHeadings = ["File Management", "Page Navigation", "Selection", "Constraints", "Export"]
btns = [
    ["Images", "Videos", "Documents", "Regex"],
    ["Search Engine", "Single URL", "URL list", "Iterative"],
    ["HTML attributes", "Whole HTML", "Whole Text", "Pattern"],
    ["Size", "Consists of", "Not Consists of"],
    ["Doc", "Text file", "Voice"]
]


inputs = [
    [
        ["URL"],
        ["URL"],
        ["URL"],
        ["URL", "Pattern"],
        ["URL*"],
        ["URL*"]
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
        ["Pattern *"]
    ],
    [
        ["Size"],
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
