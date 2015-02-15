class DataCollector():
    """
    A Class designed to collect the links related to a certain keyword, passed as an argument to the constructor method
    of this class.
    The links are first collected from google, Yahoo and Bing, and is then used to retrieve the pages corresponding to
    these links, extract text from the links and return it.

    Class Managed By : Thumssy Nazar
    """

    def __init__(self, keyword, type):
        """
        The Constructor method.
        :param keyword: keyword to be searched
        :param type: Type of links to be collected (textual/image/video/file)
        :return: self.data
        """
        self.type = type
        self.keyword = keyword  # keyword to be searched
        self.data = []  # the final data array. contains data as [title, [link, data], [title, link, data] ...]
        self.glinks = []  # links from google
        self.ylinks = []  # links from yahoo
        self.blinks = []  # links from bing
        pass

    def get_links(self, pages):
        """
        Get links from the search engines and fill them to the respective lists.
        It gets pages of links from Search Engines, sends them to the formatter functions ang gets the lists.
        :param pages: a variable to see number of search pages to be covered
        :return: nothing
        """
        pass

    def google_formatter(self, data):
        """
        Format recieved links
        :param ddata:
        :return: formatted list
        """

        pass

    def yahoo_formatter(self, data):
        """
        Format recieved links
        :param ddata:
        :return: formatted list
        """
        pass

    def bing_formatter(self, data):
        """
        Format recieved links
        :param ddata:
        :return: formatted list
        """
        pass

    def data_collector(self, url):
        """
        Gets the HTML data from the page specified by the URL.
        :param url: url from which data is to be retrieved.
        :return: list with HTML data
        """
        pass

    def extract_text(self, data):
        """
        Extract necessary text from HTML data.
        :param data: HTML data from data_collector
        :return: List of textual data
        """

    def video_link_collector(self, count):
        """
        Collect links for videos related to self.keyword
        :param count: number of links needed
        :return: list of links
        """
        pass

    def image_link_collector(self, count):
        """
        Collect links for images related to self.keyword from google images
        :param count: number of links needed
        :return: list of links
        """
        pass

    def file_link_collector(self, count):
        """
        Collect links for files(doc, txt, pdf, mp3) related to self.keyword
        :param count: number of links needed
        :return: list of links
        """
        pass