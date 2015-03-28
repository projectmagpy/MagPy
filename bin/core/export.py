class csv:
    def __init__(self, data):
        self.data = data

    def export(self, filename, append=True):
        if filename.split('.')[-1] != '.csv':
            filename += '.csv'
        mode = 'a' if append else 'w'
        with open(filename, mode) as f:
            for row in self.data:
                f.write(','.join(row) + "\n")
        f.close()


class docx:
    def __init__(self, title, data, text=True):
        self.data = data.split("\n")
        self.title = title
        self.text = text

    def export(self, filename):
        from docx import Document

        if filename.split('.')[-1] != '.docx':
            filename += '.docx'
        document = Document()
        h = document.add_heading(self.title, 0)

        if self.text:
            print self.data
            for p in self.data:
                document.add_paragraph(p)
                print p
        else:
            table = document.add_table(rows=len(self.data), cols=len(self.data[0]))
            r, c = -1, -1
            for row in self.data:
                r += 1
                c = 0
                for col in row:
                    hdr_cells = table.rows[0].cells
                    hdr_cells[c].text = col
                    c += 1

        document.add_page_break()
        document.save(filename)


class text:
    def __init__(self, data):
        self.data = data

    def export(self, filename, append=True):
        if filename.split('.')[-1] != '.txt':
            filename += '.txt'
        mode = 'a' if append else 'w'
        with open(filename, mode) as f:
            for p in self.data:
                f.write(p + "\n")
        f.close()


class json:
    def __init__(self, data):
        self.data = data

    def export(self, filename, append=True):
        import demjson

        js = demjson.encode(self.data)
        if filename.split('.')[-1] != '.json':
            filename += '.json'
        mode = 'a' if append else 'w'
        with open(filename, mode) as f:
            f.write(js)
        f.close()

if __name__ == '__main__':
    import urllib
    from BeautifulSoup import BeautifulSoup as b
    bb = b(urllib.urlopen("http://www.thehindu.com/sci-tech/science/irnss1d-launch/article7043608.ece?homepage=true").read())
    bs = bb.findAll("p")
    docx(bb.find("title").text, "\n".join([s.text for s in bs])).export("a")